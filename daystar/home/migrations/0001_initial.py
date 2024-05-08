# Generated by Django 5.0.3 on 2024-05-08 11:51

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='B_departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=200)),
                ('person_taking_baby', models.CharField(max_length=200)),
                ('telephone_no', models.CharField(max_length=200)),
                ('timeout', models.DateTimeField()),
                ('babyno', models.IntegerField(default=0)),
                ('comments', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Category_doll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categorystay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sarrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=200)),
                ('timein', models.TimeField(default=django.utils.timezone.now)),
                ('sittersno', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Sitter_arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sittersform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=200)),
                ('age', models.CharField(default=0, max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('next_of_kin', models.CharField(max_length=200)),
                ('level_of_education', models.CharField(max_length=50)),
                ('nin', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField(default=0, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(default='Ugx', max_length=10)),
                ('Payno', models.CharField(default=0, max_length=200)),
                ('currency', models.CharField(default='Ugx', max_length=10)),
                ('c_payment_id', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='home.categorystay')),
            ],
        ),
        migrations.CreateModel(
            name='Babesform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=200)),
                ('age', models.CharField(default=0, max_length=200)),
                ('gender', models.CharField(max_length=100)),
                ('location', models.CharField(default=None, max_length=50, null=True)),
                ('sponsor', models.CharField(max_length=200)),
                ('date', models.DateField(default=0, max_length=200)),
                ('parentsname', models.CharField(max_length=200)),
                ('babysno', models.CharField(default=0, max_length=200)),
                ('timein', models.DateTimeField()),
                ('person_bringing_baby', models.CharField(max_length=200)),
                ('c_stay', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='home.categorystay')),
            ],
        ),
        migrations.CreateModel(
            name='Doll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_doll', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('doll_type', models.CharField(blank=True, max_length=200, null=True)),
                ('issued_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('received_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('Unit_price', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('c_doll', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.category_doll')),
            ],
        ),
        migrations.CreateModel(
            name='Salesrecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_sold', models.IntegerField(default=0)),
                ('amount_received', models.IntegerField(default=0)),
                ('sale_date', models.DateField(default=django.utils.timezone.now)),
                ('unit_price', models.IntegerField(default=0)),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.doll')),
                ('payee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.babesform')),
            ],
        ),
        migrations.CreateModel(
            name='Sitterpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(default=3000, max_length=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('numbers_of_babies_attended_to', models.IntegerField(default=0)),
                ('sitter_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sitter_arrival')),
            ],
        ),
    ]
