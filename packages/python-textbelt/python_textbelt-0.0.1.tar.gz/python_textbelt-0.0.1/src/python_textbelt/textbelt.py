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

import requests
from . import exceptions


class Connection:
    """A connection object through which you can interact with the Textbelt API.

    Creating an instance of this class facilitates interacting with the Textbelt
    API by not having to constantly pass your API key with each request. The
    requests are mostly abstracted away, and you can simply instantiate a
    connection with your API key, and then interact with the connection object's
    various methods.

    """

    def __init__(self, api_key: str, base_url="https://textbelt.com"):
        """__init__ method for instantiating a connection object.

        Args:
            api_key (str): API key from Textbelt
            base_url (str, optional): Hostname of the target server. 
                Configure if interacting with a self-hosted server. 
                Defaults to "https://textbelt.com".

        Raises:
            exceptions.APIKeyNotFoundError: If the Textbelt API call returns
                "success": False, then the API call failed and/or the key was
                no good.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.quota = None
        try:
            response = requests.get(f"{base_url}/quota/{api_key}", timeout=5)
            response.raise_for_status()
            if response.status_code == 200:
                if response.json()["success"] is not True:
                    raise exceptions.APIKeyNotFoundError
        except requests.exceptions.HTTPError as error:
            print("HTTP Error:",error)
        except requests.exceptions.Timeout as error:
            print("Timeout Error:",error)
        self.refresh_quota()


    def refresh_quota(self) -> requests.Response:
        """Refreshes the object's stored quota with Textbelt.

        Returns:
            requests.Response: Request library response object.
        """
        try:
            response = requests.get(
                f"{self.base_url}/quota/{self.api_key}",
                timeout=5)
            response.raise_for_status()
            if response.status_code == 200:
                new_quota = response.json()["quotaRemaining"]
                self.set_quota(new_quota)
        except requests.exceptions.HTTPError as error:
            print("HTTP Error:",error)
        except requests.exceptions.Timeout as error:
            print("Timeout Error:",error)
        return response


    def set_quota(self, new_quota: int) -> None:
        """Sets connection object's quota.

        Args:
            new_quota (int): New value to set quota to.

        Returns:
            requests.Response: Request library response object.
        """
        self.quota = new_quota


    @property
    def get_quota(self) -> int:
        """Get connection object's remaining quota.

        Returns:
            int: Remaining quota.
        """
        return self.quota


    def send_sms(self, phone_num: str, msg: str) -> requests.Response:
        """Sends a Textbelt SMS.

        Args:
            phone_num (str): Destination phone number.
            msg (str): Message content.

        Returns:
            requests.Response: Request library response object.
        """
        try:
            response = requests.post(f"{self.base_url}/text", {
                "phone": phone_num,
                "message": msg,
                "key": self.api_key
            }, timeout=5)
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print("HTTP Error:",error)
        except requests.exceptions.Timeout as error:
            print("Timeout Error:",error)
        self.set_quota(response.json()["quotaRemaining"])
        return response


    def get_sms_status(self, text_id) -> requests.Response:
        """Gets the status of a previously sent SMS.

        Args:
            text_id (_type_): ID of SMS. Check returned JSON from send_sms().

        Returns:
            requests.Response: Request library response object.
        """
        try:
            response = requests.get(
                f"{self.base_url}/status/{text_id}", timeout=5)
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print("HTTP Error:",error)
        except requests.exceptions.Timeout as error:
            print("Timeout Error:",error)
        return response


    def test_send_sms(self, phone_num: str, msg: str) -> requests.Response:
        """Does not actually send SMS, useful for testing if API key is valid.

        Args:
            phone_num (str): Destination phone number.
            msg (str): Message content.
        Returns:
            requests.Response: Request library response object.
        """
        try:
            response = requests.post(f"{self.base_url}/text", {
                "phone": phone_num,
                "message": msg,
                "key": self.api_key + "_test"
            }, timeout=5)
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print("HTTP Error:",error)
        except requests.exceptions.Timeout as error:
            print("Timeout Error:",error)
        self.set_quota(response.json()["quotaRemaining"])
        return response
