# Generated by Django 3.2.3 on 2021-05-18 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='imgUrl',
            new_name='imgurl',
        ),
    ]
