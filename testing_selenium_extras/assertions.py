# -*- coding: utf-8 -*-

import inspect
import logging
import re
from selenium.webdriver.support import expected_conditions
from . import utils

logger = logging.getLogger(__name__)

# log level for assertion success and failures
LEVEL_ASSERT_SUCCEEDED = logging.WARNING + 1
LEVEL_ASSERT_FAILED = logging.WARNING + 2


class AssertionMixin(object):
    '''
    Mixin class with Selenium-specific assertions. Intended to be mixed in to concrete test case classes.
    '''

    def _failure(self, params):
        '''
        Should report assertion failure in some way. Default behaviour is to log it using the
        package logger and then raise the AssertionError exception.

        Override in subclasses to perform additional actions (e.g. verbose logging).
        '''
        caller_method_name = inspect.stack()[1][3]
        logger.log(LEVEL_ASSERT_FAILED, 'Assertion {0} failed {1}'.format(caller_method_name, params))
        raise AssertionError(caller_method_name, params)

    def _success(self, params):
        '''
        Should report that assertion succeeded. Default behaviour is to log it using the
        package logger.

        Override in subclasses to perform additional actions.
        '''
        caller_method_name = inspect.stack()[1][3]
        logger.log(LEVEL_ASSERT_SUCCEEDED, 'Assertion {0} succeeded {1}'.format(caller_method_name, params))

    def assert_alert_is_present(self, driver):
        method_params = dict(alert_is_present=True)
        condition = expected_conditions.alert_is_present()
        if not condition(driver):
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_alert_is_not_present(self, driver):
        method_params = dict(alert_is_present=False)
        condition = expected_conditions.alert_is_present()
        if condition(driver):
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_document_title_equal(self, driver, expected):
        actual = driver.title
        method_params = dict(expected=expected, actual=actual)
        if actual != expected:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_document_title_not_equal(self, driver, expected):
        actual = driver.title
        method_params = dict(expected=expected, actual=actual)
        if driver.title == expected:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_document_title_matches(self, driver, pattern):
        actual = driver.title
        method_params = dict(pattern=pattern, actual=actual)
        if not re.match(pattern, driver.title) is None:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_document_title_not_matches(self, driver, pattern):
        actual = driver.title
        method_params = dict(pattern=pattern, actual=actual)
        if re.match(pattern, driver.title) is None:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_urlhash_equal(self, driver, expected):
        actual = utils.get_urlhash(driver)
        method_params = dict(actual=actual, expected=expected)
        if actual != expected:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_urlhash_not_equal(self, driver, expected):
        actual = utils.get_urlhash(driver)
        method_params = dict(actual=actual, expected=expected)
        if actual == expected:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_urlhash_matches(self, driver, pattern):
        actual = utils.get_urlhash(driver)
        method_params = dict(actual=actual, pattern=pattern)
        if not re.match(pattern, actual):
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_urlhash_not_matches(self, driver, pattern):
        actual = utils.get_urlhash(driver)
        method_params = dict(actual=actual, pattern=pattern)
        if re.match(pattern, actual):
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_present(self, driver, locator):
        method_params = dict(locator=locator)
        condition = expected_conditions.alert_is_present(locator)
        if not condition(driver):
            self._failure(method_params)
        else:
            self._success(method_params)


    def assert_element_not_present(self, driver, locator):
        method_params = dict(locator=locator)
        condition = expected_conditions.alert_is_present(locator)
        if condition(driver):
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_visible(self, element):
        method_params = dict()
        if not element.is_displayed():
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_not_visible(self, element):
        method_params = dict()
        if element.is_displayed():
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_enabled(self, element):
        method_params = dict()
        if element.is_disabled():
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_disabled(self, element):
        method_params = dict()
        if element.is_enabled():
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_selected(self, element):
        method_params = dict()
        if not element.is_selected():
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_not_selected(self, element):
        method_params = dict()
        if element.is_selected():
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_clickable(self, element):
        method_params = dict()
        if not element.is_clickable():
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_not_clickable(self, element):
        method_params = dict()
        if element.is_clickable():
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_text_equal(self, element, expected):
        actual = element.text
        method_params = dict(actual=actual, expected=expected)
        if actual != expected:
            self._failure(method_params)
        else:
            self._failure(method_params)

    def assert_element_text_not_equal(self, element, expected):
        actual = element.text
        method_params = dict(actual=actual, expected=expected)
        if actual == expected:
            self._failure(method_params)
        else:
            self._failure(method_params)

    def assert_element_tag_name_equal(self, element, expected):
        actual = element.tag_name
        method_params = dict(actual=actual, expected=expected)
        if actual != expected:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_tag_name_not_equal(self, element, expected):
        actual = element.tag_name
        method_params = dict(actual=actual, expected=expected)
        if actual != expected:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_rect_empty(self, element):
        rect = element.rect
        method_params = dict(rect=rect)
        if rect['width'] < utils.EPSILON or rect['height'] < utils.EPSILON:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_rect_not_empty(self, element):
        rect = element.rect
        method_params = dict(rect=rect)
        if rect['width'] >= utils.EPSILON and rect['height'] >= utils.EPSILON:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_rect_includes_point(self, element, point):
        rect = element.rect
        method_params = dict(rect=rect, point=point)
        if not utils.point_inside_rect(point, rect):
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_rect_not_includes_point(self, element, point):
        rect = element.rect
        method_params = dict(rect=rect, point=point)
        if utils.point_inside_rect(point, rect):
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_attr_equal(self, element, attr_name, expected_value):
        actual_value = element.get_attribute(attr_name)
        method_params = dict(attr_name=attr_name, expected_value=expected_value, actual_value=actual_value)
        if actual_value != expected_value:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_attr_not_equal(self, element, attr_name, expected_value):
        actual_value = element.get_attribute(attr_name)
        method_params = dict(attr_name=attr_name, expected_value=expected_value, actual_value=actual_value)
        if actual_value == expected_value:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_css_class_contains(self, element, expected_class):
        actual_class_list = utils.get_css_class_list(element)
        method_params = dict(actual_class_list=actual_class_list, expected=expected_class)
        if expected_class not in actual_class_list:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_css_class_not_contains(self, element, expected_class):
        actual_class_list = utils.get_css_class_list(element)
        method_params = dict(actual_class_list=actual_class_list, expected=expected_class)
        if expected_class in actual_class_list:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_css_property_equal(self, element, property_name, expected_value):
        actual_value = element.value_of_css_property(property_name)
        method_params = dict(actual_value=actual_value,expected_value=expected_value)
        if actual_value != expected_value:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_css_property_not_equal(self, elem, property_name, expected_value):
        actual_value = elem.value_of_css_property(property_name)
        method_params = dict(actual_value=actual_value,expected_value=expected_value)
        if actual_value == expected_value:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_child_of(self, element, parent_element):
        method_params = dict()
        actual_parent = element.find_element_by_xpath('..')
        if actual_parent.id != parent_element.id:
            self._failure(method_params)
        else:
            self._success(method_params)

    def assert_element_not_child_of(self, element, parent_element):
        method_params = dict()
        actual_parent = element.find_element_by_xpath('..')
        if actual_parent.id == parent_element.id:
            self._failure(method_params)
        else:
            self._success(method_params)
