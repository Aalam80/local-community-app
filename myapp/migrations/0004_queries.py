# Generated by Django 4.1.1 on 2022-10-05 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_services_catogary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Query_detail', models.TextField()),
                ('Query_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.services')),
            ],
        ),
    ]
