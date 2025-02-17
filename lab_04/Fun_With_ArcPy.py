import arcpy

arcpy.env.workspace = r"C:\Users\awall\OneDrive\Desktop\GISProgramming\topic\04"

#creating new geodatabase
folder_path = r"C:\Users\awall\OneDrive\Desktop\GISProgramming\topic\04"
gdb_name = "lab4.gdb"
gdb_path = folder_path + "\\" + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

#Make XY Layer
csv_path = r"C:\Users\awall\OneDrive\Desktop\GISProgramming\topic\04\garages.csv"
garage_layer_name = "Garage_Points"
garages = arcpy.MakeXYEventLayer_management(csv_path, "X", "Y", garage_layer_name)

#Saving layer into GDB
input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + "\\" + garage_layer_name

#Copy buiilding features from Campus GDB to Lab 4 GDB
campus = r"C:\Users\awall\OneDrive\Desktop\GISProgramming\topic\04\Campus.gdb"
buildings_campus = campus + "\Structures"
buildings = gdb_path + "\\" + "Buildings"

arcpy.Copy_management(buildings_campus,buildings)

# Re-Projecting
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + "\Garage_Points_reprojected", spatial_ref)

# Buffer Garages in meters
garageBuffered = arcpy.Buffer_analysis(gdb_path + "\Garage_Points_reprojected", gdb_path + "\Garage_Points_buffered", 150)

# Intersect buffer with the buildings
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + "\Garage_Building_Intersection", "ALL")
arcpy.TableToTable_conversion(gdb_path + "\Garage_Building_Intersection.dbf", r"C:\Users\awall\OneDrive\Desktop\GISProgramming\topic\04", "nearbyBuildings.csv")
