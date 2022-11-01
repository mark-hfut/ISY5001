# Generated by Django 4.1.2 on 2022-10-26 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Photos",
            fields=[
                ("imgId", models.AutoField(primary_key=True, serialize=False)),
                ("imgName", models.CharField(max_length=100)),
                ("imgSrc", models.CharField(max_length=100)),
                ("imgTags", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                ("UserId", models.AutoField(primary_key=True, serialize=False)),
                ("UserName", models.CharField(max_length=100)),
            ],
        ),
    ]