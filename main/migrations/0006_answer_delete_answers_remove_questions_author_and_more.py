# Generated by Django 4.1 on 2022-08-22 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_questions_author_alter_reports_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('answer_text', models.TextField(max_length=50000)),
                ('posted_by', models.TextField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='author',
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='reports',
            name='user_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='answer',
            name='qid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.questions'),
        ),
    ]
