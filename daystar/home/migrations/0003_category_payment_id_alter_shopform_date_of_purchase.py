# Generated by Django 5.0.3 on 2024-05-20 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_shopform_date_of_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_payment_id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='shopform',
            name='Date_of_purchase',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 12, 22, 20, 266974, tzinfo=datetime.timezone.utc)),
        ),
    ]
