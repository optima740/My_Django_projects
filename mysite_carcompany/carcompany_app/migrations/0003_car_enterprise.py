# Generated by Django 3.0.4 on 2020-04-01 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carcompany_app', '0002_auto_20200401_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='enterprise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='carcompany_app.Enterprise'),
        ),
    ]