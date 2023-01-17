import mysql.connector
from mysql.connector import connect

def start():
    global cnx, cur
    cnx = connect(user='root', password='', host='127.0.0.1', database='anomalia')
    cur = cnx.cursor()
    if cnx:
        print('Database connected.')

class BotDB:

    def user_exists(self, user_id):
        """Checking if the user exists in DB"""
        cur.execute("SELECT `telegram_id` FROM `users` WHERE `telegram_id` = %s", (user_id,))
        data = cur.fetchall()
        return bool(len(data))

    def add_info(self, user_id, first_name, last_name, username, user_url):
        """Adding user's info to the DB"""
        cur.execute("INSERT INTO `users` (`telegram_id`, `first_name`, `last_name`, `username`, `user_url`, `language`) VALUES (%s, %s, %s, %s, %s, %s)", (user_id, first_name, last_name, username, user_url, "en"))
        cnx.commit()

    def update_info(self, first_name, last_name, username, user_url, user_id):
        """Updating user's info in the DB"""
        cur.execute("UPDATE `users` SET `first_name` = %s, `last_name` = %s, `username` = %s, `user_url` = %s WHERE `telegram_id` = %s", (first_name, last_name, username, user_url, user_id))
        cnx.commit()

    def update_user_language_db(self, selected_language, user_id):
        cur.execute("UPDATE `users` SET `language` = %s WHERE `telegram_id` = %s", (selected_language, user_id))
        cnx.commit()

    def get_user_language(self, user_id):
        cur.execute("SELECT `language` FROM `users` WHERE `telegram_id` = %s", (user_id,))
        data = cur.fetchone()
        return data[0] if data else None

    def close(self):
        """Closing connection with DB"""
        cur.close()
        cnx.close()

