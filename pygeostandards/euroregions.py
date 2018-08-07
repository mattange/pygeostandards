#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains classes related to European Union / Eurozone 
/ Euroarea subdivisions.

.. moduleauthor:: Matteo Angeloni <mattange@gmail.com>
"""
from pathlib import Path

from .baseitem import BaseItem
from .basecollection import BaseCollection
from .info import DATABASEDIR

class EuroRegion(BaseItem):
    _fieldnames = ['alpha_code', 'name']
    
class EuroRegionCollection(BaseCollection):
    _data_class_base = EuroRegion

euroregions = EuroRegionCollection(Path(DATABASEDIR) / 'euroregions_golden.csv')
