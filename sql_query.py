import duckdb

con = duckdb.connect(database=':memory:')

con.execute("CREATE TABLE my_table (id INTEGER, name STRING, value FLOAT);")
con.execute("INSERT INTO my_table VALUES (1, 'Test', 100), (2, 'Demo', 200);")

result = con.execute("SELECT * FROM my_table LIMIT 10;").fetchall()
print("Resultat från SQL-frågan:", result)
