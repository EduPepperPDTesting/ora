# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'Submission.max_score'
        db.add_column('controller_submission', 'max_score',
            self.gf('django.db.models.fields.IntegerField')(default=1),
            keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Submission.max_score'
        db.delete_column('controller_submission', 'max_score')


    models = {
        'controller.grader': {
            'Meta': {'object_name': 'Grader'},
            'confidence': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '9'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feedback': ('django.db.models.fields.TextField', [], {}),
            'grader_id': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'grader_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'status_code': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['controller.Submission']"})
        },
        'controller.submission': {
            'Meta': {'object_name': 'Submission'},
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'max_score': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'next_grader_type': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '2'}),
            'previous_grader_type': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '2'}),
            'problem_id': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'prompt': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'student_id': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'student_response': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'student_submission_time': (
            'django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'xqueue_queue_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'xqueue_submission_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'xqueue_submission_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'})
        }
    }

    complete_apps = ['controller']