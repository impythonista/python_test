# Generated by Django 2.1.8 on 2019-11-26 14:31

from django.db import migrations, models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contact_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Contact Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=70, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Client Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='client',
            name='postcode',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Postcode'),
        ),
        migrations.AlterField(
            model_name='client',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='client',
            name='street_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Street Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='suburb',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Suburb'),
        ),
    ]
