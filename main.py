from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for user data
users = {}

@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user.
    """
    data = request.json
    user_id = data.get('id')
    name = data.get('name')
    email = data.get('email')

    if not user_id or not name or not email:
        return jsonify({"error": "Missing required fields"}), 400

    if user_id in users:
        return jsonify({"error": "User already exists"}), 400

    users[user_id] = {
        "name": name,
        "email": email
    }

    return jsonify({"message": "User created successfully", "user": users[user_id]}), 201

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update an existing user.
    """
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    if name:
        users[user_id]['name'] = name
    if email:
        users[user_id]['email'] = email

    return jsonify({"message": "User updated successfully", "user": users[user_id]}), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get user details.
    """
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[user_id]), 200

@app.route('/users', methods=['GET'])
def get_all_users():
    """
    Get all users.
    """
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)