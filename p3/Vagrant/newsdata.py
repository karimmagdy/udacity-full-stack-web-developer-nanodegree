#!/usr/bin/env python3.

import psycopg2
import datetime


def DBconnect(db_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(db_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("There is an error in database connection please try again...")


def executeQuery(query, *kw):
    db, cursor = DBconnect()
    cursor.execute(query, *kw)
    results = [(str(row[0]), round((row[1]), 2))
               for row in cursor.fetchall()]
    db.commit()
    db.close()
    return results


def popArticle():
    """Returning the most popular three articles of all time."""
    query = """
            select articles.title,
            count(*) as views
            from articles
            inner join log on log.path like concat('%', articles.slug, '%')
            where log.status like '%200%'
            group by articles.title, log.path
            order by views
            desc limit 3
            """

    results = executeQuery(query)

    for i in range(len(results)):
        print("   *{0:s} - {1:d} views".format(results[i][0], results[i][1]))
    return results


def popAuthor():
    """Returning The most popular article authors of all time."""
    query = """
            select authors.name,
            count(*) as views
            from articles
            inner join authors on articles.author = authors.id
            inner join log on log.path like concat('%', articles.slug, '%')
            where log.status like '%200%'
            group by authors.name
            order by views desc
            """
    results = executeQuery(query)

    for i in range(len(results)):
        print("   *{0:s} - {1:d} views".format(
            results[i][0], int(results[i][1])))
    return results


def percError():
    """Days with more than 1% of requests that lead to errors"""
    query = """
            SELECT date,
            100.0 * errors/requests as perc_errors
            FROM (
            SELECT time::timestamp::date AS date,
            COUNT(CASE WHEN status
            LIKE '%404 NOT FOUND%' THEN 1 END) AS errors,
            COUNT(method) AS requests
            FROM log
            GROUP BY date
            ORDER BY date
            ) AS error_perc
            WHERE 100.0 * errors/requests > 1
            ORDER BY perc_errors DESC
            """
    results = executeQuery(query)

    for i in range(len(results)):
        date = datetime.datetime.strptime(
            results[i][0], '%Y-%m-%d').strftime("%B %d, %Y")
        print("   *{0:s} - {1:f}% errors".format(date, results[i][1]))
    return results

print("\n\t\tStart")
print("\n The most popular three articles of all time:")
print(" ---------------------------------------------\n")
popArticle()
print("\n The most popular article authors of all time:")
print(" ---------------------------------------------\n")
popAuthor()
print("\n Days with more than 1% of requests that lead to errors:")
print(" -------------------------------------------------------\n")
percError()
print("\n\t\t End")
