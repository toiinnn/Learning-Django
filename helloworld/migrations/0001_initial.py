# Generated by Django 2.2.3 on 2019-07-15 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14)),
                ('workTime', models.IntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
