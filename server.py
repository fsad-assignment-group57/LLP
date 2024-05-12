from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger
from flask_cors import CORS

from dbAPI import setMySQLConfig

app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.1')

# Enable CORS
CORS(app)

# MySQL Configuration
setMySQLConfig(app)

# Import routes
from routes.hello_world import HelloWorld
from routes.square import Square
from routes.userLanguages import userLanguages
from routes.userStreak import userStreak

# Add routes
api.add_resource(HelloWorld, '/')
api.add_resource(Square, '/square')
api.add_resource(userLanguages, '/user-languages/', endpoint='user_languages_post')
api.add_resource(userLanguages, '/user-languages/<string:user_id>',  endpoint='user_languages_get')

api.add_resource(userStreak, '/user-streak/<string:user_id>',  endpoint='user_streak')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
