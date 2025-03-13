from flask import Flask, jsonify, render_template, Response, Blueprint
import requests, os, time, sqlite3


mediaplayer_bp = Blueprint("mediaplayer",__name__)


IMAGE_FOLDER = "static/SAMMAKKO"
# This function loops through the images in the folder one by one.
def stream_images():
    # Images that have already been added to the image loop
    seen_images = set()
    while True:
        # Create a set of images from the SAMMAKKO folder with a certain condition
        images = {f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('png', 'jpg', 'jpeg', 'gif', 'avif', 'webp'))}
        
        # Separate two sets so only new images remain
        new_images = images - seen_images
        # If new images are found, they are sent to the stream function and marked as seen
        if new_images:
            for image in new_images:
                yield f"data: {image}\n\n" 
            seen_images.update(new_images) 
        # Wait 2 seconds before continuing
        time.sleep(2)

@mediaplayer_bp.route('/stream-images')
def stream():
    # Channel to send desired data to the frontend
    return Response(stream_images(), content_type="text/event-stream")