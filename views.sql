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