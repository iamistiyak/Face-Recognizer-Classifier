from flask import Flask, request, jsonify
import util
import os

os.chdir(r'C:\Users\shaik\OneDrive\Desktop\faceRecognizer\server')


# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)

app = Flask(__name__)

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']# Take the response from the UI

    response = jsonify(util.classify_image(image_data))#Convert it in a json data

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


# @app.route('/')
# def hello_world():
#     return '<h1>Hello, World!</h1>'

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(host="0.0.0.0", port=5000)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)
