# Generated by Django 3.0.2 on 2020-06-24 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200624_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=100, verbose_name='답'),
        ),
    ]
