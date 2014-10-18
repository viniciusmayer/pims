from datetime import date
import psycopg2


url = "dbname='pims' user='eleonorvinicius' host='localhost' password='viniciusmayer'"
selectTables = """select table_name from information_schema.tables where table_schema='public' and table_name like 'backend_%'"""
truncate = """truncate {0} cascade"""
files = ('insert_into_tipo.sql', 'insert_into_local.sql', 'insert_into_conta.sql', 'insert_into_ponto.sql')
insert = 'INSERT INTO backend_analise(observacoes, ativo, excluido, data_hora_criacao, usuario_criacao_id,'\
            'data_hora_atualizacao, usuario_atualizacao_id, periodo, "periodoAnterior_id")'\
            ' VALUES (''\'imported''\',true,false,now(),(select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'),now(),(select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'),'\
            '{0}, null)'
selectPeriodo = """select distinct periodo from backend_ponto"""

print("start")
try:
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute(selectTables)
    for row in cursor.fetchall():
        cursor.execute(truncate.format(row[0]))
except Exception as e:
    print(e)
    return

for _file in files:
    try:
        scriptFile = open(_file, 'r')
        script = scriptFile.read()
        scriptFile.close()
        cursor.execute(script)
        connection.commit()
    except Exception as e:
        print(e)
        return

try:
    cursor.execute(selectPeriodo)
    for row in cursor.fetchall():
        split = str(row[0]).split('-')
        cursor.execute(insert.format("'{0}'".format(date(int(split[0]), int(split[1]), int(split[2])))))
    connection.commit()
except Exception as e:
    print(e)

connection.close()
print("end")