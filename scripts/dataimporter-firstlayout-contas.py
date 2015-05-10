import csv
from datetime import date
import psycopg2


selectUsuario = '(select id from auth_user where email = ''\'viniciusmayer@gmail.com''\')'
selectTipo = '(select id from backend_tipo where nome = ''\'{0}''\')'
selectLocal = '(select id from backend_local where nome = ''\'{0}''\')'
selectConta = '(select id from backend_conta where local_id = {0} and tipo_id = {1} and nome = ''\'{2}''\')'

insertIntoTipo = 'INSERT INTO backend_tipo(nome, observacoes, ativo, excluido,'\
                        'data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, categoria)'\
                 ' VALUES (''\'{0}''\', ''\'imported''\', true, false, now(), {1}, now(), {1}, ''\'CO''\');'

insertIntoLocal = 'INSERT INTO backend_local(nome, observacoes, ativo, excluido,'\
                        'data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, tipo_id)'\
                  ' VALUES (''\'{0}''\', ''\'imported''\', true, false, now(), {1}, now(), {1}, {2});'
               
insertIntoConta = 'INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,'\
                        'data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id)'\
                  ' VALUES (''\'{0}''\', ''\'imported''\', true, false, false, now(), {1}, now(), {1}, {2}, {3});'
                 
insertIntoPonto = 'INSERT INTO backend_ponto(observacoes,ativo,excluido,data_hora_criacao,usuario_criacao_id,data_hora_atualizacao,usuario_atualizacao_id,'\
            'valor,'\
            'periodo,'\
            'conta_id)'\
         ' VALUES (''\'imported''\',true,false,now(),(select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'),now(),(select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'),'\
            '{0},'\
            '{1},'\
            '{2});'

print('start')
insertIntoTipoSql = open('insert_into_tipo-firstlayout.sql', 'a')
insertIntoTipoSql.seek(0)
insertIntoTipoSql.truncate()

insertIntoLocalSql = open('insert_into_local-firstlayout.sql', 'a')
insertIntoLocalSql.seek(0)
insertIntoLocalSql.truncate()

insertIntoContaSql = open('insert_into_conta-firstlayout.sql', 'a')
insertIntoContaSql.seek(0)
insertIntoContaSql.truncate()

insertIntoPontoSql = open('insert_into_ponto-firstlayout.sql', 'a')
insertIntoPontoSql.seek(0)
insertIntoPontoSql.truncate()

locais = list()
tipos = list()
contas = list()

def addTipos(cursor, tipo):
    try:
        cursor.execute(selectTipo.format(tipo))
        if (cursor.rowcount == 0):
            if (not tipo in tipos):
                tipos.append(tipo)
                print('=== tipo NOT found: {0}'.format(tipo))
                insertIntoTipoFormated = insertIntoTipo.format(tipo, selectUsuario) 
                insertIntoTipoSql.write(insertIntoTipoFormated)
                insertIntoTipoSql.write('\n')
    except Exception as e:
        print(e)

def addLocais(cursor, local, tipo):
    try:
        cursor.execute(selectLocal.format(local))
        if (cursor.rowcount == 0):
            if (not local in locais):
                locais.append(local)
                print('=== local NOT found: {0} - {1}'.format(local, tipo))
                insertIntoLocalFormated = insertIntoLocal.format(local, selectUsuario, selectTipo.format(tipo))
                insertIntoLocalSql.write(insertIntoLocalFormated)
                insertIntoLocalSql.write('\n')
    except Exception as e:
        print(e)

def addContas(cursor, conta, local, tipo):
    try:
        cursor.execute(selectConta.format(selectLocal.format(local), selectTipo.format(tipo), conta))
        if (cursor.rowcount == 0):
            if (not conta in contas):
                contas.append(conta)
                print('=== conta NOT found: {0} - {1} - {2}'.format(conta, tipo, local))
                insertIntoContaFormated = insertIntoConta.format(conta, selectUsuario, selectLocal.format(local), selectTipo.format(tipo))
                insertIntoContaSql.write(insertIntoContaFormated)
                insertIntoContaSql.write('\n')  
    except Exception as e:
        print(e)

def process(cursor, file):
    print(file)
    try:
        origem = open(file, 'rt')
        reader = csv.reader(origem)
        for row in reader:
            first_cel = True
            for cel in row:
                if (first_cel):
                    first_cel = False
                    continue
                
                cel_splited = cel.split('-')
                local = cel_splited[0]
                tipo = cel_splited[1]
                conta = cel_splited[2]
                addTipos(cursor, tipo)
                addLocais(cursor, local, tipo)
                addContas(cursor, conta, local, tipo)
                    
            break
    finally:
        origem.close()
        

print('start')
try:
    print('connection')
    connection = psycopg2.connect('dbname=''pims'' user=''pims'' host=''localhost'' password=''viniciusmayer''')
    cursor = connection.cursor()
    process(cursor, '../files/EleonorVinicius-Financas-2011.csv')
    process(cursor, '../files/EleonorVinicius-Financas-2012.csv')
    process(cursor, '../files/EleonorVinicius-Financas-2013.csv')
except Exception as e:
    print(e)

connection.close()
insertIntoTipoSql.close()
insertIntoLocalSql.close()
insertIntoContaSql.close()
insertIntoPontoSql.close()
print('end')