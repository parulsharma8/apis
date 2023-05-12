from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/get-dummy-data/<user>')
def get_data(user):
    print("user is ", user)
    return "Hello"

@app.route("/create-user", methods=["POST"])
def post_user_json():
    req_json = request.json
    print("Request json is")
    print(req_json)

    return "Success"