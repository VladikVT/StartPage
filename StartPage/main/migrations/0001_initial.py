# Generated by Django 4.1.1 on 2022-09-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteName', models.CharField(max_length=50, verbose_name='Site Name')),
                ('url', models.TextField(verbose_name='Site URL')),
                ('nameClass', models.CharField(max_length=50, verbose_name='Name Class')),
                ('nameTag', models.CharField(max_length=50, verbose_name='Name Tag')),
                ('linkClass', models.CharField(max_length=50, verbose_name='Link Class')),
                ('linkTag', models.CharField(max_length=50, verbose_name='Link Tag')),
            ],
        ),
    ]