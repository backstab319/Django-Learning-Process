# Generated by Django 2.2.6 on 2019-10-17 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Graphical', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calgraphicdata',
            name='data',
            field=models.TextField(max_length=10),
        ),
    ]
