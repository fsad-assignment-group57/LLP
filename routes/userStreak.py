from flask import request
from flask_restful import Resource
from flask_restful_swagger import swagger

from dbAPI import mysql


class userStreak(Resource):
    def __init__(self):
        self.__DB_table = "user_streak"

    @swagger.operation(
        notes='Update user streak for logging in',
        parameters=[
            {
                "name": "user_id",
                "description": "User ID",
                "required": True,
                "dataType": 'string',
                "paramType": 'path'
            }
        ],
        responseClass=dict,
        nickname='update_streak'
    )
    def post(self, user_id):
        data = request.get_json()
        user_id = data.get('user_id')

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT language FROM user_languages WHERE user_id = %s", (user_id))
        languages = [row[0] for row in cursor.fetchall()]

        cursor.close()

        if not languages:
            return {'error': 'User ID not found'}, 404

        if user_id is None or languages is None:
            return {'error': 'User ID or languages not provided'}, 400
        
        cursor = mysql.connection.cursor()
        try:
            for language in languages:
                cursor.execute(f"""INSERT INTO {self.__DB_table} (user_id, language) 
                    SELECT * FROM (SELECT {user_id}, '{language}') AS temp
                    WHERE NOT EXISTS ( SELECT 1
                    FROM {self.__DB_table}
                    WHERE user_id = {user_id} AND language = '{language}')""")
                
                mysql.connection.commit()

            cursor.close()
            return {'message': 'Registered languages stored successfully'}
        
        except Exception as e:
            cursor.close()
            return {'error': str(e)}, 500
        
    @swagger.operation(
        notes='Fetch registered languages for a user',
        parameters=[
            {
                "name": "user_id",
                "description": "User ID",
                "required": True,
                "dataType": 'string',
                "paramType": 'path'
            }
        ],
        responseClass=dict,
        nickname='fetch_languages'
    )
    def get(self, user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT language FROM user_languages WHERE user_id = %s", (user_id))
        languages = [row[0] for row in cursor.fetchall()]

        cursor.close()

        if not languages:
            return {'error': 'User ID not found'}, 404
        
        return {'user_id': user_id, 'languages': languages}
        
    