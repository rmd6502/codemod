#!/usr/bin/env python

# Copyright (c) 2007-2008 Facebook

import Cocoa
import objc


class SpotlightUtil(object):
    """
    Searches a directory hierarchy using OS/X spotlight
    """

    def walk_directory(self, root_directory, match_pattern):
        query = Cocoa.NSMetadataQuery.alloc().init()
        # going to trust that the user specified the proper
        # spotlight format pattern
        predicate = Cocoa.NSPredicate.predicateWithFormat_(
            "(kMDItemTextContent = \"" + match_pattern + "\")")
        if root_directory is not None:
            query.setSearchScopes_([root_directory])
        query.setPredicate_(predicate)

        Cocoa.NSNotificationCenter.defaultCenter(). \
            addObserver_selector_name_object_(
                self,
                objc.selector(self._done),
                Cocoa.NSMetadataQueryDidFinishGatheringNotification,
                query)
        if query.startQuery():
            Cocoa.CFRunLoopRun()
        Cocoa.NSNotificationCenter.defaultCenter(). \
            removeObserver_name_object_(
                self,
                Cocoa.NSMetadataQueryDidFinishGatheringNotification,
                query)

        query.stopQuery()
        items = []
        for item in query.results():
            filename = item.valueForAttribute_(Cocoa.NSMetadataItemPathKey)
            if filename is not None:
                items.append(filename)
        return items

    def _done(self, notification):
        notification.object().stopQuery()
        Cocoa.CFRunLoopStop(Cocoa.CFRunLoopGetCurrent())
