from flask import jsonify, make_response, current_app as app
from flask_restful import Resource

class IndexAPI(Resource):
    def get(self):
        return jsonify({
            "status": "200"
        })
