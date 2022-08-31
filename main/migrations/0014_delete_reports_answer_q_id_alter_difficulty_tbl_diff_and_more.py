# Generated by Django 4.1 on 2022-08-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_sum_diff_difficulty_tbl_diff_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='reports',
        ),
        migrations.AddField(
            model_name='answer',
            name='q_id',
            field=models.TextField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='difficulty_tbl',
            name='diff',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='difficulty_tbl',
            name='qid',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]