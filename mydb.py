import mysql.connector


database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
    auth_plugin='mysql_native_password'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")  