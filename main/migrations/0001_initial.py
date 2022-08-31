# Generated by Django 4.1 on 2022-08-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('difficulty', models.CharField(max_length=7)),
                ('grade', models.CharField(max_length=2)),
                ('type', models.CharField(max_length=25)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=500)),
                ('degree', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=500)),
                ('grade', models.CharField(max_length=7)),
                ('password', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=20)),
                ('school', models.CharField(max_length=100)),
            ],
        ),
    ]