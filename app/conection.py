import psycopg2

# Configurações de conexão
conn = psycopg2.connect(
    dbname="CNMD",
    user="postgres",
    password="2404",
    host="localhost",
    port="5432"
)

# Cursor para executar comandos SQL
cur = conn.cursor()

# Executar uma consulta
cur.execute("SELECT * FROM users;")
rows = cur.fetchall()
for row in rows:
    print(row)

# Fechar o cursor e a conexão
cur.close()
conn.close()    