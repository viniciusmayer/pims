select true as "ativo"
	, false as "excluido"
	, now() as "data_hora_criacao"
	, (select id from auth_user where email = 'viniciusmayer@gmail.com') as "usuario_criacao_id"
	, now() as "data_hora_atualizacao"
	, (select id from auth_user where email = 'viniciusmayer@gmail.com') as "usuario_atualizacao_id"
	, p.periodo_id
	, sum(p.valor) as "total"
from backend_ponto p
group by p.periodo_id