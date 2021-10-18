# -*- coding: utf-8 -*-

import arcpy, string
import datetime
import os
import sys
import math

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [NDTI]


class NDTI(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "NDTI"
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

        param1 = arcpy.Parameter(
            displayName="Green",
            name="Green",
            datatype="GPRasterLayer",
            parameterType="Required",
            direction="Input")
        
        #Two parameter
        param2 = arcpy.Parameter(
            displayName="Save_Folder",
            name="folder_fields",
            datatype=["Folder", "DERasterDataset"],
            parameterType="Required",
            direction="Output")

        params = [param0, param1, param2]
        
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        Red = parameters[0].valueAsText
        Green = parameters[1].valueAsText
        Save_Folder = parameters[2].valueAsText
        # To allow overwriting outputs change overwriteOutput option to True.
        arcpy.env.overwriteOutput = True

        # Check out any necessary licenses.
        arcpy.CheckOutExtension("spatial")
        arcpy.CheckOutExtension("ImageAnalyst")


        with arcpy.EnvManager(scratchWorkspace=r"[YOUR PATH]", workspace=r"[YOUR PATH]"):
            out_rc_minus_raster = arcpy.sa.RasterCalculator(([Red,Green]), ["x","y"], "(x-y)/(x+y)")
            out_rc_minus_raster.save(Save_Folder)

        return
        