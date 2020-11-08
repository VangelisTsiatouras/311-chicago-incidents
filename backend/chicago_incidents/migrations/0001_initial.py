# Generated by Django 3.1.3 on 2020-11-08 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbandonedVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('days_of_report_as_parked', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'abandoned_vehicles',
            },
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creation_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('OPEN_DUP', 'Open - Dup'), ('COMPLETED', 'Completed'), ('COMPLETED_DUP', 'Completed - Dup')], max_length=15)),
                ('completion_date', models.DateTimeField(blank=True, null=True)),
                ('service_request_number', models.CharField(max_length=20)),
                ('type_of_service_request', models.CharField(choices=[('ABANDONED_VEHICLE', 'Abandoned Vehicle Complaint'), ('ALLEY_LIGHT_OUT', 'Alley Light Out'), ('GARBAGE_CART', 'Garbage Cart Black Maintenance/Replacement'), ('GRAFFITI', 'Graffiti Removal'), ('POT_HOLE', 'Pothole in Street'), ('RODENT_BAITING', 'Rodent Baiting/Rat Complaint'), ('SANITATION_CODE', 'Sanitation Code Violation'), ('STREET_LIGHTS_ALL_OUT', 'Street Lights - All/Out'), ('STREET_LIGHT_ONE_OUT', 'Street Light Out'), ('TREE_DEBRIS', 'Tree Debris'), ('TREE_TRIM', 'Tree Trim')], max_length=30)),
                ('current_activity', models.CharField(blank=True, max_length=100, null=True)),
                ('most_recent_action', models.CharField(blank=True, max_length=100, null=True)),
                ('street_address', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('zip_codes', models.IntegerField(blank=True, null=True)),
                ('x_coordinate', models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True)),
                ('y_coordinate', models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True)),
                ('ward', models.IntegerField(blank=True, null=True)),
                ('wards', models.IntegerField(blank=True, null=True)),
                ('historical_wards_03_15', models.IntegerField(blank=True, null=True)),
                ('police_district', models.IntegerField(blank=True, null=True)),
                ('community_area', models.IntegerField(blank=True, null=True)),
                ('community_areas', models.IntegerField(blank=True, null=True)),
                ('ssa', models.IntegerField(blank=True, null=True)),
                ('census_tracts', models.IntegerField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True)),
                ('location', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'incidents',
            },
        ),
        migrations.CreateModel(
            name='NumberOfCartsAndPotholes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number_of_elements', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('license_plate', models.CharField(max_length=400)),
                ('vehicle_make_model', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_color', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'vehicles',
            },
        ),
        migrations.AddIndex(
            model_name='vehicle',
            index=models.Index(fields=['license_plate', 'vehicle_make_model', 'vehicle_color'], name='vehicles_license_d6efdf_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='vehicle',
            unique_together={('license_plate', 'vehicle_make_model', 'vehicle_color')},
        ),
        migrations.AddField(
            model_name='numberofcartsandpotholes',
            name='incident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='number_of_carts_and_potholes', to='chicago_incidents.incident'),
        ),
        migrations.AddIndex(
            model_name='incident',
            index=models.Index(fields=['creation_date', 'status', 'completion_date', 'service_request_number', 'type_of_service_request', 'street_address'], name='incidents_creatio_549343_idx'),
        ),
        migrations.AddField(
            model_name='abandonedvehicle',
            name='incident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abandoned_vehicles', to='chicago_incidents.incident'),
        ),
        migrations.AddField(
            model_name='abandonedvehicle',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abandoned_vehicles', to='chicago_incidents.vehicle'),
        ),
        migrations.AlterUniqueTogether(
            name='abandonedvehicle',
            unique_together={('vehicle', 'incident')},
        ),
    ]
