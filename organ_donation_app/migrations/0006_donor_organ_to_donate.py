# Generated by Django 5.0.3 on 2024-03-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organ_donation_app', '0005_remove_donor_organ_to_donate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='organ_to_donate',
            field=models.CharField(default='Kidney', max_length=10),
        ),
    ]