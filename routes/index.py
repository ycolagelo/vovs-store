from flask import Flask, flash, jsonify, redirect, render_template, request, session

from helpers.product_helpers import get_top_products

def make_index_route(app):
    @app.route("/")
    def index():
        top_products = get_top_products(3)

        return render_template("index.html", top_products=top_products)
