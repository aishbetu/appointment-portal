# Generated by Django 3.1.7 on 2021-04-19 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCare_app', '0002_auto_20210420_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caraouseldata',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='caraouseldata',
            name='image',
            field=models.ImageField(default=True, upload_to='Carousel'),
        ),
    ]