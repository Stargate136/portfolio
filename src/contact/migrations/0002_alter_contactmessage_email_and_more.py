# Generated by Django 4.2.5 on 2023-09-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(max_length=100, verbose_name='Sujet'),
        ),
    ]
