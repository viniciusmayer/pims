from datetime import date
import psycopg2


files = ('insert_into_tipo.sql', 'insert_into_local.sql', 'insert_into_conta.sql', 'insert_into_ponto.sql', 'insert_into_movimento.sql')

selectTables = 'select table_name from information_schema.tables'\
            ' where table_schema=''\'public''\' and table_name like ''\'backend_%''\''
truncate = 'truncate {0} cascade'
def truncateTables(cursor):
    try:
        cursor.execute(selectTables)
        for row in cursor.fetchall():
            cursor.execute(truncate.format(row[0]))
    except Exception as e:
        print(e)

def importFiles(connection, cursor):
    for _file in files:
        try:
            scriptFile = open(_file, 'r')
            script = scriptFile.read()
            scriptFile.close()
            cursor.execute(script)
            connection.commit()
        except Exception as e:
            print(e)
        
insertAnaliseSQL = 'insert into backend_analise(observacoes, ativo, excluido, data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, periodo, "analiseAnterior_id")'\
            ' values (''\'imported''\',true,false,now(),(select id from auth_user'\
            '     where email = ''\'viniciusmayer@gmail.com''\'),now(),(select id from auth_user'\
            '         where email = ''\'viniciusmayer@gmail.com''\'), {0}, null)'
def insertAnalise(connection, cursor):
    try:
        cursor.execute('select distinct periodo from backend_ponto')
        for row in cursor.fetchall():
            split = str(row[0]).split('-')
            cursor.execute(insertAnaliseSQL.format("'{0}'".format(date(int(split[0]), int(split[1]), int(split[2])))))
        connection.commit()
    except Exception as e:
        print(e)

selectMaxPeriodo = 'select max(periodo) from backend_ponto'\
            ' where conta_id = {0} and periodo < (select periodo from backend_ponto'\
            '     where conta_id = {1} and id = {2})'
updatePontoSQL = 'update backend_ponto set "pontoAnterior_id" = (select id from backend_ponto'\
            ' where conta_id = {0} and periodo = (select max(periodo) from backend_ponto'\
            '     where conta_id = {1} and periodo < (select periodo from backend_ponto'\
            '         where conta_id = {2} and id = {3})))'\
            ' where id = {4}'
def updatePonto(connection, cursor):
    try:
        cursor.execute('select id, conta_id from backend_ponto')
        for row in cursor.fetchall():
            _id = row[0]
            conta = row[1]
            cursor.execute(selectMaxPeriodo.format(conta, conta, _id))
            for _row in cursor.fetchall():
                if (not _row[0] is None):
                    cursor.execute(updatePontoSQL.format(conta, conta, conta, _id, _id))
                    connection.commit()
    except Exception as e:
        print(e)

selectMaxPeriodoAnalise = 'select max(periodo) from backend_analise'\
            ' where periodo < (select periodo from backend_analise'\
            '     where id = {0})'
updateAnaliseSQL = 'update backend_analise set "analiseAnterior_id" = (select id from backend_analise'\
            ' where periodo = (select max(periodo) from backend_analise'\
            '     where periodo < (select periodo from backend_analise'\
            '         where id = {0})))'\
            ' where id = {1}'
def updateAnalise(connection, cursor):
    try:
        cursor.execute('select id from backend_analise')
        for row in cursor.fetchall():
            cursor.execute(selectMaxPeriodoAnalise.format(row[0]))
            for _row in cursor.fetchall():
                if (not _row[0] is None):
                    cursor.execute(updateAnaliseSQL.format(row[0], row[0]))
                    connection.commit()
    except Exception as e:
        print(e)

def insertRendimento(connection, cursor):
    try:
        cursor.execute('select id from backend_conta where rendimento = true')
        ids = []
        for row in cursor.fetchall():
            ids.append(row[0])
        scriptFile = open('insert_into_rendimento.sql', 'r')
        count = 0
        for row in scriptFile:
            cursor.execute(row.format(ids[count]))
            count += 1
        scriptFile.close()
        connection.commit()
    except Exception as e:
        print(e)

insertRendimentoPorPeriodoSQL = 'insert into backend_rendimentoporperiodo(observacoes, ativo, excluido, data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, periodo)'\
            ' values (''\'imported''\', true, false, now(), (select id from auth_user'\
            '     where email = ''\'viniciusmayer@gmail.com''\'), now(), (select id from auth_user'\
            '         where email = ''\'viniciusmayer@gmail.com''\'), {0});'
def insertRendimentoPorPeriodo(connection, cursor):
    try:
        cursor.execute('select distinct periodo from backend_ponto')
        for row in cursor.fetchall():
            split = str(row[0]).split('-')
            cursor.execute(insertRendimentoPorPeriodoSQL.format("'{0}'".format(date(int(split[0]), int(split[1]), int(split[2])))))
        connection.commit()
    except Exception as e:
        print(e)

insertAnalisePorPeriodoSQL = 'INSERT INTO backend_analiseporperiodo (observacoes, ativo, excluido, data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, periodo)'\
            ' values (''\'imported''\', true, false, now(), (select id from auth_user'\
            '     where email = ''\'viniciusmayer@gmail.com''\'), now(), (select id from auth_user'\
            '         where email = ''\'viniciusmayer@gmail.com''\'), {0});'
def insertAnalisePorPeriodo(connection, cursor):
    try:
        cursor.execute('select distinct periodo from backend_ponto')
        for row in cursor.fetchall():
            split = str(row[0]).split('-')
            cursor.execute(insertAnalisePorPeriodoSQL.format("'{0}'".format(date(int(split[0]), int(split[1]), int(split[2])))))
        connection.commit()
    except Exception as e:
        print(e)

        
print('start')
try:
    print('connection')
    connection = psycopg2.connect('dbname=''pims'' user=''eleonorvinicius'' host=''localhost'' password=''viniciusmayer''')
    cursor = connection.cursor()
    
    print('truncateTables')
    truncateTables(cursor)
    
    print('importFiles')
    importFiles(connection, cursor)
    
    print('updatePonto')
    updatePonto(connection, cursor)
    
    print('insertAnalise')
    insertAnalise(connection, cursor)
    
    print('updateAnalise')
    updateAnalise(connection, cursor)
    
    print('insertRendimento')
    insertRendimento(connection, cursor)
    
    print('insertRendimentoPorPeriodo')
    insertRendimentoPorPeriodo(connection, cursor)
    
    print('insertAnalisePorPeriodo')
    insertAnalisePorPeriodo(connection, cursor)
except Exception as e:
    print(e)

connection.close()
print('end')
