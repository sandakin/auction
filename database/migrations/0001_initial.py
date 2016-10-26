# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-17 00:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_count', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='HealthCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('video', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(default='0', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='HealthState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_desc', models.CharField(max_length=200, null=True)),
                ('health_card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='states', to='database.HealthCard')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipocde', models.CharField(max_length=100, null=True)),
                ('dob', models.CharField(max_length=100, null=True)),
                ('sex', models.CharField(max_length=100, null=True)),
                ('hypertension', models.CharField(max_length=100, null=True)),
                ('insulin', models.CharField(max_length=100, null=True)),
                ('noninsulin', models.CharField(max_length=100, null=True)),
                ('asthma', models.CharField(max_length=100, null=True)),
                ('epilepsy', models.CharField(max_length=100, null=True)),
                ('anaemia', models.CharField(max_length=100, null=True)),
                ('renal', models.CharField(max_length=100, null=True)),
                ('cardiac', models.CharField(max_length=100, null=True)),
                ('accident', models.CharField(max_length=100, null=True)),
                ('mentalhealth', models.CharField(max_length=100, null=True)),
                ('gastro', models.CharField(max_length=100, null=True)),
                ('skin', models.CharField(max_length=100, null=True)),
                ('cancer', models.CharField(max_length=100, null=True)),
                ('other', models.CharField(max_length=100, null=True)),
                ('mobility', models.CharField(max_length=100, null=True)),
                ('personal', models.CharField(max_length=100, null=True)),
                ('activities', models.CharField(max_length=100, null=True)),
                ('pain', models.CharField(max_length=100, null=True)),
                ('anxiety', models.CharField(max_length=100, null=True)),
                ('health', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]