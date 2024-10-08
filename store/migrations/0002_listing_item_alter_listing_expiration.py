# Generated by Django 5.1 on 2024-09-09 02:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Listings', to='store.item'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Expiration',
            field=models.DateTimeField(),
        ),
    ]
