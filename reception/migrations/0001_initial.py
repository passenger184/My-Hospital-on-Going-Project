# Generated by Django 3.2.7 on 2021-09-15 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(null=True)),
                ('contact_number', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=200)),
                ('blood_group', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('any_major_disease', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
