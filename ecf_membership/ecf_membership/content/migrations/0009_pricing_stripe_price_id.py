# Generated by Django 3.1.7 on 2021-03-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_pricing_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='stripe_price_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
