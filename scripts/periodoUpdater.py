import psycopg2


selectPeriodo = 'select id, data from backend_periodo order by 2 desc'
selectPeriodoAnterior = 'select id, data from backend_periodo where data < ''\'{0}''\' order by 2 desc limit 1'
update = 'update backend_periodo set "periodoAnterior_id" = {0} where id = {1}'

if __name__ == '__main__':
    connection = psycopg2.connect('dbname=''pims'' user=''pims'' host=''localhost'' password=''viniciusmayer''')
    cursor = connection.cursor()
    
    try:
        cursor.execute(selectPeriodo)
        for row in cursor.fetchall():
            cursor.execute(selectPeriodoAnterior.format(row[1]))
            for _row in cursor.fetchall():
                if (not _row[0] is None):
                    cursor.execute(update.format(_row[0], row[0]))
                    connection.commit()
    except Exception as e:
        print(e)