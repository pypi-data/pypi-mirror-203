# -*- coding: utf-8 -*-
"""Textbelt Python module for interacting with the Textbelt API.
    
This module is intended to be imported into your project to add SMS
functionality. Using this module and your developer token with Textbelt,
you can check your remaining quota, send SMS, check delivery status, 
and generate and send OTP codes.

Example:
    Import this module into your project with:

        from python_textbelt.textbelt import textbelt

    You can then instantiate a connection with Textbelt:

        txtblt_conn = textbelt.Connection(api_key)

    And check your remaining quota like such:
    
        response = txtblt_conn.check_quota()

"""

class APIKeyNotFoundError(Exception):
    """Error raised when Textbelt responds that it cannot find provided API key.

    Attributes:
        msg (str): Human readable string describing the exception.
    """

    def __init__(self):
        self.msg = "Textbelt could not find the provided API key."
    def __str__(self):
        return self.msg
    