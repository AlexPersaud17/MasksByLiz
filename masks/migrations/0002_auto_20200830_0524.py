# Generated by Django 2.2.15 on 2020-08-30 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]