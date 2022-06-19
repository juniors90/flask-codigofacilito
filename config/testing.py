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

# config/testing.py
from os.path import abspath, dirname, join
import sys

# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))
FILE_DIR = join(BASE_DIR, __name__)
sys.path.append(FILE_DIR)

import default

# Parámetros para activar el modo debug
TESTING = True
DEBUG = True

APP_ENV = default.APP_ENV_TESTING

WTF_CSRF_ENABLED = False

SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
