# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 21:37:00 2019

@author: ExcelsiorPei
"""

from arcgis.gis import GIS
#登录arcgis online账户
gis = GIS("https://www.arcgis.com", username="username", password="password")
#存储shapefile元数据
chanba_properties = {'title':'chanba_sample2',
                     'tags':'rivers,chemical_index',
                     'type':'Shapefile'}
#shapefile路径
data_path = r"G:\mydata\Xian\chanba_sample.zip"
#将数据作为要素加载为要素图层
shp = gis.content.add(chanba_properties,data=data_path)
#调用的publish方法发布Shapefile
shp.publish()