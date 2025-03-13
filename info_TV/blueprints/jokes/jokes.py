from flask import Flask, jsonify, render_template, Response, Blueprint
import requests, os, time, sqlite3


jokes_bp = Blueprint("jokes",__name__)

# Database & joke stuff
@jokes_bp.route('/joke', methods=['GET'])
def get_joke():
    
    #Connection to the database
    conn = sqlite3.connect("the.db")
    cursor = conn.cursor()

        
    JOKE_API_URL = "https://official-joke-api.appspot.com/jokes/random/1"
    response = requests.get(JOKE_API_URL)
    if response.status_code == 200:
        json_filu = response.json() # Get the data

        cursor.execute("""
        SELECT setup FROM jokes
                       
        """)

        setups = [row[0] for row in cursor.fetchall()]  

        current_setup = json_filu[0]['setup']
        

        # Not done yet
        if current_setup not in setups:
            cursor.execute("INSERT INTO jokes(setup, punch, type, times_seen) VALUES(?,?,?,?)", (json_filu[0]['setup'], json_filu[0]['punchline'], json_filu[0]['type'], 0))
            conn.commit()
        else:
            pass   


        return jsonify(response.json())  # Convert and return the API response
    else:
        return jsonify({"error": "Failed to fetch joke data"}), response.status_code
