from flask import render_template, redirect, url_for, request
from flask_login import login_required
from app.sale import sale_bp
# from app.sale.models import Sale

@sale_bp.route("/sale", methods=["GET"])
def index_sales():
    return "Hello from sales"