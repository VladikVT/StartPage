# Generated by Django 4.1.1 on 2022-09-28 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_favsite_priority_newssite_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bgURL', models.TextField(verbose_name='BackGround URL')),
            ],
        ),
    ]
