from flask import Flask, flash, jsonify, redirect, render_template, request, session, abort
from helpers.cart_helpers import add_update_cart, get_full_cart
from helpers.login_required import login_required


def make_cart_route(app):
    @app.route("/cart")
    @login_required
    def cart():
        cart = get_full_cart(session['user_id'])
        print(cart)

        return render_template("cart.html", cart=cart, items=cart['items'])

    # This route is for adding to cart or updating cart count
    # It is meant to be called via ajax
    # It returns json
    @app.route("/cart/add-update", methods=["POST"])
    @login_required
    def add_update_to_cart():
        # If required params not passed, return 400 error
        if not request.json["product_id"]:
            return abort(400, "product_id is required")
        if not request.json["quantity"]:
            return abort(400, "Quantity is required")

        quantity = request.json["quantity"]
        product_id = request.json["product_id"]

        add_update_cart(product_id, quantity, session['user_id'])

        return jsonify(success=True)
