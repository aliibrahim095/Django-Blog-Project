# Generated by Django 3.2.3 on 2021-05-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='categories', to='posts.Category'),
        ),
    ]
