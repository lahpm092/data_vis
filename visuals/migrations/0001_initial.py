# Generated by Django 2.1 on 2018-09-09 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Infecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('agent', models.CharField(max_length=50)),
                ('epidemiology', models.CharField(max_length=50)),
                ('diagnosis', models.CharField(max_length=50)),
                ('treatment', models.CharField(max_length=50)),
                ('clinical', models.ManyToManyField(to='visuals.Clinical')),
            ],
        ),
    ]