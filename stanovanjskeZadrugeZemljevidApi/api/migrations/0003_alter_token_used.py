# Generated by Django 3.2.7 on 2021-09-30 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
