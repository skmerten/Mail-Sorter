import sqlite3
con = sqlite3.connect("mailSort.db")
cur = con.cursor()
#cur.execute("CREATE TABLE folders(name, directory)")

#data = [
#    ("DMV", "C:\\Users\\skmer\\Desktop\\Mail_Sorter\\Mail-Sorter\\DMV"),
#    ("TEST", "7.5"),
#]
#cur.executemany("INSERT INTO folders VALUES(?, ?)", data)
#on.commit()  # Remember to commit the transaction after executing INSERT.

#res = cur.execute("SELECT * FROM folders")
#print(res.fetchall())