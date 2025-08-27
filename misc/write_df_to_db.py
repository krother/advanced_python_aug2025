import duckdb
import seaborn as sns

df = sns.load_dataset("penguins")

con = duckdb.connect()
con.register('penguins', df)
con.execute("COPY penguins TO 'penguins.csv' (FORMAT CSV, HEADER TRUE)")
