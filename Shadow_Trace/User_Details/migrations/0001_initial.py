# Generated by Django 5.0.8 on 2024-08-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=30)),
                ('First_Nmae', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]
