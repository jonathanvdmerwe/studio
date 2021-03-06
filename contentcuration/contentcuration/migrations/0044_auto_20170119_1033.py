# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-19 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0043_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formatpreset',
            name='id',
            field=models.CharField(choices=[(b'high_res_video', b'High Resolution'), (b'low_res_video', b'Low Resolution'), (b'vector_video', b'Vectorized'), (b'video_thumbnail', b'Thumbnail'), (b'video_subtitle', b'Subtitle'), (b'audio', b'Audio'), (b'audio_thumbnail', b'Thumbnail'), (b'document', b'Document'), (b'document_thumbnail', b'Thumbnail'), (b'exercise', b'Exercise'), (b'exercise_thumbnail', b'Thumbnail'), (b'exercise_image', b'Exercise Image'), (b'exercise_graphie', b'Exercise Graphie'), (b'channel_thumbnail', b'Channel Thumbnail'), (b'html5_zip', b'HTML5 Zip'), (b'html5_thumbnail', b'HTML5 Thumbnail')], max_length=150, primary_key=True, serialize=False),
        ),
    ]
