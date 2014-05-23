import csv
from datetime import date


insert = 'INSERT INTO backend_valor(observacoes,ativo,excluido,data_hora_criacao,usuario_criacao_id,data_hora_atualizacao,usuario_atualizacao_id,'\
            'valor,'\
            '"data",'\
            'investimento_id)'\
         ' VALUES (''\'imported\''',true,false,now(),(select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'),now(),(select id from auth_user where email = ''\'viniciusmayer@gmail.com''\'),'\
            '{0},'\
            '{1},'\
            '(select id from backend_investimento'\
            ' where instituicao_id = (select id from backend_instituicao where nome = ''\'{2}''\')'\
            ' and tipo_id = (select id from backend_tipo where nome = ''\'{3}''\')'\
            ' and nome = ''\'{4}''\'));'

if __name__ == '__main__':
    f = open("../files/EleonorVinicius-Financas-working.csv", 'rb')
    try:
        reader = csv.reader(f)
        for rows in reader:
            for row in rows:
                cels = row.split(";")
                
                invest = cels[1] if (cels[2] == '-') else cels[2]
                
                if (cels[3] != '-'):
                    jan = (cels[3], "'{0}'".format(date(2014, 01, 15)), cels[0], cels[1], invest)
                    print insert.format(*jan)
                
                if (cels[4] != '-'):
                    fev = (cels[4], "'{0}'".format(date(2014, 02, 15)), cels[0], cels[1], invest)
                    print insert.format(*fev)
                
                if (cels[5] != '-'):
                    mar = (cels[5], "'{0}'".format(date(2014, 03, 15)), cels[0], cels[1], invest)
                    print insert.format(*mar)
                
                if (cels[6] != '-'):
                    abr = (cels[6], "'{0}'".format(date(2014, 04, 15)), cels[0], cels[1], invest)
                    print insert.format(*abr)
                
                if (cels[7] != '-'):
                    mai = (cels[7], "'{0}'".format(date(2014, 05, 15)), cels[0], cels[1], invest)
                    print insert.format(*mai)
                
    finally:
        f.close()