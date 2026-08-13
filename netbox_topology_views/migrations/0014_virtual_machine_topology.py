from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('netbox_topology_views', '0013_individualoptions_draw_cable_labels'),
        ('virtualization', '0001_initial'),
    ]
    operations = [
        migrations.AddField(model_name='individualoptions', name='show_virtual_machines', field=models.BooleanField(default=False)),
        migrations.CreateModel(
            name='VMCoordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=None)),
                ('x', models.IntegerField()), ('y', models.IntegerField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='virtualization.virtualmachine')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netbox_topology_views.coordinategroup')),
            ], options={'ordering': ['group', 'device'], 'unique_together': {('device', 'group')}},
        ),
    ]
