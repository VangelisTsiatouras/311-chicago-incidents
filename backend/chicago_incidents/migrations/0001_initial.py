# Generated by Django 3.1.3 on 2020-11-13 15:09

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
                ('license_plate', models.CharField(blank=True, max_length=400, null=True)),
                ('vehicle_make_model', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_color', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'abandoned_vehicles',
            },
        ),
        migrations.CreateModel(
            name='AbandonedVehicleIncident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('days_of_report_as_parked', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'abandoned_vehicles_incidents',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('current_activity', models.CharField(blank=True, max_length=100, null=True)),
                ('most_recent_action', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'activities',
            },
        ),
        migrations.CreateModel(
            name='ActivityIncident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'activities_incidents',
            },
        ),
        migrations.CreateModel(
            name='Graffiti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('surface', models.CharField(blank=True, max_length=500, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'graffiti',
            },
        ),
        migrations.CreateModel(
            name='GraffitiIncident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'graffiti_incidents',
            },
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creation_date', models.DateTimeField()),
                ('status', models.CharField(
                    choices=[('OPEN', 'Open'), ('OPEN_DUP', 'Open - Dup'), ('COMPLETED', 'Completed'),
                             ('COMPLETED_DUP', 'Completed - Dup')], max_length=15)),
                ('completion_date', models.DateTimeField(blank=True, null=True)),
                ('service_request_number', models.CharField(max_length=20)),
                ('type_of_service_request', models.CharField(
                    choices=[('ABANDONED_VEHICLE', 'Abandoned Vehicle Complaint'),
                             ('ALLEY_LIGHTS_OUT', 'Alley Lights Out'),
                             ('GARBAGE_CART', 'Garbage Cart Black Maintenance/Replacement'),
                             ('GRAFFITI', 'Graffiti Removal'), ('POT_HOLE', 'Pothole in Street'),
                             ('RODENT_BAITING', 'Rodent Baiting/Rat Complaint'),
                             ('SANITATION_CODE', 'Sanitation Code Violation'),
                             ('STREET_LIGHTS_ALL_OUT', 'Street Lights - All/Out'),
                             ('STREET_LIGHT_ONE_OUT', 'Street Light Out'), ('TREE_DEBRIS', 'Tree Debris'),
                             ('TREE_TRIM', 'Tree Trim')], max_length=30)),
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
                'db_table': 'number_of_carts_and_potholes',
            },
        ),
        migrations.CreateModel(
            name='RodentBaitingPremises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number_of_premises_baited', models.IntegerField(blank=True, null=True)),
                ('number_of_premises_w_garbage', models.IntegerField(blank=True, null=True)),
                ('number_of_premises_w_rats', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rodent_baiting_premises',
            },
        ),
        migrations.CreateModel(
            name='SanitationCodeViolation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nature_of_code_violation', models.CharField(max_length=500, unique=True)),
            ],
            options={
                'db_table': 'sanitation_code_violations',
            },
        ),
        migrations.CreateModel(
            name='SanitationCodeViolationIncident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'sanitation_code_violations_incidents',
            },
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=500, unique=True)),
            ],
            options={
                'db_table': 'trees',
            },
        ),
        migrations.CreateModel(
            name='TreeIncident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('incident',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tree_incidents',
                                   to='chicago_incidents.incident')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tree_incidents',
                                           to='chicago_incidents.tree')),
            ],
            options={
                'db_table': 'tree_incidents',
            },
        ),
        migrations.AddIndex(
            model_name='tree',
            index=models.Index(fields=['location'], name='trees_locatio_ef3458_idx'),
        ),
        migrations.AddField(
            model_name='sanitationcodeviolationincident',
            name='incident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='sanitation_code_violations_incidents',
                                    to='chicago_incidents.incident'),
        ),
        migrations.AddField(
            model_name='sanitationcodeviolationincident',
            name='sanitation_code_violation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='sanitation_code_violations_incidents',
                                    to='chicago_incidents.sanitationcodeviolation'),
        ),
        migrations.AddIndex(
            model_name='sanitationcodeviolation',
            index=models.Index(fields=['nature_of_code_violation'], name='sanitation__nature__e953d2_idx'),
        ),
        migrations.AddField(
            model_name='rodentbaitingpremises',
            name='incident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rodent_baiting_premises',
                                    to='chicago_incidents.incident'),
        ),
        migrations.AddField(
            model_name='numberofcartsandpotholes',
            name='incident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='number_of_carts_and_potholes', to='chicago_incidents.incident'),
        ),
        migrations.AddIndex(
            model_name='incident',
            index=models.Index(fields=['creation_date', 'status', 'completion_date', 'service_request_number',
                                       'type_of_service_request', 'street_address'],
                               name='incidents_creatio_549343_idx'),
        ),
        migrations.AddField(
            model_name='graffitiincident',
            name='graffiti',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='graffiti_incidents',
                                    to='chicago_incidents.graffiti'),
        ),
        migrations.AddField(
            model_name='graffitiincident',
            name='incident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='graffiti_incidents',
                                    to='chicago_incidents.incident'),
        ),
        migrations.AddIndex(
            model_name='graffiti',
            index=models.Index(fields=['surface', 'location'], name='graffiti_surface_8d5940_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='graffiti',
            unique_together={('surface', 'location')},
        ),
        migrations.AddField(
            model_name='activityincident',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities_incidents',
                                    to='chicago_incidents.activity'),
        ),
        migrations.AddField(
            model_name='activityincident',
            name='incident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities_incidents',
                                    to='chicago_incidents.incident'),
        ),
        migrations.AddIndex(
            model_name='activity',
            index=models.Index(fields=['current_activity', 'most_recent_action'], name='activities_current_d696ca_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='activity',
            unique_together={('current_activity', 'most_recent_action')},
        ),
        migrations.AddField(
            model_name='abandonedvehicleincident',
            name='abandoned_vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='abandoned_vehicles_incidents',
                                    to='chicago_incidents.abandonedvehicle'),
        ),
        migrations.AddField(
            model_name='abandonedvehicleincident',
            name='incident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='abandoned_vehicles_incidents', to='chicago_incidents.incident'),
        ),
        migrations.AddIndex(
            model_name='abandonedvehicle',
            index=models.Index(fields=['license_plate', 'vehicle_make_model', 'vehicle_color'],
                               name='abandoned_v_license_0f0966_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='abandonedvehicle',
            unique_together={('license_plate', 'vehicle_make_model', 'vehicle_color')},
        ),
        migrations.AlterUniqueTogether(
            name='treeincident',
            unique_together={('tree', 'incident')},
        ),
        migrations.AlterUniqueTogether(
            name='sanitationcodeviolationincident',
            unique_together={('sanitation_code_violation', 'incident')},
        ),
        migrations.AlterUniqueTogether(
            name='rodentbaitingpremises',
            unique_together={
                ('number_of_premises_baited', 'number_of_premises_w_garbage', 'number_of_premises_w_rats', 'incident')},
        ),
        migrations.AlterUniqueTogether(
            name='numberofcartsandpotholes',
            unique_together={('number_of_elements', 'incident')},
        ),
        migrations.AlterUniqueTogether(
            name='graffitiincident',
            unique_together={('graffiti', 'incident')},
        ),
        migrations.AlterUniqueTogether(
            name='activityincident',
            unique_together={('activity', 'incident')},
        ),
        migrations.AlterUniqueTogether(
            name='abandonedvehicleincident',
            unique_together={('abandoned_vehicle', 'incident')},
        ),
    ]
