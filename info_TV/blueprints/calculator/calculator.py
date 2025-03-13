from flask import url_for, redirect, Blueprint, render_template

calculator_bp = Blueprint("calculator", __name__)

@calculator_bp.route("/")
def index():
    return "CALCULATOR!!!"

@calculator_bp.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return str(num1 + num2)
