#!/usr/bin/env python3

"""
This is the db-connect file.

This file contains all the functions that the tool need.
"""

import psycopg2

DBNAME = "news"


def execute_query(query):
    """
    execute_query returns the results of an SQL query.

    execute_query takes an SQL query as a parameter,
    executes the query and returns the results as a list of tuples.
    args:
    query - an SQL query statement to be executed.

    returns:
    A list of tuples containing the results of the query.
    """
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def top_three_articles():
    """Display TOP 3 articles sorted by number of views."""
    result = execute_query("""
    SELECT title, hits FROM articles, path_hits
    WHERE articles.slug = replace(path_hits.path, '/article/', '') LIMIT 3;
    """)
    print("Top 3 most viewed articles of all time: \n")
    for i, (title, views) in enumerate(result, 1):
        print('{} - Title: {}'.format(i, title))
        print('Views: {}'.format(views))


def top_authors():
    """Display top authors based on the sum of views in their articles."""
    result = execute_query("""
    SELECT authors_table.name, sum(path_hits.hits) AS total
    FROM authors_table, path_hits
    WHERE authors_table.slug = replace(path_hits.path, '/article/', '')
    GROUP BY authors_table.name
    ORDER BY total DESC;
    """)
    print("Top authors based on overall views: \n")
    for i, (name, views) in enumerate(result, 1):
        print('{} - Name: {}'.format(i, name))
        print('Views: {}'.format(views))


def top_failed_requests():
    """Display dates where more than 1% of requests failed."""
    result = execute_query("""
    SELECT * from date_reqs where error_percent > 1;
    """)
    print("Dates where more than 1% of requests failed: \n")
    for i, (date, percent) in enumerate(result, 1):
        print(
            "{} - Date: {} - Failed Requests: {}%".format(
                i,
                date,
                ("{0:.2f}".format(percent)))
        )


def main():
    """Generate Report."""
    print('NEWS REPORT TOOL')
    print('\n')
    top_three_articles()
    print('\n')
    top_authors()
    print('\n')
    top_failed_requests()
    print('\n')


if __name__ == '__main__':
    main()
