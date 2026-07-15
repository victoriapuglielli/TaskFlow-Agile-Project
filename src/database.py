import sqlite3

DATABASE = "taskflow.db"


def conectar():
    return sqlite3.connect(DATABASE)