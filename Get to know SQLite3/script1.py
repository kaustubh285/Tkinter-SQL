import psycopg2
def create():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='kaust1459' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS kingdom(k_name TEXT, k_Age INTEGER ,influence REAL) ")
    conn.commit()
    conn.close()

def insert():
    kname=input("Enter name of the king:")
    kage=input("Enter age:")
    kinfluence=input("Enter the influence percentage:")
    conn=psycopg2.connect("dbname='database1' user='postgres' password='kaust1459' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO kingdom VALUES(%s,%s,%s)",(kname,kage,kinfluence))
    conn.commit()
    conn.close()

def display():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='kaust1459' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM kingdom")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='kaust1459' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM kingdom WHERE k_name=%s",(item,))
    conn.commit()
    conn.close()

def update(item1,item2):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='kaust1459' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE kingdom  SET influence=%s WHERE k_name=%s",(item2,item1,))
    conn.commit()
    conn.close()


create()



insert()
#print(display())

#delete("Jon Snow")
#update('Kaustubh',99.01)

print(display())
