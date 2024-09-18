import psycopg2

try:
    conn = psycopg2.connect(
        dbname="CNMD",
        user="postgres",
        password="2404",
        host="localhost",
        port="5432"
    )
    print("Conexão bem-sucedida!")
    
except Exception as e:
    print(f"Erro ao conectar: {e}")
finally:
    if conn:
        conn.close()
        print("Conexão fechada.")