# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20170328_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='files',
            field=models.FileField(default='docs/None/No-doc.pdf', upload_to='Docs/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='files',
            field=models.FileField(default='docs/None/No-doc.pdf', upload_to='Docs/'),
        ),
    ]