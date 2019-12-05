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

ply=True
create()
while(ply==True):
    print("Here is the current kingdom log-")
    print("---------------------------------")
    names=display()
    for name in names:
        print(name)
    print("---------------------------------")
    print("Press 1 to add new King \nPress 2 to update influence of a previous king \nPress 3 to delete data of a previous King \nPress 4 Exit")
    choice=input()
    if choice=="1":
        insert()
    elif choice=="2":
        k=input("Enter name of the King")
        infl=input("Enter the influence of the king")
        update(k,infl)
    elif choice=="3":
        k=input("Enter name of the king you wish to remove from the log")
        delete(k)
    elif choice=="4":
        ply=False
    else:
        print("ENTER A VALID NUMBER DAMMIT!!!!")
