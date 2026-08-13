# Native VirtualMachine topology support

Topology Views can render NetBox `virtualization.VirtualMachine` objects without duplicating them as DCIM devices.

## Usage

Enable **Show Virtual Machines** in the topology filter or in Individual Options. The topology includes active VMs only when their cluster has exactly one host in `cluster.devices` and that host is in the selected device result set.

VM nodes use the stable `vm-<pk>` identifier and link to the native VM detail page. A dashed host-to-VM edge identifies the relationship as **Virtual Machine/Container** and lists the VM's `VMInterface` names. Existing Device nodes and tooltips are unchanged.

## Images

A VM first uses the existing `RoleImage` assigned to its VM-capable `DeviceRole`. If none exists, the renderer checks the `VirtualMachine` content-type image and then falls back to the role slug image.

## Coordinates and API

VM positions are stored in `VMCoordinate`, independently from Device `Coordinate`, and are unique per VM and coordinate group. Drag-save accepts node IDs in the form `vm-<pk>`. CRUD is exposed at the plugin API's `vmcoordinate` endpoint. Run plugin migrations after upgrading.

## Compatibility

The implementation targets NetBox 4.6.7 and retains the 4.5.1 plugin's existing Device rendering behavior.
