# Generated by Django 4.2.3 on 2023-08-08 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_active',
            field=models.TextField(choices=[('A', 'Yes'), ('B', 'No')], default='A', max_length=100),
        ),
    ]
