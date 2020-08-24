from flask import Flask, flash, jsonify, redirect, render_template, request, session, abort
from helpers.cart_helpers import add_update_cart, get_full_cart
from helpers.login_required import login_required
from db.orders import get_orders_by_user


def make_order_history_route(app):
    @app.route("/order-history")
    @login_required
    def order_history():
        orders = get_orders_by_user(session["user_id"])
        return render_template("order_history.html", orders=orders)
