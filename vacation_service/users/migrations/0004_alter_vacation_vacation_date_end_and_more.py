# Generated by Django 4.2.6 on 2023-10-09 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_vacation_vacation_date_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='vacation_date_end',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Конец отпуска'),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='vacation_date_start',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Начало отпуска'),
        ),
    ]
