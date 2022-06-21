from flask import render_template, redirect, url_for, request
from flask_login import login_required

from app.product import product_bp
from app.product.models import Book

@product_bp.route("/product", methods=["GET"])
def index():
    return "Hello from product"