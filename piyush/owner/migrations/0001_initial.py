# Generated by Django 4.2 on 2024-09-07 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owenr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Oname', models.CharField(max_length=100)),
                ('Oemail', models.CharField(max_length=100)),
                ('Ophone', models.CharField(max_length=12)),
                ('Opassword', models.CharField(max_length=100)),
            ],
        ),
    ]
