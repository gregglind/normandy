# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-04 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import normandy.recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_action_arguments_schema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='arguments_schema',
            field=models.TextField(default='{}', validators=[normandy.recipes.validators.validate_json]),
        ),
        migrations.AlterField(
            model_name='recipeaction',
            name='arguments',
            field=models.TextField(default='{}', validators=[normandy.recipes.validators.validate_json]),
        ),
    ]
