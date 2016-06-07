#!/usr/bin/env python

# Copyright (c) 2007-2008 Facebook

from subprocess import Popen, PIPE
import re
from os import path


class GitUtil(object):
    """
    Searches a directory hierarchy using git grep.
    """

    def walk_directory(self, root_directory, match_pattern):
        """
        Uses git grep to find all files containing a particular pattern

        >>> util = GitUtil()
        >>> sorted(util.walk_directory(".","compute_percentile"))
        ['./codemod/base.py', './codemod/git_util.py']
        """
        gitPipe = Popen(['git', 'grep', '-l', match_pattern], stdout=PIPE,
                        cwd=root_directory)
        filelist = map(lambda name: path.join(root_directory, name),
                       re.split('\n+', gitPipe.communicate()[0]))
        # remove the blank entry from the final \n
        filelist.pop()

        return filelist

    @staticmethod
    def isValid():
        return True
