import arcpy
import datetime
import os
import sys
import math
from arcpy.sa import *

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [TSS]


class TSS(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        #Define parameter definitions

        # First parameter
        param0 = arcpy.Parameter(
            displayName="Red",
            name="Red",
            datatype="GPRasterLayer",
            parameterType="Required",
            direction="Input")
        
        #Two parameter
        param1 = arcpy.Parameter(
            displayName="Save_Folder",
            name="folder_fields",
            datatype=["Folder", "DERasterDataset"],
            parameterType="Required",
            direction="Output")

        params = [param0, param1]
        
        return params

    def execute(self, parameters, messages):
        """The source code of the tool."""
        Red = parameters[0].valueAsText
        Save_Folder = parameters[1].valueAsText
        # To allow overwriting outputs change overwriteOutput option to True.
        arcpy.env.overwriteOutput = True

        # Check out any necessary licenses.
        arcpy.CheckOutExtension("spatial")
        arcpy.CheckOutExtension("ImageAnalyst")

        a = float(str(3.3238))
        b = float(str(2.71))
        c = float(str(34.099))


        with arcpy.EnvManager(scratchWorkspace=r"[YOUR PATH]", workspace=r"[YOUR PATH]"):
            out_rc_minus_raster = arcpy.sa.RasterCalculator(([Red]), ["x","a","b ","c"], ("a*b*(c*x)"))
            out_rc_minus_raster.save(Save_Folder)

        return