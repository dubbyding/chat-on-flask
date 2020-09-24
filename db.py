import psycopg2

conn = psycopg2.connect("dbname='chat' user='dubbyding' password='@NepsGGMU44' host='localhost'")

cur = conn.cursor()