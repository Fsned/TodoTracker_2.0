import sqlite3
from sqlite3 import Error


def initDatabase(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or Nonedatabase
    """

    # Create connection to a file, if it exists.
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    # Create a table for incomes if it doesn't exist
    sql_create_incomePosts_table = """ CREATE TABLE IF NOT EXISTS income_posts (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        post_amount integer, 
                                        monthly_amount integer,
                                        yearly_transactions integer,
                                        added_date text,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_economyPosts_table = """ CREATE TABLE IF NOT EXISTS economyPosts (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        post_amount integer, 
                                        monthly_amount integer,
                                        yearly_transactions integer,
                                        added_date text,
                                        begin_date text,
                                        end_date text
                                    ); """                                       

    create_table(conn, sql_create_economyPosts_table)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def createPost(conn, post):
    """
    Create a new post
    :param conn:
    :param table: income_posts / expense_posts
    :param post:
    :return id:
    POST STRUCTURE:
    name <text>
    postAmount <integer>
    monthlyAmount <integer>
    yearlyTransactions <integer>
    addedDate <text>
    beginDate <text>
    endDate <text>
    """



    sql = ''' INSERT INTO economyPosts (name,post_amount,monthly_amount,yearly_transactions,added_date,begin_date, end_date)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, post)
    conn.commit()

    return cur.lastrowid


def deletePost(conn, postID):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM economyPosts WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, postID)
    conn.commit()


def flushTable(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM economyPosts'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def updatePost(conn, postID, post):



    sql = ''' UPDATE economyPosts
              SET   name=?,
                    post_amount=?,
                    monthly_amount=?,
                    yearly_transactions=?,
                    added_date=?,
                    begin_date=?,
                    end_date=?
              WHERE id = ''' + postID
    cur = conn.cursor()
    cur.execute(sql, post)
    conn.commit()


def fetchSpecificPost(conn, postID):
    sql = ' SELECT * from economyPosts where id=?'
    cur = conn.cursor()
    cur.execute(sql, str(postID))
    result = cur.fetchone()
    conn.commit()

    postDict = {"id": result[0],
                    "postName": result[1],
                    "postAmount": result[2],
                    "monthlyAmount": result[3],
                    "yearlyTransactions": result[4],
                    "addedDate": result[5],
                    "beginDate": result[6],
                    "endDate": result[7]
                    }

    return postDict

def fetchAllPosts(conn):
    sql = ' SELECT * from economyPosts'
    cur = conn.cursor()
    result = cur.execute(sql)
    conn.commit()
    
    resultList = []

    for a in result:
        postDict = {"id": a[0],
                    "postName": a[1],
                    "postAmount": a[2],
                    "monthlyAmount": a[3],
                    "yearlyTransactions": a[4],
                    "addedDate": a[5],
                    "beginDate": a[6],
                    "endDate": a[7]
                    }

        resultList.append(postDict)

    return resultList