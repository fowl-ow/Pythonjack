import sqlite3


class Database:

    def connect(self):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        return con, cur

    def __init__(self):
        con, cur = self.connect()
        cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    uid INTEGER NOT NULL PRIMARY KEY,
                    uname TEXT UNIQUE,
                    passwd TEXT
                    );''')

    def create_user(self, username, just_check_if_exists=False):
        con, cur = self.connect()
        try:
            cur.execute('INSERT INTO users (uname) VALUES (?)', [username])
            con.commit()
        except:
            return False
        if just_check_if_exists:
            self.delete_user(username)
        return True

    def delete_user(self, username):
        con, cur = self.connect()
        cur.execute('DELETE FROM users WHERE uname = ?', [username])
        con.commit()

    def set_passwd(self, username, passwd):
        con, cur = self.connect()
        query = 'UPDATE users SET passwd = "{}" WHERE uname = "{}"'.format(passwd, username)
        cur.execute(query)
        con.commit()

    def get_user_info(self, username):
        con, cur = self.connect()
        cur.execute('SELECT * FROM users WHERE uname = ?', [username])
        return cur.fetchone()

    def get_user_passwd(self, username):
        con, cur = self.connect()
        cur.execute('SELECT passwd FROM users WHERE uname = ?', [username])
        return cur.fetchone()

    def get_all(self):
        con, cur = self.connect()
        cur.execute('SELECT * FROM users')
        return cur.fetchall()


















