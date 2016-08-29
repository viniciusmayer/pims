﻿select true as ativo
	, false as excluido
	, now() as data_hora_criacao
	, (select id from auth_user where email = 'viniciusmayer@gmail.com') as usuario_criacao_id
	, now() as data_hora_atualizacao
	, (select id from auth_user where email = 'viniciusmayer@gmail.com') as usuario_atualizacao_id
	, rendimentoporperiodo.periodo_id
	, rendimentoporperiodo.total
from (
	select pe.id as periodo_id
		, sum(po.valor
			- coalesce(poan.valor, 0)
			- coalesce(credito.valor, 0)
			+ coalesce(debito.valor, 0)) as total
	from backend_ponto po
		inner join backend_periodo pe on pe.id=po.periodo_id
		inner join backend_conta co on co.id=po.conta_id and co.rendimento = true
		left join (
			select distinct po.id
				, sum(mo.valor) as valor
			from backend_movimento mo
				inner join backend_ponto po on po.id=mo.ponto_id and mo.operacao='CR'
			group by 1
		) as credito on credito.id=po.id
		left join (
			select distinct po.id
				, sum(mo.valor) as valor
			from backend_movimento mo
				inner join backend_ponto po on po.id=mo.ponto_id and mo.operacao='DE'
			group by 1
		) as debito on debito.id=po.id
		left join backend_ponto poan on poan.id=po."pontoAnterior_id"
	group by 1
) as rendimentoporperiodo

/*select distinct pe.data
	, co.nome || ' ' || ti.nome || ' ' || lo.nome as conta
	, po.valor as ponto
	, coalesce(poan.valor, 0) as pontoanterior
	, coalesce(credito.valor, 0) as credito
	, coalesce(debito.valor, 0) as debito
	, (po.valor
		- coalesce(poan.valor, 0)
		- coalesce(credito.valor, 0)
		+ coalesce(debito.valor, 0))
from backend_ponto po
	inner join backend_periodo pe on pe.id=po.periodo_id and pe.data = '2015-05-15'
	inner join backend_conta co on co.id=po.conta_id and co.rendimento = true
	inner join backend_tipo ti on ti.id=co.tipo_id
	inner join backend_local lo on lo.id=co.local_id
	left join (
		select distinct po.id
			, sum(mo.valor) as valor
		from backend_movimento mo
			inner join backend_ponto po on po.id=mo.ponto_id and mo.operacao='CR'
		group by 1
	) as credito on credito.id=po.id
	left join (
		select distinct po.id
			, sum(mo.valor) as valor
		from backend_movimento mo
			inner join backend_ponto po on po.id=mo.ponto_id and mo.operacao='DE'
		group by 1
	) as debito on debito.id=po.id
	left join backend_ponto poan on poan.id=po."pontoAnterior_id"
--group by 1
order by 1 desc*/