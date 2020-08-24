from functools import wraps
import os
import datetime
import requests
import urllib.parse

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from routes import make_cart_route, make_change_password_route, make_checkout_route, \
    make_index_route, make_login_route, make_register_route, make_product_page_route, \
    make_logout_route, make_order_history_route

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 15
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
# todo ask Pat about this functionality
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

make_index_route(app)
make_login_route(app)
make_register_route(app)
make_logout_route(app)
make_change_password_route(app)
make_product_page_route(app)
make_cart_route(app)
make_checkout_route(app)
make_order_history_route(app)
