# Generated by Django 5.0.7 on 2024-07-18 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olcha', '0003_attribute_attributevalue_productattribute'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='field',
            new_name='file',
        ),
    ]
