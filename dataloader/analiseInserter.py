import psycopg2


selectPeriodo = 'select distinct "data", id from backend_periodo where "data" not in ('\
    'select periodo."data" from backend_analise analise inner join backend_periodo periodo on (analise.periodo_id=periodo.id))'

insertIntoAnalise = 'INSERT INTO backend_analise(observacoes, ativo, excluido, data_hora_criacao, usuario_criacao_id,data_hora_atualizacao, usuario_atualizacao_id,'\
    ' periodo_id)'\
    ' VALUES (''\'imported''\', true, false, now(), (select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'), now(), (select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'),'\
    ' {0});'

selectAnalise = 'select analise.id, periodo."data"'\
    ' from backend_analise analise inner join backend_periodo periodo on (analise.periodo_id=periodo.id)'\
    ' where "analiseAnterior_id" is null'

selectAnaliseAnterior = 'select analise.id, periodo."data"'\
    ' from backend_analise analise inner join backend_periodo periodo on (analise.periodo_id=periodo.id)'\
    ' where periodo."data" < ''\'{0}''\''\
    ' order by 2 desc'\
    ' limit 1'

updateAnalise = 'update backend_analise set "analiseAnterior_id" = {0} where id = {1}'

if __name__ == '__main__':
    connection = psycopg2.connect('dbname=''pims'' user=''pims'' host=''localhost'' password=''viniciusmayer''')
    cursor = connection.cursor()
    
    cursor.execute(selectPeriodo)
    for periodo in cursor.fetchall():
        cursor.execute(insertIntoAnalise.format(periodo[1]))
        connection.commit()

    cursor.execute(selectAnalise)
    for analise in cursor.fetchall():
        cursor.execute(selectAnaliseAnterior.format(analise[1]))
        if (cursor.rowcount > 0):
            for analiseAnterior in cursor.fetchall():
                cursor.execute(updateAnalise.format(analiseAnterior[0], analise[0]))
                connection.commit()
    
    connection.close()