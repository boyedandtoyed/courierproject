# Generated by Django 3.1.7 on 2021-03-25 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_range', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('fullname', models.CharField(max_length=255)),
                ('contact1', models.CharField(max_length=255)),
                ('contact2', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=255)),
                ('shipping_address', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('delivered', 'DELIVERED'), ('return', 'Return')], max_length=50)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('weight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.weight')),
            ],
        ),
    ]
