INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id) VALUES ('corrente', 'imported', true, false, false, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_local where nome = 'banrisul'), (select id from backend_tipo where nome = 'conta'));
INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id) VALUES ('cdb', 'imported', true, false, true, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_local where nome = 'banrisul'), (select id from backend_tipo where nome = 'cdb'));
INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id) VALUES ('corrente', 'imported', true, false, false, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_local where nome = 'itau'), (select id from backend_tipo where nome = 'conta'));
INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id) VALUES ('poupanca', 'imported', true, false, true, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_local where nome = 'itau'), (select id from backend_tipo where nome = 'conta'));
INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id) VALUES ('capitalizacao', 'imported', true, false, false, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_local where nome = 'itau'), (select id from backend_tipo where nome = 'capitalizacao'));
INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id) VALUES ('cdb', 'imported', true, false, true, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_local where nome = 'itau'), (select id from backend_tipo where nome = 'cdb'));
INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id) VALUES ('cap', 'imported', true, false, true, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_local where nome = 'itau'), (select id from backend_tipo where nome = 'fundo'));
INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id) VALUES ('kinea', 'imported', true, false, true, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_local where nome = 'itau'), (select id from backend_tipo where nome = 'fundo'));
INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id) VALUES ('privada', 'imported', true, false, true, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_local where nome = 'itau'), (select id from backend_tipo where nome = 'previdencia'));
INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id) VALUES ('mastercard', 'imported', true, false, false, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_local where nome = 'itau'), (select id from backend_tipo where nome = 'cartao'));
INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id) VALUES ('travelmoney', 'imported', true, false, false, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_local where nome = 'itau'), (select id from backend_tipo where nome = 'cartao'));
INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id) VALUES ('travelmoney', 'imported', true, false, false, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_local where nome = 'visa'), (select id from backend_tipo where nome = 'cartao'));
INSERT INTO backend_conta(nome, observacoes, ativo, excluido, rendimento,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, local_id, tipo_id) VALUES ('corrente', 'imported', true, false, false, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_local where nome = 'aib'), (select id from backend_tipo where nome = 'conta'));