# Generated by Django 4.2.5 on 2023-09-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_alter_cv_personal_info_alter_cv_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='display_order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
