# Generated by Django 5.0.3 on 2024-04-04 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_listing_city_alter_listing_main_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
