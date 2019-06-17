# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 16:40:27 2019

@author: pcl
"""

import arcpy
arcpy.CheckOutExtension("spatial")#使用浮动版许可时，脚本检索到扩展模块许可后，即可使用扩展模块工具。
typeall = {'tif':'tif','img':'img'}#生成的文件的可选的格式
arcpy.env.workspace = arcpy.GetParameterAsText(0)#对话框第一个参数，设置工作空间，即待裁剪影像所在文件夹
Inputfeature = arcpy.GetParameterAsText(1)#用于裁剪的矢量文件
OutputFile = arcpy.GetParameterAsText(2)#裁剪结果保存的文件夹
type1 = arcpy.GetParameterAsText(3)#裁剪结果的格式
type1 = typeall[type1]#同上
rasters = arcpy.ListRasters('*',type1)
for raster in rasters:
    out = OutputFile+'/'+'clip_'+raster
    arcpy.gp.ExtractByMask_sa(raster,Inputfeature,out)#裁剪影像的函数ExtractByMask_sa
    arcpy.AddMessage(raster+'has done')#向脚本工具或 Python 工具箱工具的消息中添加自定义信息性消息