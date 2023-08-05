#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
  ████
██    ██   Datature
  ██  ██   Powering Breakthrough AI
    ██

@File    :   base_processor.py
@Author  :   Raighne.Weng
@Version :   0.7.3
@Contact :   raighne@datature.io
@License :   Apache License 2.0
@Desc    :   Base Processor module
'''

from abc import ABC, abstractmethod


class BaseProcessor(ABC):
    """Base processor class"""

    @abstractmethod
    def valid(self, request_data):
        """Valid the input file if a valid file"""

    @abstractmethod
    def process(self, request_data):
        """Function to process input file to assets"""
