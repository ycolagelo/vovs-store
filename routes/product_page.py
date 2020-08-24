from flask import Flask, flash, jsonify, redirect, render_template, request, session
from helpers.product_helpers import get_product, get_product_images
from helpers.cart_helpers import get_cart, get_cart_count
from helpers.login_required import login_required

# @login_required


def make_product_page_route(app):
    @app.route("/product/<int:product_id>")
    def product_page(product_id):
        product = get_product(product_id)
        images = get_product_images(product_id)
        cart_count = 0

        logged_in = False
        if "user_id" in session:
            logged_in = True
            cart = get_cart(session['user_id'])
            cart_count = get_cart_count(cart['id'], product_id)
        if cart_count == 0:
            cart_count = 1

        if product is None:
            # TODO: Error page
            return "Product Not Found"

        return render_template("product_page.html", product=product,
                               images=images, cart_count=cart_count, logged_in=logged_in)
