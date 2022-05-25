import sqlite3
nums = [12,13,14,15]
conn=sqlite3.connect('users.db')
cursor = conn.cursor()
