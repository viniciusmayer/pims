import csv
from datetime import date, datetime
import psycopg2


selectPeriodo = 'select * from backend_periodo where "data" = ''\'{0}''\''

insertIntoPeriodo = 'INSERT INTO backend_periodo ('\
        ' observacoes, ativo, excluido, data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, data)'\
    ' VALUES'\
        ' (''\'imported''\', true, false, now(),'\
        ' (select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'), now(),'\
        ' (select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'), ''\'{0}''\');'

def getPeriodos(file):
    try:
        periodos = list()
        origem = open(file, 'rt')
        reader = csv.reader(origem)
        first_row = True
        for row in reader:
            if (first_row):
                first_row = False
                continue
            first_cel = True
            column = 0
            date = None
            for cel in row:
                if (first_cel):
                    cel_splited = cel.split('/')
                    date = datetime(int(cel_splited[2]), int(cel_splited[0]), int(cel_splited[1]))
                    periodos.insert(column, date)
                    first_cel = False
                    column += 1
        return periodos
    finally:
        origem.close()

def process(cursos, file):
    periodos = getPeriodos(file)
    for periodo in periodos:
        cursor.execute(selectPeriodo.format(periodo))
        if (cursor.rowcount == 0):
            insertIntoPeriodoFormated = insertIntoPeriodo.format(periodo)
            insertIntoPeriodoSql.write(insertIntoPeriodoFormated)
            insertIntoPeriodoSql.write('\n')

print('start')
insertIntoPeriodoSql = open('insert_into_periodo-firstlayout.sql', 'a')
insertIntoPeriodoSql.seek(0)
insertIntoPeriodoSql.truncate()

try:
    connection = psycopg2.connect('dbname=''pims'' user=''pims'' host=''localhost'' password=''viniciusmayer''')
    cursor = connection.cursor()
    process(cursor, '../files/EleonorVinicius-Financas-2011.csv')
    process(cursor, '../files/EleonorVinicius-Financas-2012.csv')
    process(cursor, '../files/EleonorVinicius-Financas-2013.csv')
            
except Exception as e:
    print(e)

connection.close()
insertIntoPeriodoSql.close()
print('end')