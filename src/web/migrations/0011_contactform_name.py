# Generated by Django 2.2 on 2019-06-06 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='name',
            field=models.CharField(default='', max_length=32),
        ),
    ]
