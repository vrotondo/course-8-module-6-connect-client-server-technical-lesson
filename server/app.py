from flask import Flask, jsonify, send_from_directory
# Import any helper functions you create in store.py

app = Flask(__name__, static_folder='../client', static_url_path='')

# TASK: Define a route for "/"
# This should return index.html from the static folder


# TASK: Define a route for "/api/data"
# This should return a JSON object with a message and status
# Hint: You can use a function from store.py to generate the response


if __name__ == '__main__':
    app.run(debug=True)
