# Generated by Django 3.2.10 on 2022-07-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issue_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Daily Issue'), (2, 'Weekly Issue'), (3, 'Monthly Issue')], default=2),
        ),
    ]
