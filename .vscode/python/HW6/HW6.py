import sqlite3 as sql
import json

with open("HW6_1.json") as f:
    data = json.load(f)

print(data)

con=sql.connect("project.db")
cur=con.cursor()
try:
    cur.execute("""CREATE TABLE member(
                full_name CHAR(255),
                nationality CHAR(255),
                born DATA,
                id INT,
                city CHAR(255),
                gender CHAR(255));""")
except:
    pass

cur.execute(f"INSERT INTO member(full_name,nationality,born,id,city,gender) VALUES('{data['member']['full_name']}','{data['member']['nationality']}','{data['member']['born']}',{data['member']['id']},'{data['member']['city']}','{data['member']['gender']}')")
con.commit()
con.close()
