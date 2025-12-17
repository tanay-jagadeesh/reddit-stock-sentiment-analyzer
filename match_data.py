import sqlite3

conn = sqlite3.connect('news.sentiment.db')

c = conn.cursor()

c.execute("SELECT * FROM articles ")
article = c.fetchone()

# The published_at is at index 6
published_at = article[6]
print("Full timestamp:", published_at)

# Extract just the date (first 10 characters)
just_date = published_at[:10]
print("Just the date:", just_date)










conn.commit()

conn.close()