#!/usr/bin/python

import subprocess

from LoadCommand import LoadCommand

class LoadTextPdfCommand(LoadCommand):

    def __init__ (self, filename):

        LoadCommand.__init__(self, 
                             "LOAD_TEXT_PDF_COMMAND", 
                             filename)

    def execute (self):

        """
        Extracts text from input open PDF file

        Reads an input PDF and returns just the display text found, in no
        particular order. Note that depending on the format of the input
        file, words may be split in funny ways. PDFs can be created in
        pathological ways which could confuse the interpreter. Also note
        that images will not be interpreted.

        Args:
           file: an open PDF file object

        Returns:
            A pair, the text extracted from the PDF and 1 (signifying one document read)
        """

        print ('Command Name = "%s"' % self.getCommandName())

        return (subprocess.check_output(['pdftotext', '-', '-'],
                                        stdin=file).decode('utf8'), 1)

