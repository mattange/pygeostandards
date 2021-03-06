#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 23:18:18 2018

"""
import threading
import logging
import csv
import codecs
from pkg_resources import resource_stream

from .info import DATADIR
from .utils import lazy_load
from .baseitem import BaseItem

logger = logging.getLogger('BaseCollection')

class BaseCollection():
    
    _data_class_base = BaseItem
    _no_index = []
    
    def __init__(self, string_or_list):
        if isinstance(string_or_list, str):
            #assume we need loading from csv files
            self._stream = DATADIR + "/" + string_or_list
            self._is_loaded = False
        else:
            #assume it's a list that we can attach to object directly
            self._stream = None
            self._is_loaded = True
            self.objects = string_or_list
            self.index_names = set()
            self.indices = {}
            for obj in self.objects:
                self._addtoindex(obj)
            
        self._load_lock = threading.Lock()
            
    def force_load(self):
        self._load()
    
    def _load(self):
        if self._is_loaded:
            # Help keeping the _load_if_needed code easier
            # to read.
            return

        self.objects = []
        self.index_names = set()
        self.indices = {}
        
        io = resource_stream(__name__, self._stream)
        utf8_reader = codecs.getreader('utf-8')
        reader = csv.DictReader(utf8_reader(io), fieldnames=self._data_class_base.fieldnames(), delimiter=",")
        next(reader)
        for entry in reader:
            obj = self._data_class_base(**entry)
            self.objects.append(obj)
            self._addtoindex(obj)

        self._is_loaded = True          

    def _addtoindex(self, obj):
        entry = obj.fields
        for key, value in entry.items():
            if key in self._no_index:
                continue
            index = self.indices.setdefault(key, {})
            if value in index:
                logger.debug(
                    '%s %r already taken in index %r and will be '
                    'ignored. This is an error in the databases.' %
                    (self._data_class_base.__name__, value, key))
            index[value] = obj
        
    @lazy_load
    def __getitem__(self, idx):
        return self.objects[idx]
    
    @lazy_load
    def __iter__(self):
        return iter(self.objects)

    @lazy_load
    def __len__(self):
        return len(self.objects)

    @lazy_load
    def get(self, **kw):
        if len(kw) != 1:
            raise TypeError('Only one criteria may be given')
        field, value = kw.popitem()
        return self.indices[field][value]
    
    @lazy_load
    def to_csv(self, filename):
        with open(filename, 'wt') as f:
            csvwriter = csv.writer(f, delimiter=',')
            csvwriter.writerow(self._data_class_base.fieldnames())
            csvwriter.writerows([o.fields.values() for o in self.objects])
            
    @classmethod
    def fieldnames(cls):
        return cls._data_class_base.fieldnames()
