# Generated by Django 4.2.1 on 2023-05-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]