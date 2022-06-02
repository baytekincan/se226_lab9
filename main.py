import mysql.connector

def create_Schema():
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Baytekincan13."
    )
    CURSOR = dataBase.cursor()
    CURSOR.execute("DROP DATABASE IF EXISTS LAB")
    sql = '''CREATE DATABASE LAB'''
    CURSOR.execute(sql)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Baytekincan13.",
        database="LAB"
    )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version", db_Info)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)


def create_Table():
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Baytekincan13.",
        database="LAB"
    )
    CURSOR = dataBase.cursor()
    CURSOR.execute("DROP TABLE IF EXISTS Marvel")
    mysql_Create_Table = '''CREATE TABLE Marvel(
                  ID INT,
                  MOVIE VARCHAR(100),
                  DATE VARCHAR(100),
                  MCU_PHASE VARCHAR(100)
                )'''
    CURSOR.execute( mysql_Create_Table)


def insert(address):
    path = open("C:\Users\user\Desktop\Projects\pyProjects\ 226lab9\Marvel.txt")
    try:
        dataBase = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Baytekincan13.",
            database="LAB"
        )
        CURSOR = dataBase.cursor()
        while path:
            marvel = path.readline()
            if marvel == "":
                break
            splitLines = marvel.split()
            mysql_ınsert_table = """INSERT INTO Marvel(ID,MOVIE,DATE,MCU_PHASE) VALUES (%s,%s,%s,%s)"""
            record = (splitLines[0], splitLines[1], splitLines[2], splitLines[3])
            CURSOR.execute(mysql_ınsert_table, record)
            dataBase.commit()

    except mysql.connector.Error as error:
        print("Failed to insert into MySql Table {}".format(error))
    finally:
        if dataBase.is_connected():
            CURSOR.close()
            dataBase.close()
            print("MYSQL connection is closed")


def print_all_movies():
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Baytekincan13.",
        database="LAB"
    )
    CURSOR = dataBase.cursor()
    query = "SELECT * FROM Marvel"
    CURSOR.execute(query)
    rows = CURSOR.fetchall()
    for row in rows:
        print(row)

    dataBase.close()


def delete_from_table(name):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Baytekincan13.",
        database="LAB"
    )
    CURSOR = dataBase.cursor()
    q = "DELETE FROM Marvel WHERE MOVIE = %s"
    data = (name,)
    CURSOR.execute(q, data)
    dataBase.commit()
    dataBase.close()


def phase_2():
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Baytekincan13.",
        database="LAB"
    )
    CURSOR = dataBase.cursor()
    query = "SELECT * FROM Marvel WHERE MCU_PHASE = 'Phase2'"
    CURSOR.execute(query)
    rows = CURSOR.fetchall()
    for row in rows:
        print(row)

    dataBase.close()


def fix_Thor():
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Baytekincan13.",
        database="LAB"
    )
    CURSOR = dataBase.cursor()
    query = "UPDATE Marvel SET DATE = 'November3,2017' WHERE MOVIE = 'Thor:Ragnarok'"
    CURSOR.execute(query)
    dataBase.commit()
    dataBase.close()


def main():
    create_Schema()
    create_Table()
    insert("C:\Users\user\Desktop\Projects\pyProjects\ 226lab9\Marvel.txt")
    print("ALL MOVIES ")
    print_all_movies()
    delete_from_table('TheIncredibleHulk')
    print("ALL MOVIES AFTER DELETE PROCESS")
    print_all_movies()
    print("PHASE 2 MOVIES")
    phase_2()
    fix_Thor()
    print("AFTER THOR HAS BEEN FIXED")
    print_all_movies()


if __name__ == '__main__':
    main()