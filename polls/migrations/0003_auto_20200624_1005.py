# Generated by Django 3.0.2 on 2020-06-24 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200624_0903'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Qs', 'verbose_name_plural': 'Qs'},
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=100, null=True, verbose_name='답'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='질'),
        ),
        migrations.AlterModelTable(
            name='question',
            table='questions',
        ),
    ]
