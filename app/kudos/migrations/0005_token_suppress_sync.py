# Generated by Django 2.1.7 on 2019-04-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kudos', '0004_token_preview_img_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='suppress_sync',
            field=models.BooleanField(default=False),
        ),
    ]
