from flask import Flask, flash, jsonify, redirect, render_template, request, session


def make_index_route(app):
    @app.route("/")
    def index():
        return render_template("index.html")
