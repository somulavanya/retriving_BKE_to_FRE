# Generated by Django 4.2.6 on 2024-08-30 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('flight_number', models.IntegerField(primary_key=True, serialize=False)),
                ('airline_name', models.CharField(max_length=50)),
                ('No_of_seats_available', models.IntegerField()),
                ('source', models.CharField(max_length=50)),
                ('source_code', models.CharField(max_length=5)),
                ('destination', models.CharField(max_length=100)),
                ('destination_code', models.CharField(max_length=5)),
                ('arraival_time', models.DateTimeField()),
                ('depature_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='passenger',
            fields=[
                ('pnr', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=7)),
                ('nationality', models.CharField(max_length=10)),
                ('checkin_status', models.BooleanField(default=0)),
                ('cleared_security_status', models.IntegerField(default=0)),
                ('flight_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.flights')),
            ],
        ),
        migrations.DeleteModel(
            name='Display_Flights',
        ),
    ]
