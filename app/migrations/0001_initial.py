# Generated by Django 4.2.2 on 2023-06-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Eid', models.IntegerField(primary_key=True, serialize=False)),
                ('Ename', models.CharField(max_length=100)),
                ('Eage', models.IntegerField()),
            ],
        ),
    ]
