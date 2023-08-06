#!/usr/bin/env python3

import logging
import os
import os.path

import connexion
from flask_cors import CORS

from annif.openapi.validation import CustomRequestBodyValidator

logging.basicConfig()
logger = logging.getLogger("annif")
logger.setLevel(level=logging.INFO)

import annif.backend  # noqa


def create_app(config_name=None):
    # 'cxapp' here is the Connexion application that has a normal Flask app
    # as a property (cxapp.app)

    specdir = os.path.join(os.path.dirname(__file__), "openapi")
    cxapp = connexion.App(__name__, specification_dir=specdir)
    if config_name is None:
        config_name = os.environ.get("ANNIF_CONFIG")
    if config_name is None:
        if os.environ.get("FLASK_RUN_FROM_CLI") == "true":
            config_name = "annif.default_config.Config"
        else:
            config_name = "annif.default_config.ProductionConfig"
    logger.debug("creating app with configuration %s", config_name)
    cxapp.app.config.from_object(config_name)
    cxapp.app.config.from_envvar("ANNIF_SETTINGS", silent=True)

    validator_map = {
        "body": CustomRequestBodyValidator,
    }
    cxapp.add_api("annif.yaml", validator_map=validator_map)

    # add CORS support
    CORS(cxapp.app)

    if cxapp.app.config["INITIALIZE_PROJECTS"]:
        annif.registry.initialize_projects(cxapp.app)
        logger.info("finished initializing projects")

    # register the views via blueprints
    from annif.views import bp

    cxapp.app.register_blueprint(bp)

    # return the Flask app
    return cxapp.app
