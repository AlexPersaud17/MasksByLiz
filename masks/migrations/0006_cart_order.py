# Generated by Django 2.2.15 on 2020-08-28 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masks', '0005_auto_20200828_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masks.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('orderitems', models.ManyToManyField(to='masks.Cart')),
            ],
        ),
    ]
