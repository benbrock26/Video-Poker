#!/usr/bin/python

from LoadCommand import LoadCommand

class LoadTextOtherCommand(LoadCommand):

    def __init__ (self, filename):

        LoadCommand.__init__(self, 
                             "LOAD_TEXT_OTHER_COMMAND", 
                             filename)

    def execute (self):

        """
        Extracts text from files we don't otherwise know how to handle

        Reads an input file and extracts whatever text it can.
        For the moment, returns nothing assuming we can't actually read the file

        Args:
           file: an open file object

        Returns:
           A pair, an empty string and a 0 (signifying no document read)
        """

        print ('Command Name = "%s"' % self.getCommandName())

        return ('', 0)
