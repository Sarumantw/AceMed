# Generated by Django 5.1.5 on 2025-01-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.CharField(default='not_defined', max_length=200),
            preserve_default=False,
        ),
    ]
