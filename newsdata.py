#!/usr/bin/env python2
import psycopg2

# QUESTION FUNCTIONS
# Each question should have its own function containing:
# - a human-readable printable question for the output
# - the SQL query
# - code to beautify the printed output


def question1(cur):
    # QUESTION 1. Who are the most popular article authors of all time?

    print "What are the most popular three articles of all time?\n"

    query = "SELECT DISTINCT title, count(path)"
    query += " FROM articles, log"
    query += " WHERE path LIKE '%' || slug || '%' GROUP BY title "
    query += "ORDER BY count(path) desc LIMIT 3;"

    cur.execute(query)

    i = 1
    for a in cur.fetchall():
        print str(i) + '. ' + a[0]
        i = i + 1

    print ''


def question2(cur):
    # QUESTION 2. Who are the most popular article authors of all time?

    print "Who are the most popular article authors of all time?\n"

    query = "SELECT DISTINCT authors.name, count(path)"
    query += " FROM articles, authors, log"
    query += " WHERE articles.author = authors.id"
    query += " AND path LIKE '%' || slug || '%'"
    query += " GROUP BY authors.name"
    query += " ORDER BY count(path) DESC;"

    cur.execute(query)

    i = 1
    for a in cur.fetchall():
        print str(i) + '. ' + a[0]
        i = i + 1

    print ''


def question3(cur):
    # QUESTION 3. On which days did more than 1% of requests lead to errors?

    print "On which days did more than 1% of requests lead to errors?\n"

    query = "SELECT total.date, total.status_total, error.status_error,"
    query += " error.status_error * 100.0/total.status_total AS error_rate"
    query += " FROM ("
    query += "	(SELECT   time::date as date, count(*) AS status_total "
    query += "	 FROM 	  log"
    query += "	 GROUP BY date) total"
    query += " JOIN"
    query += "	 (SELECT   time::date as date, count(*) AS status_error"
    query += "	  FROM 	   log"
    query += "	  WHERE    status not like '%200%'"
    query += "	  GROUP BY date) error"
    query += " ON error.date = total.date);"

    cur.execute(query)

    i = 1
    for a in cur.fetchall():
        print str(i) + '. ' + str(a[0])
        i = i + 1


if __name__ == "__main__":
    # Connect to database, run selected questions, close database

    conn = psycopg2.connect(dbname='news', user='vagrant')
    cur = conn.cursor()

    question1(cur)
    question2(cur)
    question3(cur)

    cur.close()
    conn.close()
