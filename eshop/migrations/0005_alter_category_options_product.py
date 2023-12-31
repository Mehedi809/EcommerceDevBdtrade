# Generated by Django 4.2.6 on 2023-10-14 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0004_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='Product')),
                ('description', models.TextField(max_length=5000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]
