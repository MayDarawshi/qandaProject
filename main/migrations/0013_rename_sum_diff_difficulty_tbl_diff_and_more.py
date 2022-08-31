# Generated by Django 4.1 on 2022-08-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_difficulty_tbl_remove_answer_posted_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='difficulty_tbl',
            old_name='sum_diff',
            new_name='diff',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='qid',
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]