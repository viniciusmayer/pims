INSERT INTO backend_local(nome, observacoes, ativo, excluido,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, tipo_id) VALUES ('banrisul', 'imported', true, false, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_tipo where nome = 'conta'));
INSERT INTO backend_local(nome, observacoes, ativo, excluido,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, tipo_id) VALUES ('itau', 'imported', true, false, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_tipo where nome = 'conta'));
INSERT INTO backend_local(nome, observacoes, ativo, excluido,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, tipo_id) VALUES ('visa', 'imported', true, false, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_tipo where nome = 'conta'));
INSERT INTO backend_local(nome, observacoes, ativo, excluido,data_hora_criacao, usuario_criacao_id, data_hora_atualizacao, usuario_atualizacao_id, tipo_id) VALUES ('aib', 'imported', true, false, now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), now(), (select id from auth_user where email = 'viniciusmayer@gmail.com'), (select id from backend_tipo where nome = 'conta'));
