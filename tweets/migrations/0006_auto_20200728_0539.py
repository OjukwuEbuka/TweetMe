# Generated by Django 2.2 on 2020-07-28 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_tweet_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
