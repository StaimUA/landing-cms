# Generated by Django 2.2 on 2019-04-18 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20190418_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=32)),
                ('photo', models.ImageField(upload_to='team')),
                ('text', models.TextField(default='', max_length=2048)),
                ('block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_list', to='web.Block')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]