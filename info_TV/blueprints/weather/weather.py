from flask import Flask, jsonify, render_template, Response, Blueprint
import requests, os, time, sqlite3


weather_bp = Blueprint("weather",__name__)

@weather_bp.route('/weather', methods=['GET'])
def get_weather():
    WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast?latitude=65.01962&longitude=25.486084&hourly=temperature_2m&daily=uv_index_max&timezone=auto&forecast_days=1"

    response = requests.get(WEATHER_API_URL)

    if response.status_code == 200:
        return jsonify(response.json())  # Convert and return the API response
    else:
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code

