# Generated by Django 4.1.3 on 2024-04-23 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Full_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('Ph_number', models.CharField(blank=True, max_length=15, null=True)),
                ('Aadhar_number', models.CharField(max_length=12, unique=True)),
                ('Address', models.TextField(blank=True, null=True)),
                ('state', models.CharField(blank=True, choices=[('TN', 'Tamil Nadu'), ('KL', 'Kerala'), ('AP', 'Andhra Pradesh'), ('MH', 'Maharashtra'), ('DL', 'Delhi')], max_length=20, null=True)),
                ('Language', models.CharField(blank=True, choices=[('TA', 'Tamil'), ('TE', 'Telugu'), ('ML', 'Malayalam'), ('HI', 'Hindi')], max_length=2, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
