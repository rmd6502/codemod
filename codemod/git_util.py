#!/usr/bin/env python

# Copyright (c) 2007-2008 Facebook

from subprocess import Popen,PIPE
import re
from os import path

class GitUtil(object):
    """
    Searches a directory hierarchy using OS/X spotlight.
    """

    def walk_directory(self, root_directory, match_pattern):
        """
        Uses git grep to find all files containing a particular pattern

        >>> util = GitUtil()
        >>> util.walk_directory(".","try:")
        [ "base.py", "setup.py", "spotlight_util.py" ]
        """
        gitPipe = Popen(['git', 'grep', '-l', match_pattern], stdout=PIPE, cwd=root_directory)
        filelist = map(lambda name: path.join(root_directory,name), re.split('\n+', gitPipe.communicate()[0]))
        print('returning '+",".join(filelist))

        return filelist

    @staticmethod
    def isValid():
        return True

