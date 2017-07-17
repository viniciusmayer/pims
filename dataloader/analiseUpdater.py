import psycopg2


selectRendimentoPorPeriodo = 'select id, periodo from backend_analise'
selectPeriodo = 'select id from backend_periodo where data = ''\'{0}''\''
update = 'update backend_analise set "periodoTempo_id" = {0} where id = {1}'

if __name__ == '__main__':
    connection = psycopg2.connect('dbname=''pims'' user=''pims'' host=''localhost'' password=''viniciusmayer''')
    cursor = connection.cursor()
    
    try:
        cursor.execute(selectRendimentoPorPeriodo)
        for row in cursor.fetchall():
            cursor.execute(selectPeriodo.format(row[1]))
            for _row in cursor.fetchall():
                if (not _row[0] is None):
                    cursor.execute(update.format(_row[0], row[0]))
                    connection.commit()
    except Exception as e:
        print(e)