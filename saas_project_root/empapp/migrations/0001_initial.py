# Generated by Django 4.2.7 on 2023-12-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
