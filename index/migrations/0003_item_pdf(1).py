# Generated by Django 3.0.1 on 2020-01-11 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20200111_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pdf',
            field=models.FileField(default='null', upload_to='items/pdfs/'),
        ),
    ]
