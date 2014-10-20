from datetime import date
import psycopg2


files = ('insert_into_tipo.sql', 'insert_into_local.sql', 'insert_into_conta.sql', 'insert_into_ponto.sql')


selectTables = 'select table_name from information_schema.tables where table_schema=''public'' and table_name like ''backend_%'''
truncate = 'truncate {0} cascade'
def truncateTables(cursor):
    try:
        cursor.execute(selectTables)
        for row in cursor.fetchall():
            cursor.execute(truncate.format(row[0]))
        return True
    except Exception as e:
        print(e)
        return False

def importFiles(connection, cursor):
    for _file in files:
        try:
            scriptFile = open(_file, 'r')
            script = scriptFile.read()
            scriptFile.close()
            cursor.execute(script)
            connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
selectPeriodo = 'select distinct periodo from backend_ponto'
insertIntoAnalise = 'insert into backend_analise(observacoes, ativo, excluido, data_hora_criacao, usuario_criacao_id,'\
            ' data_hora_atualizacao, usuario_atualizacao_id, periodo, "periodoAnterior_id")'\
            ' values (''\'imported''\',true,false,now(),(select id from auth_user where'\
            ' email = ''\'viniciusmayer@gmail.com''\'),now(),(select id from auth_user where'\
            ' email = ''\'viniciusmayer@gmail.com''\'), {0}, null)'
def insertIntoAnalise(connection, cursor):
    try:
        cursor.execute(selectPeriodo)
        for row in cursor.fetchall():
            split = str(row[0]).split('-')
            cursor.execute(insertIntoAnalise.format("'{0}'".format(date(int(split[0]), int(split[1]), int(split[2])))))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

selectMaxPeriodo = 'select max(periodo) from backend_ponto where conta_id = {0}'\
            ' and periodo < (select periodo from backend_ponto where conta_id = {1} and id = {2})'
updatePeriodoAnterior = 'update backend_ponto set ''\"periodoAnterior_id''\" = ('\
            'select id from backend_ponto where conta_id = {0}'\
            '    and periodo = (select max(periodo) from backend_ponto where conta_id = {1}'\
            '        and periodo < (select periodo from backend_ponto where conta_id = {2} and id = {3})))'\
            'where id = {4}'
def updatePonto(connection, cursor):
    try:
        cursor.execute('select id, conta_id from backend_ponto')
        for row in cursor.fetchall():
            _id = row[0]
            conta = row[1]
            cursor.execute(selectMaxPeriodo.format(conta, conta, _id))
            for _row in cursor.fetchall():
                cursor.execute(updatePeriodoAnterior.format(conta, conta, conta, _id, _id))
                connection.commit()
    except Exception as e:
        print(e)

#FIXME develop
def updateAnalise(connection, cursor):
    pass

print("start")
url = 'dbname=''pims'' user=''eleonorvinicius'' host=''localhost'' password=''viniciusmayer'''
try:
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
except Exception as e:
    print(e)

truncateTables(cursor)
importFiles(connection, cursor)
updatePonto(connection, cursor)
insertIntoAnalise(connection, cursor)
updateAnalise(connection, cursor)

connection.close()
print("end")