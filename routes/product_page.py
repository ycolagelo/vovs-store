from flask import Flask, flash, jsonify, redirect, render_template, request, session
from helpers.product_helpers import get_product, get_product_images

def make_product_page_route(app):
    @app.route("/product/<int:product_id>")
    def product_page(product_id):
        product = get_product(product_id)
        images = get_product_images(product_id)

        if product is None:
            # TODO: Error page
            return "Product Not Found"

        return render_template("product_page.html", product=product, images=images)
