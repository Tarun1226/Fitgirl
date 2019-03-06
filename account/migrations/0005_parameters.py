# Generated by Django 2.1.5 on 2019-02-25 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190218_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_days_to_done', models.IntegerField(default=1)),
                ('nutrition_days_to_done', models.IntegerField(default=1)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('current_values', models.BooleanField(default=True)),
            ],
        ),
    ]