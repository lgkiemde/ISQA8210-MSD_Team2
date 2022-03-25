# Generated by Django 4.0.3 on 2022-03-24 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=5)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('referred_by', models.CharField(max_length=1000)),
                ('reffered_to', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UPScode', models.CharField(max_length=15)),
                ('item_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_note', models.CharField(max_length=2000)),
                ('date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.client')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_quantity', models.IntegerField()),
                ('delivered_quantity', models.IntegerField()),
                ('UPScode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_UPScode', to='account.inventory')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.client')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.visit')),
                ('item_description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_item_description', to='account.inventory')),
            ],
        ),
    ]
