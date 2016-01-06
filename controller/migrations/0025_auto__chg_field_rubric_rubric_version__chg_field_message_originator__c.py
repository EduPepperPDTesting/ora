# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Rubric.rubric_version'
        db.alter_column('controller_rubric', 'rubric_version', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Message.originator'
        db.alter_column('controller_message', 'originator', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Message.message_type'
        db.alter_column('controller_message', 'message_type', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Message.recipient'
        db.alter_column('controller_message', 'recipient', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'RubricOption.short_text'
        db.alter_column('controller_rubricoption', 'short_text', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Submission.xqueue_queue_name'
        db.alter_column('controller_submission', 'xqueue_queue_name', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Submission.course_id'
        db.alter_column('controller_submission', 'course_id', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Submission.student_id'
        db.alter_column('controller_submission', 'student_id', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Submission.location'
        db.alter_column('controller_submission', 'location', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):

        # Changing field 'Rubric.rubric_version'
        db.alter_column('controller_rubric', 'rubric_version', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Message.originator'
        db.alter_column('controller_message', 'originator', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Message.message_type'
        db.alter_column('controller_message', 'message_type', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Message.recipient'
        db.alter_column('controller_message', 'recipient', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'RubricOption.short_text'
        db.alter_column('controller_rubricoption', 'short_text', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Submission.xqueue_queue_name'
        db.alter_column('controller_submission', 'xqueue_queue_name', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Submission.course_id'
        db.alter_column('controller_submission', 'course_id', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Submission.student_id'
        db.alter_column('controller_submission', 'student_id', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Submission.location'
        db.alter_column('controller_submission', 'location', self.gf('django.db.models.fields.CharField')(max_length=1024))

    models = {
        'controller.grader': {
            'Meta': {'object_name': 'Grader'},
            'confidence': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '9'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feedback': ('django.db.models.fields.TextField', [], {}),
            'grader_id': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '1024'}),
            'grader_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_calibration': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'status_code': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['controller.Submission']"})
        },
        'controller.message': {
            'Meta': {'object_name': 'Message'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'grader': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['controller.Grader']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'message_type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'originator': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'controller.rubric': {
            'Meta': {'object_name': 'Rubric'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'finished_scoring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'grader': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['controller.Grader']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rubric_version': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'controller.rubricitem': {
            'Meta': {'object_name': 'RubricItem'},
            'comment': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'finished_scoring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_number': ('django.db.models.fields.IntegerField', [], {}),
            'max_score': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'rubric': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['controller.Rubric']"}),
            'score': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'short_text': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'controller.rubricoption': {
            'Meta': {'object_name': 'RubricOption'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_number': ('django.db.models.fields.IntegerField', [], {}),
            'points': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'rubric_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['controller.RubricItem']"}),
            'short_text': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'controller.submission': {
            'Meta': {'object_name': 'Submission'},
            'answer': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'duplicate_submission_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grader_settings': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_display': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'is_duplicate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_plagiarized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'max_score': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'next_grader_type': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '2'}),
            'posted_results_back_to_queue': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'preferred_grader_type': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '2'}),
            'previous_grader_type': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '2'}),
            'problem_id': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'prompt': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'rubric': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'student_id': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'student_response': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'student_submission_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'xqueue_queue_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'xqueue_submission_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024'}),
            'xqueue_submission_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024'})
        }
    }

    complete_apps = ['controller']