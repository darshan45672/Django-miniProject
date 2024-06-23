# Generated by Django 5.0.6 on 2024-06-23 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address1',
            new_name='shippingAddress1',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address2',
            new_name='shippingAddress2',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='city',
            new_name='shippingCity',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='country',
            new_name='shippingCountry',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='email',
            new_name='shippingEmail',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='fullName',
            new_name='shippingFullName',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='state',
            new_name='shippingState',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='zipcode',
            new_name='shippingZipcode',
        ),
    ]