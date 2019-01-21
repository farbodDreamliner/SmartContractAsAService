# Generated by Django 2.0.7 on 2019-01-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('family', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phoneNumber', models.DecimalField(decimal_places=0, max_digits=11)),
            ],
        ),
    ]