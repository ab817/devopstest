# Generated by Django 5.0.6 on 2024-06-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='employee_images/'),
        ),
    ]
