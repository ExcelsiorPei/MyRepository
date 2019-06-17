# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 16:40:27 2019

@author: pcl
"""

import arcpy
arcpy.CheckOutExtension("spatial")
typeall = {'tif':'tif','img':'img'}
arcpy.env.workspace = arcpy.GetParameterAsText(0)
Inputfeature = arcpy.GetParameterAsText(1)
OutputFile = arcpy.GetParameterAsText(2)#输出的位置有问题
type1 = arcpy.GetParameterAsText(3)
type1 = typeall[type1]
rasters = arcpy.ListRasters('*',type1)
for raster in rasters:
    out = OutputFile+'/'+'clip_'+raster
    arcpy.gp.ExtractByMask_sa(raster,Inputfeature,out)
    arcpy.AddMessage(raster+'has done')