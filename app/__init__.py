#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
# Flask-Codigofacilito Project
#      (https://github.com/juniors90/flask-codigofacilito).
# Copyright (c) 2022, Ferreira Juan David
# License: MIT
# Full Text:
#     https://github.com/juniors90/flask-codigofacilito/blob/master/LICENSE
#
# =============================================================================
# DOCS
# =============================================================================

"""Flask-Codigofacilito

Implementation of in Flask.
"""

# =============================================================================
# IMPORTS
# =============================================================================

from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()


def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    # Load the config file specified by the APP environment variable
    app.config.from_object(settings_module)
    # Load the configuration from the instance folder
    if app.config.get("TESTING", False):
        app.config.from_pyfile("config-testing.py", silent=True)
    else:
        app.config.from_pyfile("config.py", silent=True)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprint Registers
    from app.public import public_bp
    app.register_blueprint(public_bp)
    from app.auth import auth_bp
    app.register_blueprint(auth_bp)
    from app.product import product_bp
    app.register_blueprint(product_bp)
    from app.sale import sale_bp
    app.register_blueprint(sale_bp)


    # Custom error handlers
    register_error_handlers(app)
    return app


def register_error_handlers(app):
    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template("errors/500.html"), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(401)
    def error_404_handler(e):
        return render_template("errors/401.html"), 401
