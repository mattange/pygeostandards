#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains classes related to Regions, Subregions and Intermediate 
regions. This is to be used in conjunction with the countries, 
as each country is normally assigned a region (and possibly a 
subregion and intermediate region).

.. moduleauthor:: Matteo Angeloni <mattange@gmail.com>
"""
from pathlib import Path

from .baseitem import BaseItem
from .basecollection import BaseCollection
from .info import DATABASEDIR

class Region(BaseItem):
    _fieldnames = ['name','code']
    _prettyprintfields = _fieldnames
        
    
class RegionsCollection(BaseCollection):
    _data_class_base = Region

regions = RegionsCollection(Path(DATABASEDIR) / 'regions_golden.csv')
sub_regions = RegionsCollection(Path(DATABASEDIR) / 'sub_regions_golden.csv')
intermediate_regions = RegionsCollection(Path(DATABASEDIR) / 'intermediate_regions_golden.csv')