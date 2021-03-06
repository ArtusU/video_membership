# Generated by Django 3.1.7 on 2021-03-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_course_pricing_tiers'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='currency',
            field=models.CharField(default='gbp', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pricing',
            name='price',
            field=models.DecimalField(decimal_places=2, default='5', max_digits=5),
            preserve_default=False,
        ),
    ]
