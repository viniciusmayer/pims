import psycopg2


url = "dbname='pims' user='eleonorvinicius' host='localhost' password='viniciusmayer'"
selectTables = """select table_name from information_schema.tables where table_schema='public' and table_name like 'backend_%'"""
truncate = """truncate {0} cascade"""
files = ('insert_into_tipo.sql', 'insert_into_local.sql', 'insert_into_conta.sql', 'insert_into_ponto.sql')

print "start"
try:
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute(selectTables)
    for row in cursor.fetchall():
        cursor.execute(truncate.format(row[0]))
except Exception, e:
    print e

for _file in files:
    try:
        scriptFile = open(_file, 'r')
        script = scriptFile.read()
        scriptFile.close()
        cursor.execute(script)
        connection.commit()
    except Exception, e:
        print e

connection.close()

print "end"