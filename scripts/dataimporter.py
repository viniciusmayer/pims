import csv
from datetime import date


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
               
insertIntoConta = 'INSERT INTO backend_conta(nome, observacoes, ativo, excluido,'\
                        'data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id)'\
                  ' VALUES (''\'{0}''\', ''\'imported''\', true, false, now(), {1}, now(), {1}, {2}, {3});'
                 
insertIntoPonto = 'INSERT INTO backend_ponto(observacoes,ativo,excluido,data_hora_criacao,usuario_criacao_id,data_hora_atualizacao,usuario_atualizacao_id,'\
            'valor,'\
            'periodo,'\
            'conta_id)'\
         ' VALUES (''\'imported''\',true,false,now(),(select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'),now(),(select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'),'\
            '{0},'\
            '{1},'\
            '{2});'

print "start"
origem = open("../files/EleonorVinicius-Financas.csv", 'rb')
insertIntoTipoSql = open("insert_into_tipo.sql", 'a')
insertIntoTipoSql.seek(0)
insertIntoTipoSql.truncate()

insertIntoLocalSql = open("insert_into_local.sql", 'a')
insertIntoLocalSql.seek(0)
insertIntoLocalSql.truncate()

insertIntoContaSql = open("insert_into_conta.sql", 'a')
insertIntoContaSql.seek(0)
insertIntoContaSql.truncate()

insertIntoPontoSql = open("insert_into_ponto.sql", 'a')
insertIntoPontoSql.seek(0)
insertIntoPontoSql.truncate()

tipos = list()
locais = list()

try:
    reader = csv.reader(origem)
    for rows in reader:
        for row in rows:
            cels = row.split(";")
            
            local = cels[0]
            tipo = cels[1]
            conta = cels[2]
            
            if (not tipo in tipos):
                tipos.append(tipo)
                insertIntoTipoFormated = insertIntoTipo.format(tipo, selectUsuario) 
                insertIntoTipoSql.write(insertIntoTipoFormated)
                insertIntoTipoSql.write('\n')

            if (not local in locais):
                locais.append(local)
                insertIntoLocalFormated = insertIntoLocal.format(local, selectUsuario, selectTipo.format('conta corrente'))
                insertIntoLocalSql.write(insertIntoLocalFormated)
                insertIntoLocalSql.write('\n')
                
            conta = tipo if (conta == '-') else conta
            insertIntoContaFormated = insertIntoConta.format(conta, selectUsuario, selectLocal.format(local), selectTipo.format(tipo))
            insertIntoContaSql.write(insertIntoContaFormated)
            insertIntoContaSql.write('\n')                
            
            for x in range(0, 10):
                if (cels[x + 3] != '-'):
                    p = (cels[x + 3], "'{0}'".format(date(2014, (x + 1), 15)), selectConta.format(selectLocal.format(local), selectTipo.format(tipo), conta))
                    insertIntoPontoSql.write(insertIntoPonto.format(*p))
                    insertIntoPontoSql.write("\n")
            
finally:
    origem.close()
    insertIntoTipoSql.close()
    insertIntoLocalSql.close()
    insertIntoContaSql.close()
    insertIntoPontoSql.close()

print "end"
