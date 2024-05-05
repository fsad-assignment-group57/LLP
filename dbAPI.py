from flask_mysqldb import MySQL

import json

# MySQL configuration
mysql = MySQL()


def setMySQLConfig(app):
    with open("config.json", "r") as file:
        data = json.load(file)

    try:
        app.config['MYSQL_HOST'] = data["MYSQL"]["host"]
        app.config['MYSQL_USER'] = data["MYSQL"]["user"]
        app.config['MYSQL_PASSWORD'] = data["MYSQL"]["password"]
        app.config['MYSQL_DB'] = data["MYSQL"]["db"]
        mysql.init_app(app)

        return True
    except Exception as e:
        print("Caught exception while reading the data", e)

        return False
    