#!/usr/bin/env python2
import psycopg2

# QUESTION FUNCTIONS
# Each question should have its own function containing:
# - a human-readable printable question for the output
# - the SQL query
# - code to beautify the printed output


def question1(cur):
    # QUESTION 1. Who are the most popular article authors of all time?

    print "The most popular three articles of all time:\n"

    query = "SELECT title, count(slug)"
    query += " FROM log, articles"
    query += " WHERE path LIKE '%' || slug GROUP BY title "
    query += "ORDER BY count desc LIMIT 3;"

    cur.execute(query)

    i = 1
    for a in cur.fetchall():
        print '\t' + str(i) + '. ' + a[0] + ' -- ' + str(a[1]) + ' views'
        i = i + 1
    print ''


def question2(cur):
    # QUESTION 2. Who are the most popular article authors of all time?

    print "Most popular article authors of all time:\n"

    query = "SELECT artview.name, sum(artview.count)"
    query += " FROM ("
    query += "       SELECT title, author, name, count(slug)"
    query += "       FROM log, articles, authors"
    query += "       WHERE path LIKE '%'||slug"
    query += "          AND authors.id = articles.author"
    query += "       GROUP BY title, name, author"
    query += "       ORDER BY count DESC) as artview"
    query += " GROUP BY artview.name"
    query += " ORDER BY sum DESC"
    query += " LIMIT 3;"

    cur.execute(query)

    i = 1
    for a in cur.fetchall():
        print '\t' + str(i) + '. ' + a[0] + ' (' + str(a[1]) + ' views)'
        i = i + 1
    print ''


def question3(cur):
    # QUESTION 3. On which days did more than 1% of requests lead to errors?

    print "Days on which more than 1% of requests led to errors:\n"

    query = "SELECT requests.date,"
    query += "       ROUND(errors.total*100.0/requests.total,1) AS error_rate"
    query += " FROM"

    query += " (SELECT DISTINCT time::date AS date,"
    query += " 	               count(status) AS total "
    query += " FROM log "
    query += " GROUP BY date "
    query += " ORDER BY date) as requests"

    query += " INNER JOIN "

    query += " (SELECT DISTINCT time::date AS date,"
    query += " 	                count(status) AS total"
    query += " FROM log "
    query += " WHERE status LIKE '404%' "
    query += " GROUP BY date, status"
    query += " ORDER BY date) as errors"

    query += " ON requests.date = errors.date"

    query += " WHERE ROUND(errors.total*100.0/requests.total,1) > 1.0"
    query += " ORDER BY requests.date;"

    cur.execute(query)

    for a in cur.fetchall():
        print '\t' + str(a[0]) + ' (' + str(a[1]) + '%)'
    print ''


if __name__ == "__main__":
    # Connect to database, run selected questions, close database

    conn = psycopg2.connect(dbname='news', user='vagrant')
    cur = conn.cursor()

    question1(cur)
    question2(cur)
    question3(cur)

    cur.close()
    conn.close()
