# Generated by Django 2.2.24 on 2022-12-05 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('father_name', models.CharField(max_length=100)),
                ('point1', models.IntegerField()),
                ('point2', models.IntegerField()),
                ('total', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('fin', models.CharField(max_length=7)),
            ],
        ),
    ]
