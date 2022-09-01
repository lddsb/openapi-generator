# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import petstore_api
from petstore_api.model.date_time_with_validations import DateTimeWithValidations
from datetime import date, datetime, timezone


class TestDateTimeWithValidations(unittest.TestCase):
    """DateTimeWithValidations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDateTimeWithValidations(self):
        """Test DateTimeWithValidations"""

        # works with datetime input
        valid_values = [datetime(2020, 1, 1), '2020-01-01T00:00:00']
        expected_datetime = '2020-01-01T00:00:00'
        for valid_value in valid_values:
            inst = DateTimeWithValidations(valid_value)
            assert inst == expected_datetime

        # when passing data in with from_openapi_data_oapg one must use str
        with self.assertRaisesRegex(
            petstore_api.ApiTypeError,
            r"Invalid type. Required value type is str and passed type was datetime at \['args\[0\]'\]"
        ):
            DateTimeWithValidations.from_openapi_data_oapg(datetime(2020, 1, 1))

        # when passing data from_openapi_data_oapg we can use str
        input_value_to_datetime = {
            "2020-01-01T00:00:00": datetime(2020, 1, 1, tzinfo=None),
            "2020-01-01T00:00:00Z": datetime(2020, 1, 1, tzinfo=timezone.utc),
            "2020-01-01T00:00:00+00:00": datetime(2020, 1, 1, tzinfo=timezone.utc)
        }
        for input_value, expected_datetime in input_value_to_datetime.items():
            inst = DateTimeWithValidations.from_openapi_data_oapg(input_value)
            assert inst.as_datetime_oapg == expected_datetime

        # value error is raised if an invalid string is passed in
        with self.assertRaisesRegex(
            petstore_api.ApiValueError,
            r"Value does not conform to the required ISO-8601 datetime format. Invalid value 'abcd' for type datetime at \('args\[0\]',\)"
        ):
            DateTimeWithValidations.from_openapi_data_oapg("abcd")

        # value error is raised if a date is passed in
        with self.assertRaisesRegex(
            petstore_api.ApiValueError,
            r"Value does not conform to the required ISO-8601 datetime format. Invalid value '2020-01-01' for type datetime at \('args\[0\]',\)"
        ):
            DateTimeWithValidations(date(2020, 1, 1))

        # pattern checking with string input
        error_regex = r"Invalid value `2019-01-01T00:00:00Z`, must match regular expression `.+?` at \('args\[0\]',\)"
        with self.assertRaisesRegex(
            petstore_api.ApiValueError,
            error_regex
        ):
            DateTimeWithValidations.from_openapi_data_oapg("2019-01-01T00:00:00Z")
        # pattern checking with date input
        error_regex = r"Invalid value `2019-01-01T00:00:00`, must match regular expression `.+?` at \('args\[0\]',\)"
        with self.assertRaisesRegex(
            petstore_api.ApiValueError,
            error_regex
        ):
            DateTimeWithValidations(datetime(2019, 1, 1))


if __name__ == '__main__':
    unittest.main()
