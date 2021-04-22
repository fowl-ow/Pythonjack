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

    def create_user(self, username):
        con, cur = self.connect()
        # noinspection PyBroadException
        try:
            cur.execute('INSERT INTO users (uname) VALUES (?)', [username])
            con.commit()
        except:
            return False
        return True

    def user_exists(self, username):
        con, cur = self.connect()
        cur.execute('SELECT uname FROM users WHERE uname = ?', [username])
        result = cur.fetchall()
        if len(result) == 0:
            return False
        else:
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
        try:
            return "".join(cur.fetchone())
        except:
            return False

    def get_all(self):
        con, cur = self.connect()
        cur.execute('SELECT * FROM users')
        return cur.fetchall()
