# Generated by Django 2.2.3 on 2019-07-14 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_factory', '0010_auto_20190712_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ddcx',
            fields=[
                ('ddh', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ddid', models.CharField(max_length=100, null=True)),
                ('essddh', models.CharField(max_length=100, null=True)),
                ('ddrq', models.CharField(max_length=100, null=True)),
                ('ddrq2', models.CharField(max_length=100, null=True)),
                ('ddyf', models.CharField(max_length=100, null=True)),
                ('ddzt', models.CharField(max_length=100, null=True)),
                ('sf', models.CharField(max_length=100, null=True)),
                ('ds', models.CharField(max_length=100, null=True)),
                ('splx', models.CharField(max_length=100, null=True)),
                ('spmc', models.CharField(max_length=100, null=True)),
                ('tcmc', models.CharField(max_length=100, null=True)),
                ('dghm', models.CharField(max_length=100, null=True)),
                ('zdpp', models.CharField(max_length=100, null=True)),
                ('zdxh', models.CharField(max_length=100, null=True)),
                ('zdys', models.CharField(max_length=100, null=True)),
                ('hdlx', models.CharField(max_length=100, null=True)),
                ('kxb', models.CharField(max_length=100, null=True)),
                ('scss', models.CharField(max_length=100, null=True)),
                ('zfzt', models.CharField(max_length=100, null=True)),
                ('zffs', models.CharField(max_length=100, null=True)),
                ('khxm', models.CharField(max_length=100, null=True)),
                ('zjlx', models.CharField(max_length=100, null=True)),
                ('zjhm', models.CharField(max_length=100, null=True)),
                ('lxr', models.CharField(max_length=100, null=True)),
                ('lxrdh', models.CharField(max_length=100, null=True)),
                ('qtlxrdh', models.CharField(max_length=100, null=True)),
                ('psdz', models.CharField(max_length=100, null=True)),
                ('khbz', models.CharField(max_length=100, null=True)),
                ('qylx', models.CharField(max_length=100, null=True)),
                ('qymx', models.CharField(max_length=100, null=True)),
                ('fzrxm', models.CharField(max_length=100, null=True)),
                ('fzrbm', models.CharField(max_length=100, null=True)),
                ('gsqd', models.CharField(max_length=100, null=True)),
                ('qdly', models.CharField(max_length=100, null=True)),
                ('yhlx', models.CharField(max_length=100, null=True)),
                ('smzjhzt', models.CharField(max_length=100, null=True)),
                ('hkjhzt', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]