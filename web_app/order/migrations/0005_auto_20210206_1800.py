# Generated by Django 3.1.5 on 2021-02-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210206_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-modify_dt',)},
        ),
        migrations.AddField(
            model_name='order',
            name='Order_set',
            field=models.IntegerField(default=0),
        ),
    ]