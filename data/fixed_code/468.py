import cadquery as cq
import math
from cadquery import exporters
# --- Parameters from JSON ---
plate_radius = 0.375 * 0.75
hole_radius = 0.0469 * 0.75
corner_radius = 0.0268 * 0.75
plate_thickness = 0.0313
hole_centers = [
    (0.0938 * 0.75, 0.1875 * 0.75),
    (0.0938 * 0.75, 0.5625 * 0.75),
    (0.6562 * 0.75, 0.1875 * 0.75)
]
# --- Create the base circular plate ---
plate = cq.Workplane("XY").circle(plate_radius).extrude(plate_thickness)
# --- Add the central hole ---
plate = plate.faces(">Z").workplane().circle(hole_radius).cutThruAll()
# --- Cut the corner holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().moveTo(center_x - plate_radius/2, center_y - plate_radius/2).circle(hole_radius).cutThruAll()
# --- Export to STL ---
# --- Export to STL ---
cq.exporters.export({result_var}, "output_468.stl"output_468.stl