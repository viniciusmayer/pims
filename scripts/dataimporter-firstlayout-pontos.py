import csv
from datetime import date, datetime
import psycopg2

from scripts.analisePeriodoUpdater import selectPeriodo


class Conta(object):
    def __init__(self, conta, tipo, local):
        self.conta = conta
        self.tipo = tipo
        self.local = local
    def __str__(self):
        return '{0} - {1} - {2}'.format(self.conta, self.tipo, self.local)

selectUsuario = '(select id from auth_user where email = ''\'viniciusmayer@gmail.com''\')'
selectTipo = '(select id from backend_tipo where nome = ''\'{0}''\')'
selectLocal = '(select id from backend_local where nome = ''\'{0}''\')'
selectConta = '(select id from backend_conta where local_id = {0} and tipo_id = {1} and nome = ''\'{2}''\')'
selectPeriodo = 'select id from backend_periodo where "data" = ''\'{0}''\''

insertIntoPonto = 'INSERT INTO backend_ponto(observacoes, ativo, excluido, data_hora_criacao, usuario_criacao_id,data_hora_atualizacao, usuario_atualizacao_id,'\
        ' valor, conta_id, periodo_id)'\
    ' VALUES (''\'imported''\', true, false, now(), (select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'), now(), (select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'),'\
        ' {0}, {1}, {2});'

def getContas(file):
    try:
        contas = list()
        origem = open(file, 'rt')
        reader = csv.reader(origem)
        for rows in reader:
            for row in rows:
                first_cel = True
                column = 0
                cels = row.split(';')
                for cel in cels:
                    if (first_cel):
                        first_cel = False
                        continue
                    cel_splited = cel.split('-')
                    local = cel_splited[0]
                    tipo = cel_splited[1]
                    conta = cel_splited[2]
                    _conta = Conta(conta, tipo, local)
                    contas.insert(column, _conta)
                    column += 1
            break
        return contas
    finally:
        origem.close()

def getPeriodos(file):
    try:
        periodos = list()
        origem = open(file, 'rt')
        reader = csv.reader(origem)
        first_row = True
        for rows in reader:
            for row in rows:
                if (first_row):
                    first_row = False
                    continue
                first_cel = True
                column = 0
                date = None
                cels = row.split(';')
                for cel in cels:
                    if (first_cel):
                        cel_splited = cel.split('/')
                        date = datetime(int(cel_splited[2]), int(cel_splited[0]), int(cel_splited[1]))
                        periodos.insert(column, date)
                        first_cel = False
                        column += 1
        return periodos
    finally:
        origem.close()

def process(cursor, contas, periodos, file):
    try:
        origem = open(file, 'rt')
        reader = csv.reader(origem)
        first_row = True
        column_periodo = -1
        for rows in reader:
            for row in rows:
                if (first_row):
                    first_row = False
                    continue
                first_cel = True
                column = 0
                periodo = None
                cels = row.split(';')
                for cel in cels:
                    if (first_cel):
                        periodo = periodos[column_periodo]
                        first_cel = False
                        continue
                    if (cel == '-'):
                        column += 1
                        continue
                    else:
                        conta = contas[column]
                        column += 1
                        cursor.execute(selectConta.format(selectLocal.format(conta.local), selectTipo.format(conta.tipo), conta.conta))
                        for _row in cursor.fetchall():
                            cursor.execute(selectPeriodo.format(periodo))
                            for __row in cursor.fetchall():
                                insertIntoPontoFormated = insertIntoPonto.format(cel, _row[0], __row[0])
                                insertIntoPontoSql.write(insertIntoPontoFormated)
                                insertIntoPontoSql.write('\n')
            column_periodo += 1

    finally:
        origem.close()

def main(cursor, file):
    contas = getContas(file)
    periodos = getPeriodos(file)
    periodos.reverse()
    process(cursor, contas, periodos, file)
    
print('start')
insertIntoPontoSql = open('insert_into_ponto-firstlayout.sql', 'a')
insertIntoPontoSql.seek(0)
insertIntoPontoSql.truncate()

connection = psycopg2.connect('dbname=''pims'' user=''pims'' host=''localhost'' password=''viniciusmayer''')
cursor = connection.cursor()
main(cursor, '../files/EleonorVinicius-Financas-2011.csv')
main(cursor, '../files/EleonorVinicius-Financas-2012.csv')
main(cursor, '../files/EleonorVinicius-Financas-2013.csv')

connection.close()
insertIntoPontoSql.close()
print('end')