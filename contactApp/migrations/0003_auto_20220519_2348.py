# Generated by Django 2.2.4 on 2022-05-19 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0002_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='birth',
            field=models.DateField(default='2022-05-19', max_length=20, verbose_name='出生日期'),
        ),
    ]