import os
import json
from datetime import date
from typing import Any, Dict, List, Union, Optional, NamedTuple, Tuple, Mapping
import httpx
import logging

logging.basicConfig(
    format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=os.environ.get('DEBUG') and logging.DEBUG or logging.WARN
)

JsonNumber = Union[int, float]
JsonString = str
JsonNull = type(None)
JsonObject = Mapping[str, 'JsonType']
JsonArray = List['JsonType']

JsonType = Union[JsonNull, JsonNumber, JsonString, JsonObject, JsonArray]

class Customer(NamedTuple):
    first_name: str
    last_name: str
    email_address_primary: str
    hire_date: date
    create_date: date
    company_id: Union[str, None]
    phone_mobile: Union[str, None]
    external_id: Union[str, None]

class I9EverywhereClient:
    auth_key: str
    api_base_url: str

    def __init__(self, auth_key: str, api_base_url: str = "https://test-api.pointhr.com"):
        self.auth_key = auth_key
        self.api_base_url = api_base_url

    def _send_request(self, method: str, endpoint: str, params: Optional[List[Tuple[str, str]]] = None, data: JsonType = None) -> JsonType:
        url = self.api_base_url + endpoint
        logging.debug(f'params: {params}')
        logging.debug(f'json: {data}')
        headers = {'authKey': self.auth_key, 'apiKey': self.auth_key}
        timeout = 60
        response = httpx.request(method, url, params=params, json=data, headers=headers, timeout=timeout)
        logging.debug(f'response text: {response.text}')
        response.raise_for_status()
        return response.json()

    def add_customer(self, customer: Customer) -> JsonType:
        date_fmt = '%m/%d/%Y'
        data = {
            "firstName": customer.first_name,
            "lastName": customer.last_name,
            "EmailAddressPrimary": customer.email_address_primary,
            "hireDate": customer.hire_date.strftime(date_fmt),
            "createDate": customer.create_date.strftime(date_fmt)
        }
        if customer.company_id:
            data["companyID"] = customer.company_id
        if customer.phone_mobile:
            data["phoneMobile"] = customer.phone_mobile
        if customer.external_id:
            data["ExternalID"] = customer.external_id

        return self._send_request("POST", "/customer/add", data=data)

    def add_customers(self, customers: List[Customer]):
        date_fmt = '%m/%d/%Y'
        customer_dicts: JsonArray = []

        for customer in customers:
            customer_dict = {
                "firstName": customer.first_name,
                "lastName": customer.last_name,
                "EmailAddressPrimary": customer.email_address_primary,
                "hireDate": customer.hire_date.strftime(date_fmt),
                "createDate": customer.create_date.strftime(date_fmt),
                "authKey": self.auth_key,
            }
            if customer.company_id:
                customer_dict["companyID"] = customer.company_id
            if customer.phone_mobile:
                customer_dict["phoneMobile"] = customer.phone_mobile
            if customer.external_id:
                customer_dict["ExternalID"] = customer.external_id
            customer_dicts.append(customer_dict)

        return self._send_request("POST", "/customers/add", data=customer_dicts)

    def get_customer_status(self, hire_date: date, email_address: Optional[str] = None,
                            ssn: Optional[str] = None, external_id: Optional[str] = None):
        if not email_address and not ssn and not external_id:
            raise Exception(f"One of email, SSN, or external ID required")

        params: List[Tuple[str, str]] = [("hiredate", hire_date.strftime('%m/%d/%Y'))]
        if email_address:
            params.append(("emailAddress", email_address))
        if ssn:
            params.append(("SSN", ssn))
        if external_id:
            params.append(("externalID", external_id))
        params.append(('authKey', self.auth_key))

        return self._send_request("GET", "/employee/status", params=params)

    def update_termination_date(self, term_date: date, hire_date: date, company_id: str, email_address: Optional[str] = None, ssn: Optional[str] = None, external_id: Optional[str] = None):
        data = {
            "termDate": term_date.strftime('%m/%d/%Y'),
            "hireDate": hire_date.strftime('%m/%d/%Y'),
            "companyID": company_id
        }
        if email_address:
            data["emailAddress"] = email_address
        if ssn:
            data["ssn"] = ssn
        if external_id:
            data["externalID"] = external_id

        return self._send_request("POST", "/employee/updateTermDate", data=data)

    def update_hire_date(self, new_hire_date: date, old_hire_date: date, company_id: str, email_address: Optional[str] = None, ssn: Optional[str] = None, external_id: Optional[str] = None):
        data = {
            "newHireDate": new_hire_date.strftime('%m/%d/%Y'),
            "oldhireDate": old_hire_date.strftime('%m/%d/%Y'),
            "companyID": company_id
        }
        if email_address:
            data["emailAddress"] = email_address
        if ssn:
            data["ssn"] = ssn
        if external_id:
            data["externalID"] = external_id

        return self._send_request("POST", "/employee/updateHireDate", data=data)
