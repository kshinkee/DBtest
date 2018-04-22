# -*- coding: utf-8 -*-

import sqlite3
from contextlib import closing

dbname = 'database.db'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()

    ## Create a table named "users"
    create_table = '''CREATE TABLE IF NOT EXISTS users (id int(10) NOT NULL,
                    name varchar(64) NOT NULL, age int, gender varchar(32), PRIMARY KEY('id'))'''
    c.execute(create_table)

    ## Set values using tuple
    sql = 'INSERT OR IGNORE INTO users (id, name, age, gender) VALUES (?,?,?,?)'
    user = (1, 'Taro', 20, 'male')
    c.execute(sql, user)

    ## Multiple execution og SQLs
    insert_sql = 'INSERT OR IGNORE INTO users (id, name, age, gender) VALUES (?,?,?,?)'
    users = [
        (2, 'Jiro', 16, 'male'),
        (3, 'Saburo', 12, 'female'),
        (4, 'Shiro', 8, 'male'),
        (5, 'Goro', 4, 'male')
    ]
    c.executemany(insert_sql, users)
    conn.commit()

    select_sql = 'SELECT * FROM users'
    for row in c.execute(select_sql):
        print(row)

    del_sql = 'DELETE FROM users WHERE id=?'
    c.execute(del_sql, (2,))

    conn.commit()

    for row in c.execute(select_sql):
        print(row)

    conn.close()
