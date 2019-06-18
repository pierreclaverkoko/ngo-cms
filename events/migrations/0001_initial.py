# Generated by Django 2.1.4 on 2019-03-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('short_desc', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_details', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='%Y/%m/%d')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=65, unique=True)),
            ],
            options={
                'db_table': 'eventapp_event',
            },
        ),
    ]