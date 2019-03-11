#!/usr/bin/env python2.7.14

# loge project

import psycopg2

# q_1. this list shows popular articles:
query_1 = """select articles.title,count(*) as list_1 from articles join log
        on log.path like ('/articles/%'||articles.slug)group by articles.title
        order by list_1 desc LIMIT 3;"""

# q_2. this list shows popular authors:
query_2 = """select author.name, count(*) as views from authors join articles
        on authors.id = articles.author join log
        on log.path like cocant('/articles/%',articles.slug)
        group by authors.name order by views desc limit 4; """
# q_3. On which days did more than 1% of requests lead to errors?
query_3 = """select date (time), round (100.00*sum(CASE WHEN status='404 NOT
        FOUND' THEN 1 else 0 END)/count(log.status),2)as error from log
        group by date (time) order by error desc limit 1"""


def retrive_result(query):
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


def display_result():
    print("The most popular three articles of all time are as follows \n")
    result = retrive_result(query_1)
    for row in result:
        print(str(row[0]) + ' = ' + str(row[1]) + ' views\n')
    print("The most popular article authors of all time are given \n")
    result = retrive_result(query_2)
    for row in result:
        print(str(row[0]) + ' = ' + str(row[1]) + ' views\n')

    print("""The days on which more than 1% of requests lead to errors
    are here \n""")
    result = retrive_result(query_3)
    for row in result:
        print(str(row[0]) + ' = ' + str(row[1]) + '% errors\n')
# Call to output function
display_result()
