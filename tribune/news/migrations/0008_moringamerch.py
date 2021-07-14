# Generated by Django 3.1.7 on 2021-07-13 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20210708_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoringaMerch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
