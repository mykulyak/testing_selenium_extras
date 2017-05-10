# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


class ajax_call_is_pending(object):
    '''
    Wait condition that evaluates to True only if there is no pending AJAX calls.

    TODO To be moved from CaMon.
    '''

    def __init__(self):
        pass

    def __call__(self):
        pass


class animation_is_running(object):
    '''
    Wait condition that evaluates to True only if there is some animations running
    on the page.

    TODO To be moved from CaMon.
    '''

    def __init__(self):
        pass

    def __call__(self):
        pass
