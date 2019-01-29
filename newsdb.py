import psycopg2

DBNAME = "news"

def top_three_articles():
  """Displays TOP 3 articles sorted by number of views"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("""
  select title, hits from articles, pathHits
  where articles.slug = replace(pathHits.path, '/article/', '') limit 3;
  """)
  result = c.fetchall()
  print("TOP 3 most viewed articles of all time: \n")
  for item in result:
    print("Title: %s - Views: %s" %(item[0],item[1],))
  db.close()