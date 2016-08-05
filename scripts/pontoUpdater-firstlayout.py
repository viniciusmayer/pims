import psycopg2


selectConta = 'select id from backend_conta'

selectPonto = 'select ponto.id, periodo."data"'\
    ' from backend_ponto ponto inner join backend_periodo periodo on (ponto.periodo_id=periodo.id)'\
    ' where ponto."pontoAnterior_id" is null'\
        ' and ponto.conta_id = {0}'\
    ' order by 2 desc'

selectPontoAnterior = 'select ponto.id, periodo."data"'\
    ' from backend_ponto ponto inner join backend_periodo periodo on (ponto.periodo_id=periodo.id)'\
    ' where periodo."data" < ('\
        'select periodo."data"'\
            ' from backend_ponto ponto inner join backend_periodo periodo on (ponto.periodo_id=periodo.id)'\
            ' where ponto.id = {0}'\
        ')'\
        ' and ponto.conta_id = {1}'\
    ' order by 2 desc'\
    ' limit 1'
    
updatePonto = 'update backend_ponto set "pontoAnterior_id" = {0} where id = {1}'

if __name__ == '__main__':
    connection = psycopg2.connect('dbname=''pims'' user=''pims'' host=''localhost'' password=''viniciusmayer''')
    cursor = connection.cursor()
    
    cursor.execute(selectConta)
    for conta in cursor.fetchall(): #para todas as contas
        
        cursor.execute(selectPonto.format(conta[0]))
        for ponto in cursor.fetchall(): #para todos os pontos
            
            cursor.execute(selectPontoAnterior.format(ponto[0], conta[0]))
            for pontoAnterior in cursor.fetchall(): #para todos os pontos anteriores
                if (cursor.rowcount != 0):
                    cursor.execute(updatePonto.format(pontoAnterior[0], ponto[0]))
                    connection.commit()
    
    connection.close()