from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from helpers.product_helpers import get_products


def make_shop_route(app):
    @app.route("/shop")
    def shop():
        products = get_products()

        return render_template("/shop.html", products=products)
