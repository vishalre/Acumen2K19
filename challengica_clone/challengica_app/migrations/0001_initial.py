# Generated by Django 2.0.1 on 2018-03-14 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
                ('points', models.IntegerField(default=0)),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_img', models.TextField(max_length=100)),
                ('ques_text', models.TextField(max_length=3000)),
                ('ans_text', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SetNo',
            fields=[
                ('setno', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='setno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challengica_app.SetNo'),
        ),
        migrations.AddField(
            model_name='contestant',
            name='setno',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='challengica_app.SetNo'),
        ),
    ]