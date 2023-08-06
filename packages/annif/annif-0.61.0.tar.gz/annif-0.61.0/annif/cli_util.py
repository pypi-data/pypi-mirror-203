"""Utility functions for Annif CLI commands"""


import collections
import itertools
import os
import sys

import click
import click_log
from flask import current_app

import annif
from annif.exception import ConfigurationException
from annif.project import Access

logger = annif.logger


def _set_project_config_file_path(ctx, param, value):
    """Override the default path or the path given in env by CLI option"""
    with ctx.obj.load_app().app_context():
        if value:
            current_app.config["PROJECTS_CONFIG_PATH"] = value


def common_options(f):
    """Decorator to add common options for all CLI commands"""
    f = click.option(
        "-p",
        "--projects",
        help="Set path to project configuration file or directory",
        type=click.Path(dir_okay=True, exists=True),
        callback=_set_project_config_file_path,
        expose_value=False,
        is_eager=True,
    )(f)
    return click_log.simple_verbosity_option(logger)(f)


def backend_param_option(f):
    """Decorator to add an option for CLI commands to override BE parameters"""
    return click.option(
        "--backend-param",
        "-b",
        multiple=True,
        help="Override backend parameter of the config file. "
        + "Syntax: `-b <backend>.<parameter>=<value>`.",
    )(f)


def docs_limit_option(f):
    """Decorator to add an option for CLI commands to limit the number of documents to
    use"""
    return click.option(
        "--docs-limit",
        "-d",
        default=None,
        type=click.IntRange(0, None),
        help="Maximum number of documents to use",
    )(f)


def get_project(project_id):
    """
    Helper function to get a project by ID and bail out if it doesn't exist"""
    try:
        return annif.registry.get_project(project_id, min_access=Access.private)
    except ValueError:
        click.echo("No projects found with id '{0}'.".format(project_id), err=True)
        sys.exit(1)


def get_vocab(vocab_id):
    """
    Helper function to get a vocabulary by ID and bail out if it doesn't
    exist"""
    try:
        return annif.registry.get_vocab(vocab_id, min_access=Access.private)
    except ValueError:
        click.echo(f"No vocabularies found with the id '{vocab_id}'.", err=True)
        sys.exit(1)


def open_documents(paths, subject_index, vocab_lang, docs_limit):
    """Helper function to open a document corpus from a list of pathnames,
    each of which is either a TSV file or a directory of TXT files. For
    directories with subjects in TSV files, the given vocabulary language
    will be used to convert subject labels into URIs. The corpus will be
    returned as an instance of DocumentCorpus or LimitingDocumentCorpus."""

    def open_doc_path(path, subject_index):
        """open a single path and return it as a DocumentCorpus"""
        if os.path.isdir(path):
            return annif.corpus.DocumentDirectory(
                path, subject_index, vocab_lang, require_subjects=True
            )
        return annif.corpus.DocumentFile(path, subject_index)

    if len(paths) == 0:
        logger.warning("Reading empty file")
        docs = open_doc_path(os.path.devnull, subject_index)
    elif len(paths) == 1:
        docs = open_doc_path(paths[0], subject_index)
    else:
        corpora = [open_doc_path(path, subject_index) for path in paths]
        docs = annif.corpus.CombinedCorpus(corpora)
    if docs_limit is not None:
        docs = annif.corpus.LimitingDocumentCorpus(docs, docs_limit)
    return docs


def open_text_documents(paths, docs_limit):
    """
    Helper function to read text documents from the given file paths. Returns a
    DocumentList object with Documents having no subjects. If a path is "-", the
    document text is read from standard input. The maximum number of documents to read
    is set by docs_limit parameter.
    """

    def _docs(paths):
        for path in paths:
            if path == "-":
                doc = annif.corpus.Document(text=sys.stdin.read(), subject_set=None)
            else:
                with open(path, errors="replace", encoding="utf-8-sig") as docfile:
                    doc = annif.corpus.Document(text=docfile.read(), subject_set=None)
            yield doc

    return annif.corpus.DocumentList(_docs(paths[:docs_limit]))


def show_hits(hits, project, lang, file=None):
    """
    Print subject suggestions to the console or a file. The suggestions are displayed as
    a table, with one row per hit. Each row contains the URI, label, possible notation,
    and score of the suggestion. The label is given in the specified language.
    """
    for hit in hits:
        subj = project.subjects[hit.subject_id]
        line = "<{}>\t{}\t{}".format(
            subj.uri,
            "\t".join(filter(None, (subj.labels[lang], subj.notation))),
            hit.score,
        )
        click.echo(line, file=file)


def parse_backend_params(backend_param, project):
    """Parse a list of backend parameters given with the --backend-param
    option into a nested dict structure"""
    backend_params = collections.defaultdict(dict)
    for beparam in backend_param:
        backend, param = beparam.split(".", 1)
        key, val = param.split("=", 1)
        _validate_backend_params(backend, beparam, project)
        backend_params[backend][key] = val
    return backend_params


def _validate_backend_params(backend, beparam, project):
    if backend != project.config["backend"]:
        raise ConfigurationException(
            'The backend {} in CLI option "-b {}" not matching the project'
            " backend {}.".format(backend, beparam, project.config["backend"])
        )


def generate_filter_params(filter_batch_max_limit):
    limits = range(1, filter_batch_max_limit + 1)
    thresholds = [i * 0.05 for i in range(20)]
    return list(itertools.product(limits, thresholds))
