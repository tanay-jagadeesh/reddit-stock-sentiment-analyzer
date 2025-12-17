import sqlite3

conn = sqlite3.connect('news.sentiment.db')
conn2 = sqlite3.connect('stock_value.db')

c = conn.cursor()
c2 = conn2.cursor()

c.execute("SELECT * FROM articles ")
article = c.fetchone()

# The published_at is at index 6
published_at = article[6]
print("Full timestamp:", published_at)

# Extract just the date (first 10 characters)
just_date = published_at[:10]
print("Just the date:", just_date)

c2.execute("SELECT * FROM stock_prices ")
stock_price = c2.fetchone()
just_stock_date = stock_price[1]
print("Stock date: ", just_stock_date)







conn.commit()

conn.close()