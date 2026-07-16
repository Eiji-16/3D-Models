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
