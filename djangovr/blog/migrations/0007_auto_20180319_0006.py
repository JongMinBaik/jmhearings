# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-18 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180318_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('모집중', '모집중'), ('준비중', '준비중'), ('제작중', '제작중'), ('배포완료', '배포완료'), ('제작중단', '제작중단')], default='모집중', max_length=20),
        ),
    ]