import bpy

# Get active object
obj = bpy.context.active_object

if obj and obj.type == 'GREASEPENCIL':
    gp = obj.data

    # Replace with your layer name or loop through all layers
    layer = gp.layers.get("Layer") # use correct layer name here

    if layer:
        stroke_count = 0

        for frame_number, frame in layer.frames.items():
            drawing = frame.drawing
            if drawing is not None:
                stroke_count += len(drawing.strokes)

        print(f"Total strokes in layer '{layer.name}': {stroke_count}")
    else:
        print("Layer not found.")
else:
    print("Active object is not a Grease Pencil (v3) object.")
