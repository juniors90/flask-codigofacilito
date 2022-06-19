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

# config/prod.py
from os.path import abspath, dirname, join
import sys

# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))
FILE_DIR = join(BASE_DIR, __name__)
sys.path.append(FILE_DIR)

import default

APP_ENV = default.APP_ENV_PRODUCTION
