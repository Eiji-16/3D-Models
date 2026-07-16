	bpy.ops.object.editmode_toggle()
	bpy.ops.object.editmode_toggle()
	bpy.context. = True
	bpy.context. = False
	bpy.context. = True
	bpy.context. = False
	bpy.context. = True
	bpy.context. = False
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Case']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Case']
	bpy.context. = False
	bpy.ops.object.editmode_toggle()
	bpy.context.object.active_material_index = 0
	bpy.context. = False
	bpy.context. = False
	bpy.context. = False
	bpy.context. = True
	bpy.context. = False
	bpy.context. = True
	bpy.ops.object.editmode_toggle()
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Caps']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Caps']
	bpy.ops.transform.translate(value=(-0.0179335, -0.00367866, -0.0109045), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SPHERE', proportional_size=9.84974, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
