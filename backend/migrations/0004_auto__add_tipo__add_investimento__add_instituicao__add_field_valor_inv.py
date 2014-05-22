# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tipo'
        db.create_table(u'backend_tipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('usuario_criacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_tipo_criacao_related', to=orm['auth.User'])),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('usuario_atualizacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_tipo_atualizacao_related', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'backend', ['Tipo'])

        # Adding model 'Investimento'
        db.create_table(u'backend_investimento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('usuario_criacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_investimento_criacao_related', to=orm['auth.User'])),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('usuario_atualizacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_investimento_atualizacao_related', to=orm['auth.User'])),
            ('instituicao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Instituicao'])),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Tipo'])),
        ))
        db.send_create_signal(u'backend', ['Investimento'])

        # Adding model 'Instituicao'
        db.create_table(u'backend_instituicao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('usuario_criacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_instituicao_criacao_related', to=orm['auth.User'])),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('usuario_atualizacao', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'backend_instituicao_atualizacao_related', to=orm['auth.User'])),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Tipo'])),
        ))
        db.send_create_signal(u'backend', ['Instituicao'])

        # Adding field 'Valor.investimento'
        db.add_column(u'backend_valor', 'investimento',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['backend.Investimento']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Tipo'
        db.delete_table(u'backend_tipo')

        # Deleting model 'Investimento'
        db.delete_table(u'backend_investimento')

        # Deleting model 'Instituicao'
        db.delete_table(u'backend_instituicao')

        # Deleting field 'Valor.investimento'
        db.delete_column(u'backend_valor', 'investimento_id')


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
        u'backend.instituicao': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Instituicao'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Tipo']"}),
            'usuario_atualizacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_instituicao_atualizacao_related'", 'to': u"orm['auth.User']"}),
            'usuario_criacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_instituicao_criacao_related'", 'to': u"orm['auth.User']"})
        },
        u'backend.investimento': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Investimento'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituicao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Instituicao']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Tipo']"}),
            'usuario_atualizacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_investimento_atualizacao_related'", 'to': u"orm['auth.User']"}),
            'usuario_criacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_investimento_criacao_related'", 'to': u"orm['auth.User']"})
        },
        u'backend.tipo': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Tipo'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'usuario_atualizacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_tipo_atualizacao_related'", 'to': u"orm['auth.User']"}),
            'usuario_criacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_tipo_criacao_related'", 'to': u"orm['auth.User']"})
        },
        u'backend.valor': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Valor'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investimento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Investimento']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'usuario_atualizacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_valor_atualizacao_related'", 'to': u"orm['auth.User']"}),
            'usuario_criacao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'backend_valor_criacao_related'", 'to': u"orm['auth.User']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
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