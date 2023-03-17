
from flask import Flask, render_template, request,jsonify,session
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)
class DataStore():
    isopen = True
    password = "Mw6uykq4"

data = DataStore()

@app.route("/")
def mrc():
    return render_template("mrc.html", title="MR C")


@app.route("/isopen")
def test():
    if request.method == 'GET':
        message = {'open': data.isopen}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200
@app.route("/admin/<password>")
def admin(password):
    if password == data.password:
        return render_template("admin.html")
    else:
        return render_template("password_error.html")

@app.route("/admin/toggle_open")
def admin_toggle():
    if request.method == 'GET':
        data.isopen = not data.isopen
        message = {'open': data.isopen}
        return jsonify(message)  # serialize and use JSON headers
