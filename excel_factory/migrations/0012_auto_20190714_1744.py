# Generated by Django 2.2.3 on 2019-07-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_factory', '0011_ddcx'),
    ]

    operations = [
        migrations.AddField(
            model_name='cz',
            name='jhrq',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cz',
            name='jhyf',
            field=models.CharField(max_length=100, null=True),
        ),
    ]