# Generated by Django 2.2.5 on 2020-11-05 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('airplanes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airplanes',
            name='_departure',
            field=models.DateTimeField(default=''),
        ),
        migrations.AddField(
            model_name='airplanes',
            name='_return',
            field=models.DateField(default=''),
        ),
        migrations.AddField(
            model_name='airplanes',
            name='adult',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='airplanes',
            name='children',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='airplanes',
            name='destination',
            field=django_countries.fields.CountryField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='airplanes',
            name='flight_class',
            field=models.CharField(blank=True, choices=[('economy', 'Economy'), ('business', 'Business'), ('first class', 'First Class')], max_length=30),
        ),
        migrations.AddField(
            model_name='airplanes',
            name='flight_name',
            field=models.CharField(blank=True, choices=[('daehan', 'Daehan'), ('asiana', 'Asiana'), ('jeju', 'Jeju'), ('airforce', 'Airforce')], max_length=50),
        ),
        migrations.AddField(
            model_name='airplanes',
            name='starting_point',
            field=django_countries.fields.CountryField(default='', max_length=746, multiple=True),
        ),
        migrations.AddField(
            model_name='airplanes',
            name='take_time',
            field=models.TimeField(default=''),
        ),
        migrations.AddField(
            model_name='airplanes',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='airplanes',
            name='way',
            field=models.CharField(blank=True, choices=[('oneway', 'One Way'), ('roundtrip', 'Round Trip')], max_length=50),
        ),
    ]