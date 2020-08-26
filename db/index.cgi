import sqlite3
connection = sqlite3.connect(':memory:')
print "Content-Type: text/html\n"
print "<html><head><title>Books</title></head>"
print "<body>"
print "<h1>Books</h1>"
print "<ul>"

cursor = connection.cursor()
cursor.execute("CREATE TABLE books (name text, pub_date text);")
cursor.execute("INSERT INTO books VALUES ('Django','2013-01-01')")
cursor.execute("SELECT name FROM books ORDER BY pub_date DESC LIMIT 10")

for row in cursor.fetchall():
    print "<li>%s</li>" % row[0]

print "</ul>"
print "</body></html>"

connection.close()
