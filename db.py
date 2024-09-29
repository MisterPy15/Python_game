import sqlite3


def database():
    con = sqlite3.connect("python_game.db")
    cur = con.cursor()
    cur.execute("CREATE User()")