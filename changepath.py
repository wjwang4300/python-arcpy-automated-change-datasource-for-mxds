import arcpy, os

folderPath = r"G:\arcgisserver\service_files\maps_test"
for filename in os.listdir(folderPath):
    fullpath = os.path.join(folderPath, filename)
    if os.path.isfile(fullpath):
        basename, extension = os.path.splitext(fullpath)
        if extension.lower() == ".mxd":
            mxd = arcpy.mapping.MapDocument(fullpath)
            print fullpath
            print"@@@@"
           
            for lyr in arcpy.mapping.ListLayers(mxd):
                print lyr
                #print "#################################
                if lyr.supports("DATASOURCE"):
                    print lyr.workspacePath 
                    if lyr.workspacePath  == r"pathA.sde":
                        datapath= r"pathB.sde"
                        mxd.replaceWorkspaces(lyr.workspacePath,"SDE_WORKSPACE", datapath,"SDE_WORKSPACE")
                        print "data source has been changed to" + datapath
             
                    #print "done"
            mxd.save()
                #else:
                    #print"skip"
del mxd
print"done"
