# Generated by Django 3.1.7 on 2021-03-23 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0004_addvisitorsdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='addrolesdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Type here', max_length=30)),
            ],
        ),
    ]