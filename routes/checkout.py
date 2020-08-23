from helpers.login_required import login_required
from flask import Flask, flash, jsonify, redirect, render_template, request, session, abort
from helpers.checkout_helpers import place_order


def make_checkout_route(app):
    @app.route("/checkout", methods=["GET", "POST"])
    @login_required
    def checkout():
        if request.method == "POST":
            # if not request.form.get("firstName"):
            #     return("Please provide firstname")
            # if not request.form.get("lastName"):
            #     return("Please provide last Name")
            # firstName = request.form.get("firstName")
            # lastName = request.form.get("lastName")
            # if not request.form.get("address1"):
            #     return("Please provide an address")
            # if not request.form.get("province"):
            #     return("Please provide a province")
            # if not request.form.get("postalCode"):
            #     return("Please insert a valid postal code")
            # if not request.form.get("city"):
            #     return("Please insert a valid city")
            # address1 = request.form.get("address1")
            # address2 = request.form.get("address2")
            # province = request.form.get("province")
            # postalcode = request.form.get("postalCode")
            # city = request.form.get("city")

            payment_info = {}  # todo
            place_order(user_id=session["user_id"], payment_info=payment_info)
            return redirect("/")

        # redirect to home page (or ideally make an order confirmation page)

        else:
            return render_template("checkout.html")
