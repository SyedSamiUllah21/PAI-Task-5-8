from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_joke', methods=['GET'])
def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any")
    joke = response.json()
    if 'joke' in joke:
        return jsonify({"joke": joke['joke']})
    else:
        return jsonify({"joke": f"{joke['setup']} - {joke['delivery']}"})

if __name__ == '__main__':
    app.run(debug=True)
