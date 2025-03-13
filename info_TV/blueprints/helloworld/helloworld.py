from flask import Blueprint, render_template, redirect


helloworld_bp = Blueprint("helloworld", __name__, template_folder="templates")


@helloworld_bp.route("/")
def index():
    return "hello world"

@helloworld_bp.route("/hello/<nimi>")
def hello_name(nimi):
    return f"hello {nimi}"

@helloworld_bp.route("/hello_html")
def hello_html():
    return render_template("/helloworld/hellohtml.html")