# Generated by Django 2.0.3 on 2018-03-21 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_notes', '0003_auto_20180321_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(max_length=70, primary_key=True, serialize=False),
        ),
    ]
