import psycopg2

DBNAME = "news"


def top_three_articles():
  """Displays TOP 3 articles sorted by number of views"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("""
  SELECT title, hits FROM articles, path_hits
  WHERE articles.slug = replace(path_hits.path, '/article/', '') LIMIT 3;
  """)
  result = c.fetchall()
  list_item = 1
  print("Top 3 most viewed articles of all time: \n")
  for item in result:
    print("%s - Title: %s" % (list_item, item[0], ))
    print("Views: %s" % (item[1], ))
    list_item += 1
  db.close()


def top_authors():
  """Displays top authors based on the sum of views in their articles"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("""
  SELECT authors_table.name, sum(path_hits.hits) AS total
  FROM authors_table, path_hits
  WHERE authors_table.slug = replace(path_hits.path, '/article/', '')
  GROUP BY authors_table.name
  ORDER BY total DESC;
  """)
  result = c.fetchall()
  list_item = 1
  print("Top authors based on overall views: \n")
  for item in result:
    print("%s - Name: %s - Views: %s" % (list_item, item[0], item[1], ))
    list_item += 1
  db.close()


def top_failed_requests():
  """Displays dates where more than 1% of requests failed"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("""
  SELECT date, percentage from date_reqs where percentage > 1;
  """)
  result = c.fetchall()
  list_item = 1
  print("Dates where more than 1% of requests failed: \n")
  for item in result:
    print("%s - Date: %s - Failed Percentage: %s" % (
      list_item,
      item[0],
      item[1],
    ))
    list_item += 1
  db.close()
