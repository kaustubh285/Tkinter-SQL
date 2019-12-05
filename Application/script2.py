import sqlite3
def create():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS kingdom(k_name TEXT, k_Age INTEGER ,influence REAL) ")
    conn.commit()
    conn.close()

def insert(name,age,influ):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO kingdom VALUES(?,?,?)",(name,age,influ))
    conn.commit()
    conn.close()

def display():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM kingdom")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM kingdom WHERE k_name=?",(item,))
    conn.commit()
    conn.close()

def update(item1,item2):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("UPDATE kingdom  SET influence=? WHERE k_name=?",(item2,item1,))
    conn.commit()
    conn.close()


create()

kname=input("Enter name of the king:")
kage=input("Enter age:")
kinfluence=input("Enter the influence percentage:")

insert(kname,kage,kinfluence)
print(display())

#delete("Jon Snow")
update('Kaustubh',99.01)

print(display())
