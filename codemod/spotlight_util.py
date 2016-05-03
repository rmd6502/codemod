#!/usr/bin/env python

# Copyright (c) 2007-2008 Facebook

import Cocoa


class SpotlightUtil(object):
    """
    Searches a directory hierarchy using OS/X spotlight
    """

    @staticmethod
    def walk_directory(root_directory, match_pattern):
        query = Cocoa.NSMetadataQuery.alloc().init()
        # going to trust that the user specified the proper
        # spotlight format pattern
        predicate = Cocoa.NSPredicate.predicateWithFormat_(
            "(kMDItemTextContent = \"" + match_pattern + "\")")
        if root_directory is not None:
            query.setSearchScopes_([root_directory])
        query.setPredicate_(predicate)
        query.startQuery()
        # TODO: figure out how to do this asynchronously if possible
        while query.isGathering():
            Cocoa.NSRunLoop.currentRunLoop().runUntilDate_(
                Cocoa.NSDate.dateWithTimeIntervalSinceNow_(1))
        query.stopQuery()
        items = []
        for item in query.results():
            filename = item.valueForAttribute_(Cocoa.NSMetadataItemPathKey)
            if filename is not None:
                items.append(filename)
        return items
