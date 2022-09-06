# Generated by Django 4.0.1 on 2022-09-06 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0009_alter_file_filedate_alter_item_itemdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='itemID',
        ),
        migrations.AddField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='fileDate',
            field=models.DateField(default=datetime.datetime(2022, 9, 6, 11, 35, 29, 908516), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemDate',
            field=models.DateField(default=datetime.datetime(2022, 9, 6, 11, 35, 29, 907516), verbose_name='Date'),
        ),
    ]