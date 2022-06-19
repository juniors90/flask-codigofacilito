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

from flask import render_template
from . import public_bp


@public_bp.route("/")
def index():
    return render_template("public/index.html")