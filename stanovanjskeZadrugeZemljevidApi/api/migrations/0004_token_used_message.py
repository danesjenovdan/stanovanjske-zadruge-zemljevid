# Generated by Django 3.2.7 on 2021-09-30 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_token_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='used_message',
            field=models.BooleanField(default=False),
        ),
    ]
