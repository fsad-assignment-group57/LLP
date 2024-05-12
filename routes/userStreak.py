from flask import request
from flask_restful import Resource
from flask_restful_swagger import swagger
from datetime import datetime, timedelta

from dbAPI import mysql


class userStreak(Resource):
    def __init__(self):
        self.__DB_table = "user_streak"

    @swagger.operation(
        notes='Update user streak',
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
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(f"SELECT streak, update_time FROM {self.__DB_table} WHERE user_id = '{user_id}'")

            result = cursor.fetchone()
            if result:
                latest_streak, latest_update_time = result
            else:
                latest_streak, latest_update_time = 0, None
            
            current_time = datetime.now()
            message = ''

            if latest_update_time:
                day_before_yesterday_end = datetime.now().replace(hour=23, minute=59, second=59, microsecond=59) - timedelta(days=2)

                # Check if the update_time is anytime of yesterday
                if latest_update_time.date() == (current_time - timedelta(days=1)).date():
                    latest_streak += 1
                    print(f"User {user_id}'s streak has been updated. Current streak: {latest_streak}")
                    message = f"User {user_id}'s streak has been updated. Current streak: {latest_streak}"

                    cursor.execute(f"UPDATE {self.__DB_table} SET streak = {latest_streak}, update_time = '{current_time.strftime('%Y-%m-%d %H:%M:%S')}' WHERE user_id = '{user_id}'")
                elif latest_update_time < day_before_yesterday_end:
                    latest_streak = 1
                    print(f"User {user_id}'s streak has been reset for a new day.")
                    message = f"User {user_id}'s streak has been reset for a new day"
                
                    cursor.execute(f"UPDATE {self.__DB_table} SET streak = {latest_streak}, update_time = '{current_time.strftime('%Y-%m-%d %H:%M:%S')}' WHERE user_id = '{user_id}'")
                else:
                    print(f"User {user_id} has updated their streak recently.")
                    message = f"User {user_id} has updated their streak recently"

            else:
                # No previous update found, start a new streak
                latest_streak = 1
                print(f"Starting a new streak for user {user_id}.")
                message = f"User {user_id}'s streak has been reset for a new day"

                cursor.execute(f"INSERT INTO {self.__DB_table} (user_id, streak, update_time) VALUES ('{user_id}', {latest_streak}, '{current_time.strftime('%Y-%m-%d %H:%M:%S')}')")
            
            mysql.connection.commit()
            cursor.close()
            return {'message': message}
        except Exception as e:
            cursor.close()
            return {'error': str(e)}, 500
        
    @swagger.operation(
        notes='Fetch user',
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
        nickname='fetch_streak'
    )
    def get(self, user_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(f"SELECT streak FROM {self.__DB_table} WHERE user_id = '{user_id}'")
            streak = cursor.fetchone()

            cursor.close()

            if not streak:
                return {'error': 'User ID not found'}, 404
            
            return {'user_id': user_id, 'streak': int(streak[0])}
        except Exception as e:
            cursor.close()
            return {'error': str(e)}, 500
