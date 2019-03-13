# Generated by Django 2.1.5 on 2019-02-25 02:43

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('week', '0008_remove_modelindexpage_vertical_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelindexpage',
            name='announcements',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='modelindexpage',
            name='vertical_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='modelindexpage',
            name='vertical_url',
            field=models.URLField(blank=True),
        ),
    ]