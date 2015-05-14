select periodo."data", periodoAnterior."data", conta.nome, tipo.nome, "local".nome
from backend_ponto ponto
	inner join backend_ponto pontoAnterior on (ponto."pontoAnterior_id"=pontoAnterior.id)
	inner join backend_periodo periodo on (ponto.periodo_id=periodo.id)
	inner join backend_periodo periodoAnterior on (pontoAnterior.periodo_id=periodoAnterior.id)
	inner join backend_conta conta on (ponto.conta_id=conta.id)
	inner join backend_tipo tipo on (conta.tipo_id=tipo.id)
	inner join backend_local "local" on (conta.local_id="local".id)
where (periodo."data" - interval '1 month') > periodoAnterior."data"
