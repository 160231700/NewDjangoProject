# Generated by Django 4.2.19 on 2025-02-25 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_ticket_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
