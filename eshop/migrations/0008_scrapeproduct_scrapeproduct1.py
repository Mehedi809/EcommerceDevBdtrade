# Generated by Django 4.2.6 on 2023-10-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0007_cartproduct_orderedproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapeProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ScrapeProduct1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
            ],
        ),
    ]