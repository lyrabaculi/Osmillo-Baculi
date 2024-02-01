# Generated by Django 5.0 on 2024-01-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_donor_wig_wigrecipient_distributionhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('image1', models.ImageField(upload_to='donation_images/')),
                ('image2', models.ImageField(upload_to='donation_images/')),
                ('image3', models.ImageField(upload_to='donation_images/')),
            ],
        ),
    ]
