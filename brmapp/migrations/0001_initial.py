# Generated by Django 3.0.5 on 2020-05-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('author', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
            ],
        ),
    ]
