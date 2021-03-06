# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Server.is_proxmox'
        db.delete_column(u'servers_server', 'is_proxmox')

        # Adding field 'Server.is_vm'
        db.add_column(u'servers_server', 'is_vm',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Server.vm_host'
        db.add_column(u'servers_server', 'vm_host',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servers.Server'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Server.is_proxmox'
        db.add_column(u'servers_server', 'is_proxmox',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Server.is_vm'
        db.delete_column(u'servers_server', 'is_vm')

        # Deleting field 'Server.vm_host'
        db.delete_column(u'servers_server', 'vm_host_id')


    models = {
        u'servers.server': {
            'Meta': {'object_name': 'Server'},
            'external_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interal_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'is_vm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keymanger_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ssh_connection_string': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'vm_host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['servers.Server']", 'null': 'True', 'blank': 'True'})
        },
        u'servers.sshkey': {
            'Meta': {'object_name': 'SshKey'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.TextField', [], {}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['servers.Server']"}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['servers']