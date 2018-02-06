#!/usr/bin/python

import itertools
import os
import re

from abc import ABCMeta
from abc import abstractmethod

class LoadCommand(object):

    numInstances = 0
    attach_loc_dict = None
    attach_loc_dict_text = None
    html_content_type_re = None
    xml_content_type_re = None

    __metaclass__ = ABCMeta

    def __init__ (self, name, filename=None, debug=False):

        self.__command_name     = name
        self.__filename = filename
        self.__debug = debug

        LoadCommand.numInstances = LoadCommand.numInstances + 1

        if LoadCommand.numInstances == 1:
            print("\nInitialize data for LOAD COMMANDS\n")

            ATTACH_BASE_LOC = '/usr1/data/tcr_attachments'
            LoadCommand.attach_loc_dict = dict(itertools.chain(*[zip(
                dir_vec[2],
                [dir_vec[0] + '/' + filenam for filenam in dir_vec[2]]
                ) for dir_vec in os.walk(ATTACH_BASE_LOC)]))

            ATTACH_BASE_LOC_TEXT = '/usr1/data/tcr_attach_text'
            LoadCommand.attach_loc_dict_text = dict(itertools.chain(*[zip(
                dir_vec[2],
                [dir_vec[0] + '/' + filenam for filenam in dir_vec[2]]
                ) for dir_vec in os.walk(ATTACH_BASE_LOC_TEXT)]))

            LoadCommand.html_content_type_re = \
               re.compile(r'<META http-equiv=("|)Content-Type("|) content="text/html; charset=(?P<ctype>[^"]*)"')

            LoadCommand.xml_content_type_re = \
               re.compile(r'<?xml version=("|)1.0("|) encoding=("|)(?P<ctype>[^"?]*)("|)?>')

            self.__debug = False

    @abstractmethod
    def execute(self, filename):
        pass

    @staticmethod
    def getNumInstances():
        print("Number of instances created: ", LoadCommand.numInstances)
        return LoadCommand.numInstances

    @staticmethod
    def getHtmlContentTypeRE ():
        return LoadCommand.html_content_type_re

    @staticmethod
    def getXmlContentTypeRE ():
        return LoadCommand.xml_content_type_re

    @staticmethod
    def getAttachLocDict ():
        return LoadCommand.attach_loc_dict

    @staticmethod
    def getAttachLocDictText ():
        return LoadCommand.attach_loc_dict_text

    def getCommandName(self):
        return self.__command_name

    def getFilename(self):
        return self.__filename

    def getDebugFlag (self):
        return self.__debug

    def getFileType(self):

        """
        Returns the extension from a file name

        Given a file name with an extension, return just the extension

        Args:
           file_name: the full name of the file

        Returns:
            Everything after the last . or 'other' if there's no extension or the
            extension isn't recognized
        """

        try:
            extension = re.search(r"\.(\w+)$", self.__filename, re.I).group(1).lower()

        except AttributeError:
            extension = 'other'

        return extension if extension in load_file_types else 'other'
