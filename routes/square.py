from flask import request
from flask_restful import Resource, reqparse
from flask_restful_swagger import swagger

class Square(Resource):
    @swagger.operation(
        notes='Calculate square of a number',
        parameters=[
            {
                "name": "number",
                "description": "Input number",
                "required": True,
                "dataType": 'integer',
                "paramType": 'query'
            }
        ],
        responseClass=dict,
        nickname='get_square'
    )
    def get(self):
        number = request.args.get('number')
        if number is None:
            return {'error': 'Number not provided'}, 400
        try:
            number = int(number)
        except ValueError:
            return {'error': 'Number must be an integer'}, 400
        return {'square': number ** 2}

    @swagger.operation(
        notes='Calculate square of a number',
        parameters=[
            {
                "name": "number",
                "description": "Input number",
                "required": True,
                "dataType": 'integer',
                "paramType": 'body'
            }
        ],
        responseClass=dict,
        nickname='post_square'
    )
    def post(self):
        data = request.get_json()
        number = data.get('number')
        if number is None:
            return {'error': 'Number not provided'}, 400
        try:
            number = int(number)
        except ValueError:
            return {'error': 'Number must be an integer'}, 400
        return {'square': number ** 2}
