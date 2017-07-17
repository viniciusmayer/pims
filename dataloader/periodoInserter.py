import psycopg2


insertIntoPeriodo = 'INSERT INTO backend_periodo ('\
    ' observacoes, ativo, excluido, data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, data)'\
    ' VALUES'\
    ' (''\'imported''\', true, false, now(),'\
    ' (select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'), now(),'\
    ' (select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'), ''\'{0}''\');'

if __name__ == '__main__':
    connection = psycopg2.connect('dbname=''pims'' user=''pims'' host=''localhost'' password=''viniciusmayer''')
    cursor = connection.cursor()
    
    try:
        cursor.execute('select distinct periodo from backend_ponto;')
        for row in cursor.fetchall():
            cursor.execute(insertIntoPeriodo.format(row[0]))
            connection.commit()
    except Exception as e:
        print(e)