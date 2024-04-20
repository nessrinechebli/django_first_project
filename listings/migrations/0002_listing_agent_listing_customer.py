# Generated by Django 5.0.3 on 2024-04-02 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acount', '0001_initial'),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acount.agentprofile'),
        ),
        migrations.AddField(
            model_name='listing',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acount.customerprofile'),
        ),
    ]
