# Generated by Django 3.1.2 on 2020-11-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Departament Name', max_length=10)),
            ],
        ),
    ]
