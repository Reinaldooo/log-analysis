CREATE VIEW path_hits AS
    SELECT path, count(*) AS hits FROM log
    WHERE log.status = '200 OK' AND
    path LIKE '%article%'
    GROUP BY path
    ORDER BY hits DESC;

CREATE VIEW authors_table AS
    SELECT articles.slug, authors.name FROM articles, authors 
    WHERE authors.id = articles.author;

CREATE VIEW req_errors AS
  SELECT time::date AS date, count(*) AS total FROM log
    WHERE status != '200 OK'
    GROUP BY log.time::date
    ORDER BY total Desc;

CREATE VIEW req_total AS
  SELECT time::date AS date, count(*) AS total FROM log
  GROUP BY log.time::date
  ORDER BY total Desc;

CREATE VIEW date_reqs AS
  SELECT req_total.date,
  req_total.total AS req_ok,
  req_errors.total AS req_err,
  round(( req_errors.total::decimal / req_total.total ) * 100) AS percentage
  FROM req_total, req_errors
  WHERE req_total.date = req_errors.date
  ORDER BY req_ok DESC;