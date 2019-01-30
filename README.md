## Backend Developer Nanodegree Program
### Log Analysis

This tool uses Python version 3 to analise the PostgreSQL database of an newspaper site and answer 3 big questions:

* Top 3 most viewed articles
* Most popular authors
* Days where site requests failed more than 1% of the time

###### SAMPLE OUTPUT:

```
NEWS REPORT TOOL

Top 3 most viewed articles of all time:

1 - Title: Candidate is jerk, alleges rival
Views: 338647
2 - Title: Bears love berries, alleges bear
Views: 253801
3 - Title: Bad things gone, say good people
Views: 170098


Top authors based on overall views:

1 - Name: Ursula La Multa
Views: 507594
2 - Name: Rudolf von Treppenwitz
Views: 423457
3 - Name: Anonymous Contributor
Views: 170098
4 - Name: Markoff Chaney
Views: 84557


Dates where more than 1% of requests failed:

1 - Date: 2016-07-17 - Failed Requests: 2.26%

```

### Program Design

The development focus was to leave the hardwork to PostgreSQL, while Python would only organize and format the data, so that the program would run as fast as possible. Joins and Aggregations were used to avoid redundant queries.

### SQL Views

Only 3 views where used to optimize the queries process:

```
CREATE VIEW path_hits AS
    SELECT path, count(*) AS hits FROM log
    WHERE log.status = '200 OK' AND
    path LIKE '%article%'
    GROUP BY path
    ORDER BY hits DESC;

CREATE VIEW authors_table AS
    SELECT articles.slug, authors.name FROM articles, authors 
    WHERE authors.id = articles.author;

CREATE VIEW date_reqs AS
  SELECT time::date AS date,
    100 * (COUNT(*) FILTER (WHERE status = '404 NOT FOUND') /
        COUNT(*)::numeric) AS error_percent
    FROM log
    GROUP BY time::date;
```

### Run this project locally
* First of all, this project assumes you are using Python 3 and an recent version of PostgreSQL.
* To set-up the database you should uncompress the file ``newsdata.sql.zip`` in the same folder.
* After that, open a terminal in the folder, and execute ``psql -d news -f newsdata.sql``.
* Also execute ``psql -d news -f views.sql``to setup the views needed.
* [psycopg2](http://initd.org/psycopg/) is used to easily connect to PostgreSQL, you should install it using ``pip3 install psycopg2``.
* Now you can execute the program using ``python3 newsdb.py``.

###### Reinaldo Trindade - Full Stack Developer