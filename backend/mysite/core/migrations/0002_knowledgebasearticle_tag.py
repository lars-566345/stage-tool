# Generated by Django 5.2 on 2025-06-04 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledgebasearticle',
            name='tag',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
