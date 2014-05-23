# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Investimento'
        db.delete_table(u'backend_investimento')

        # Deleting model 'Valor'
        db.delete_table(u'backend_valor')

        # Deleting model 'Instituicao'
        db.delete_table(u'backend_instituicao')

        # Adding model 'Conta'
        db.create_table(u'backend_conta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('usuario_criacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_conta_criacao_related', to=orm['auth.User'])),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('usuario_atualizacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_conta_atualizacao_related', to=orm['auth.User'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('local', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Local'])),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Tipo'])),
        ))
        db.send_create_signal(u'backend', ['Conta'])

        # Adding model 'Ponto'
        db.create_table(u'backend_ponto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('usuario_criacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_ponto_criacao_related', to=orm['auth.User'])),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('usuario_atualizacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_ponto_atualizacao_related', to=orm['auth.User'])),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('periodo', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 5, 23, 0, 0))),
            ('periodoAnterior', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Ponto'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('conta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Conta'])),
        ))
        db.send_create_signal(u'backend', ['Ponto'])

        # Adding model 'Local'
        db.create_table(u'backend_local', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('usuario_criacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_local_criacao_related', to=orm['auth.User'])),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('usuario_atualizacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_local_atualizacao_related', to=orm['auth.User'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Tipo'])),
        ))
        db.send_create_signal(u'backend', ['Local'])


    def backwards(self, orm):
        # Adding model 'Investimento'
        db.create_table(u'backend_investimento', (
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('usuario_atualizacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_investimento_atualizacao_related', to=orm['auth.User'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Tipo'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('instituicao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Instituicao'])),
            ('usuario_criacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_investimento_criacao_related', to=orm['auth.User'])),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'backend', ['Investimento'])

        # Adding model 'Valor'
        db.create_table(u'backend_valor', (
            ('investimento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Investimento'])),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('usuario_atualizacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_valor_atualizacao_related', to=orm['auth.User'])),
            ('data', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 5, 23, 0, 0))),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('usuario_criacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_valor_criacao_related', to=orm['auth.User'])),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'backend', ['Valor'])

        # Adding model 'Instituicao'
        db.create_table(u'backend_instituicao', (
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('usuario_atualizacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_instituicao_atualizacao_related', to=orm['auth.User'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Tipo'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('usuario_criacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_instituicao_criacao_related', to=orm['auth.User'])),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'backend', ['Instituicao'])

        # Deleting model 'Conta'
        db.delete_table(u'backend_conta')

        # Deleting model 'Ponto'
        db.delete_table(u'backend_ponto')

        # Deleting model 'Local'
        db.delete_table(u'backend_local')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'backend.conta': {
            'Meta': {'ordering': "['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Conta'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Local']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Tipo']"}),
            'usuario_atualizacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_conta_atualizacao_related'", 'to': u"orm['auth.User']"}),
            'usuario_criacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_conta_criacao_related'", 'to': u"orm['auth.User']"})
        },
        u'backend.local': {
            'Meta': {'ordering': "['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Local'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Tipo']"}),
            'usuario_atualizacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_local_atualizacao_related'", 'to': u"orm['auth.User']"}),
            'usuario_criacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_local_criacao_related'", 'to': u"orm['auth.User']"})
        },
        u'backend.ponto': {
            'Meta': {'ordering': "['-ativo', '-periodo', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Ponto'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'conta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Conta']"}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'periodo': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 23, 0, 0)'}),
            'periodoAnterior': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Ponto']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'usuario_atualizacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_ponto_atualizacao_related'", 'to': u"orm['auth.User']"}),
            'usuario_criacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_ponto_criacao_related'", 'to': u"orm['auth.User']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        },
        u'backend.tipo': {
            'Meta': {'ordering': "['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Tipo'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'usuario_atualizacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_tipo_atualizacao_related'", 'to': u"orm['auth.User']"}),
            'usuario_criacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_tipo_criacao_related'", 'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['backend']