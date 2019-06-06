# Generated by Django 2.2 on 2019-06-06 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_remove_contactform_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='comment',
            field=models.TextField(default='', help_text='Your comments', max_length=2048),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.EmailField(help_text='Your E-mail', max_length=254),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='full_name',
            field=models.CharField(help_text='Your Full name', max_length=100),
        ),
    ]
