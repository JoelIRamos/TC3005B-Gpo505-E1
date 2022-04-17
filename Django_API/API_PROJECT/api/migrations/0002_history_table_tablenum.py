# Generated by Django 4.0.3 on 2022-04-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('HistoryID', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='table',
            name='TableNum',
            field=models.IntegerField(default=0),
        ),
    ]
