# put and delete HTTP verbs
# workign with API's -> Json

from flask import Flask, jsonify, request

app = Flask(__name__)

# intial data in to do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

# home page -> by default get method
@app.route('/')
def home():
    return "Welcome to the sample TO DO List app"

# get method -> retrived all the itemsa
@app.route('/items')
def get_items():
    return jsonify(items)

# get -> retrive a specific item by id
@app.route('/item/<int:item_id>')
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

# post -> create a new item
# test with postman
@app.route('/item', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "invalid request"})


    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "description": request.json["description"]
    }

    items.append(new_item)
    return jsonify(new_item)

# put -> udpate an existing item
@app.route('/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    # retrive the item
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": f"Item with item id - {item_id} not found"})

    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# delete -> delete an existing item
@app.route('/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    
    # retrive the item
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": f"Item with item id - {item_id} not found"})

    # remove the item
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item Delted!"})

if __name__ == "__main__":
    app.run(debug=True)
