# Generated by Django 2.1.8 on 2019-11-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('street_name', models.CharField(blank=True, max_length=50, null=True)),
                ('suburb', models.CharField(blank=True, max_length=50, null=True)),
                ('postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('phone_number', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
