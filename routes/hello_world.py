from flask_restful import Resource
from flask_restful_swagger import swagger

class HelloWorld(Resource):
    @swagger.operation(
        notes='Get hello message',
        responseClass=dict,
        nickname='get_hello'
    )
    def get(self):
        return {'message': 'Hello, world!'}
