# I9Everywhere API Python library and CLI

Python client library and CLI for the I9Everywhere API V4.

This is a Python client library and CLI that interacts with the I9EverywhereClient API to add and retrieve customer data.

## Requirements

- Python 3.6 or higher
- `click` library
- `pathlib` library

## Installation

1. Install Python 3.6 or higher
1. Install the required libraries using pip: `pip install click pathlib i9-everywhere-client`

## Usage

The CLI program `i9everywhere` has four main commands:

- `add_customer` - adds a single customer to I9Everywhere. Required parameters are `first_name`, `last_name`, `email`, `hire_date`, and `create_date`. Optional parameters are `company_id`, `phone_mobile`, and `external_id`.
- `add_customers` - adds multiple customers to I9Everywhere. The customers are provided in CSV format, either from a file given by `--csv_file` or read from standard input. The CSV file must have a header row with the same names as the paramters as `add_customer`. For example:

```csv
first_name,last_name,email,hire_date,create_date
Ethan,Williams,ethan.williams@adhoc.team,4/18/2023,4/18/2023
Madison,Johnson,madison.johnson@adhoc.team,4/18/2023,4/18/2023
Aiden,Brown,aiden.brown@adhoc.team,4/18/2023,4/18/2023
Olivia,Davis,olivia.davis@adhoc.team,4/18/2023,4/18/2023
Benjamin,Garcia,benjamin.garcia@adhoc.team,4/18/2023,4/18/2023
Sophia,Wilson,sophia.wilson@adhoc.team,4/18/2023,4/18/2023
Jacob,Rodriguez,jacob.rodriguez@adhoc.team,4/18/2023,4/18/2023
Isabella,Martinez,isabella.martinez@adhoc.team,4/18/2023,4/18/2023
Michael,Anderson,michael.anderson@adhoc.team,4/18/2023,4/18/2023
Emma,Smith,emma.smith@adhoc.team,4/18/2023,4/18/2023
```

- `get_customer_status` - retrieves the I9 form status for a single customer. Required parameter is `hire_date`, plus at least one of `email`, `ssn`, or `external_id`.
- `update_termination_date` - not yet implemented.
- `update_hire_date` - not yet implemented.

The CLI requires an authentication key to access the I9Everywhere API. The key can be provided as a command-line argument using the `--auth_key` option or as an environment variable named `I9_EVERYWHERE_API_KEY`.

## Example

Add a customer with the following details:

- First name: John
- Last name: Doe
- Email: john.doe@example.com
- Hire date: 04/18/2022
- Create date: today's date
- Company ID: 1234
- Mobile phone: +1 (555) 555-1212
- External ID: 5678

```sh
i9everywhere add_customer --auth_key <your_auth_key> --first_name John --last_name Doe --email john.doe@example.com --hire_date 04/18/2022 --company_id 1234 --phone_mobile "+1 (555) 555-1212" --external_id 5678
```
