# Generated by Django 2.1.5 on 2019-02-18 22:26

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
