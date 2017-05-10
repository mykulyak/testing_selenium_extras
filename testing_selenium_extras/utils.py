# -*- coding: utf-8 -*-

import logging
import re
import urllib.parse as urlparse

logger = logging.getLogger(__name__)


# precision of comparison of floating-point numbers, notably
# web element coordinates and dimensions
EPSILON = 0.001


def get_urlhash(driver):
    '''
    Returns the hash part of the current URL.

    :param driver: WebDriver
    :return: URL hash
    '''
    url = driver.current_url
    parts = urlparse.urlparse(url)
    return parts.fragment


_RE_CLASS_SEP = re.compile(r'\s+')


def get_css_class_list(element):
    '''
    Returns list of CSS classes given element has.

    :param element: WebElement
    :return: list of CSS classes the element has
    '''
    class_attr = element.get_attribute('class')
    return _RE_CLASS_SEP.split(class_attr)


def point_inside_rect(point, rect):
    '''
    Returns True if the point is inside the rectangle, False if it is outside.

    :param point: 2-element tuple containing point coordinates
    :param rect: a dictionary with keys x, y, width and height
    :return: True if the point is inside the rectangle, False if it is outside
    '''
    x, y = point
    dx = x - rect['x']
    dy = y - rect['y']
    return dx >= 0 and dx < rect['width'] and dy >= 0 and dy <= rect['height']
