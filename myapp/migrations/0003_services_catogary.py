# Generated by Django 4.1.1 on 2022-10-04 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_catogary'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='catogary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.catogary'),
        ),
    ]
