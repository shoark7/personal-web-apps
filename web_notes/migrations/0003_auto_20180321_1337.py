# Generated by Django 2.0.3 on 2018-03-21 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_notes', '0002_auto_20180321_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]