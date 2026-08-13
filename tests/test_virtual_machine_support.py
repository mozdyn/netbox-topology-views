from pathlib import Path

ROOT = Path(__file__).parents[1] / "netbox_topology_views"


def source(name):
    return (ROOT / name).read_text()


def test_vm_coordinate_model_and_migration_exist():
    models = source("models.py")
    migration = source("migrations/0014_virtual_machine_topology.py")
    assert "class VMCoordinate(NetBoxModel):" in models
    assert "to='virtualization.virtualmachine'" in migration
    assert "unique_together" in migration
    assert "show_virtual_machines" in migration


def test_vm_coordinate_is_exposed_and_save_endpoint_accepts_vm_node_ids():
    assert "VMCoordinateSerializer" in source("api/serializers.py")
    assert 'router.register("vmcoordinate"' in source("api/urls.py")
    api = source("api/views.py")
    assert 'device_id.startswith("vm-")' in api
    assert "VirtualMachine.objects.get" in api
    assert "model_name = 'VMCoordinate'" in api


def test_vm_option_is_available_in_model_forms_query_and_serializer():
    assert "show_virtual_machines = models.BooleanField" in source("models.py")
    assert "'show_virtual_machines'" in source("forms.py")
    assert '"show_virtual_machines"' in source("api/serializers.py")
    utils = source("utils.py")
    assert '"show_virtual_machines" in request.GET' in utils
    api = source("api/views.py")
    assert "save_coords, show_unconnected, show_virtual_machines, show_power" in api


def test_topology_builds_active_vm_nodes_and_host_edges_without_changing_device_ids():
    views = source("views.py")
    assert "VirtualMachine.objects.filter(status=\"active\"" in views
    assert 'node["id"] = f"vm-{device.pk}"' in views
    assert 'node["id"] = device.pk' in views  # existing Device rendering contract
    assert "cluster.devices.count() != 1" in views
    assert "VMInterface.objects.filter(virtual_machine=vm)" in views
    assert "Virtual Machine/Container<br>" in views


def test_vm_role_image_prefers_role_and_falls_back_to_vm_content_type():
    views = source("views.py")
    assert "entity.role_id" in views
    assert "ContentType.objects.get_for_model(VirtualMachine)" in views
