# Generated by Django 2.2.5 on 2019-10-06 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191006_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sliderpos',
            field=models.IntegerField(choices=[(0, 'First'), (2, 'None'), (1, 'Other')], default=2),
        ),
    ]
