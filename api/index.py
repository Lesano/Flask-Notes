from flask import Flask, render_template, jsonify, request, redirect, url_for
from os import path
import json

app = Flask(__name__)
@app.route("/")
def home():
    site_root = path.dirname(__file__)
    json_url = path.join(site_root, 'notes.json')
    try:
        data = json.load(open(json_url))
    except:
        data = {"notes": []}
    note_count = len(data.get("notes", []))
    print(note_count)
    return render_template("index.html", data=data, note_count=note_count)

@app.route("/xp")
def xphome():
    site_root = path.dirname(__file__)
    json_url = path.join(site_root, 'notes.json')
    try:
        data = json.load(open(json_url))
    except:
        data = {"notes": []}
    note_count = len(data.get("notes", []))
    print(note_count)
    return render_template("xpindex.html", data=data, note_count=note_count)

@app.route("/add_note", methods=['POST'])
def add_note():
    site_root = path.dirname(__file__)
    json_url = path.join(site_root, 'notes.json')
    author = request.form['author']
    note = request.form['text']
    note_title = request.form['note']
    new_note = {
        'title': note_title,
        'author': author,
        'note': note
    }
    try:
        with open(json_url, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"notes": []}

    data['notes'].append(new_note)
    with open(json_url, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    return redirect(url_for("home"))
app.run(host="0.0.0.0", port="8080", debug=True)
