#!/usr/bin/python3
from flask import Flask
from flask_cors import CORS
import router
from config import config
import db

def create_app():
    app = Flask(__name__)

    app.config.from_object(config.Config)
    db.init_db(app)
    db.init_ma(app)

    app.register_blueprint(router.router)

    app.config['JSON_AS_ASCII'] = False
    app.config["JSON_SORT_KEYS"] = False
    CORS(
        app,
        resources = {
            r"/api/*": {"origins": ["http://localhost", "http://localhost:4200"]}
        }
    )
    return app

app = create_app()
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080, threaded=True, use_reloader=False)
