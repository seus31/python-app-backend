from flask import make_response, request, jsonify
from model.user import User, UserSchema
from werkzeug.security import generate_password_hash


def get_user_logic():
    users = User.get_user_list()
    user_schema = UserSchema(many=True)
    return make_response(jsonify({
        'code': 200,
        'users': user_schema.dump(users)
    }))


def post_user_logic():
    data = request.json
    username = data.get('user_name')
    email = data.get('email')
    password = data.get('password')
    password_confirm = data.get('password_confirm')
    print(username, email, password, password_confirm)

    if not username or not email or not password or not password_confirm:
        return make_response(
            jsonify({
                'code': 400,
                'error': 'Missing required fields'
            })
        )

    if User.query.filter_by(email=email).first():
        return make_response(
            jsonify({
                'code': 400,
                'error': 'Email already registered'
            })
        )

    hashed_password = generate_password_hash(password)
    new_user = User(name=username, email=email, password=hashed_password).create_user()
    user_schema = UserSchema(many=False)

    return make_response(
        jsonify({
            'code': 201,
            'user': user_schema.dump(new_user)
        })
    )
