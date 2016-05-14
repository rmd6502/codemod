#!/usr/bin/env python

# Copyright (c) 2007-2008 Facebook

from subprocess import Popen, PIPE
import re
from os import path


class MercurialUtil(object):
    """
    Searches a directory hierarchy using hg grep
    """

    def walk_directory(self, root_directory, match_pattern):
        """
        Uses hg grep to find all files containing a particular pattern.

        >>> util = MercurialUtil()
        >>> util.walk_directory(".","try:")
        []

        Note that this test fails because we're a git repo.
        """
        hgPipe = Popen(['hg', 'grep', '-l', match_pattern],
                       stdout=PIPE, cwd=root_directory)
        filelist = map(lambda name: path.join(root_directory, name),
                       re.split('\n+', hgPipe.communicate()[0]))

        filelist.pop()
        return filelist

    @staticmethod
    def isValid():
        return True
