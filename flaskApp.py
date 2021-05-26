from flask import Flask, json, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'name': 'Mom',
        'contact': '1483290595',
        'called': False
    },
    {
        'id': 2,
        'name': 'Dad',
        'contact': '3046803946',
        'called': False
    }
]

@app.route("/add-data", methods = ["POST"])

def add_contact():
    if not request.json:
        return jsonify({
            "status": "Error",
            "message": "Provide the data of the contact."
        },
        400)
    
    contact = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'called': False
    }

    contacts.append(contact)
    return jsonify({
            "status": "Success",
            "message": "The contact was added successfully!"
        })

@app.route("/get-data")

def get_task():
    return jsonify({ "data" : contacts })

if(__name__ == "__main__"):
    app.run(debug = True)

#data provided by me in flask by POST method and add data route
"""{
    "id": 3,
    "name": "Friend",
    "contact": "2074632179",
    "called": true
}"""
#data returned by flask using GET method and get data route
"""{
    "data": [
        {
            "called": false,
            "contact": "1483290595",
            "id": 1,
            "name": "Mom"
        },
        {
            "called": false,
            "contact": "3046803946",
            "id": 2,
            "name": "Dad"
        },
        {
            "called": false,
            "contact": "2074632179",
            "id": 3,
            "name": "Friend"
        }
    ]
}"""