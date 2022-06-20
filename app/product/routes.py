from flask import render_template, redirect, url_for, request
from flask_login import login_required

from . import product_bp
from app.product.models import Book