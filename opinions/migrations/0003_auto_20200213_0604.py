# Generated by Django 3.0.3 on 2020-02-13 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('opinions', '0002_opinion_owner'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='opinion',
            unique_together={('content_type', 'object_id')},
        ),
    ]