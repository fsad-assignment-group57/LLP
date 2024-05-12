from flask import request
from flask_restful import Resource
from flask_restful_swagger import swagger

from dbAPI import mysql


class userLanguages(Resource):
    def __init__(self):
        self.__DB_table = "user_languages"
    
    @swagger.operation(
        notes='Store registered languages for a user',
        parameters=[
            {
                "name": "user_id",
                "description": "User ID",
                "required": True,
                "dataType": 'string',
                "paramType": 'body'
            },
            {
                "name": "languages",
                "description": "List of registered languages",
                "required": True,
                "dataType": 'list',
                "paramType": 'body'
            }
        ],
        responseClass=dict,
        nickname='store_languages'
    )
    def post(self):
        data = request.get_json()
        user_id = data.get('user_id')
        languages = data.get('languages')
        if user_id is None or languages is None:
            return {'error': 'User ID or languages not provided'}, 400
        
        cursor = mysql.connection.cursor()
        try:
            for language in languages:
                # cursor.execute(f"""INSERT INTO {self.__DB_table} (user_id, language) 
                #     SELECT * FROM (SELECT {user_id}, '{language}') AS temp
                #     WHERE NOT EXISTS ( SELECT 1
                #     FROM {self.__DB_table}
                #     WHERE user_id = {user_id} AND language = '{language}')""")
                
                cursor.execute(f"SELECT 1 FROM {self.__DB_table} WHERE user_id = '{user_id}' AND language = '{language}'")
                if cursor.fetchone() is None:
                    cursor.execute(f"""INSERT INTO {self.__DB_table} (user_id, language) VALUES ('{user_id}', '{language}')""")
                
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
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(f"SELECT language FROM {self.__DB_table} WHERE user_id = '{user_id}'")
            languages = [row[0] for row in cursor.fetchall()]

            cursor.close()

            if not languages:
                return {'error': 'User ID not found'}, 404
            
            return {'user_id': user_id, 'languages': languages}
        except Exception as e:
            cursor.close()
            return {'error': str(e)}, 500
        