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

from flask import Blueprint

public_bp = Blueprint("public", __name__, template_folder="templates")

from app.public import routes
