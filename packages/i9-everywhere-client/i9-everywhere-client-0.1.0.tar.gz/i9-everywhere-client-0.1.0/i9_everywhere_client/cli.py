from datetime import date
import os
import sys
import csv
import click
from pathlib import Path
from datetime import datetime
from i9_everywhere_client import Customer, I9EverywhereClient

@click.group()
@click.option('--auth_key', help='The authentication key for the API.')
@click.pass_context
def cli(ctx, auth_key):
    ctx.ensure_object(dict)
    env_auth_key = os.environ.get('I9_EVERYWHERE_API_KEY', None)
    if auth_key and env_auth_key:
        raise click.UsageError("Both --auth_key option and I9_EVERYWHERE_API_KEY environment variable are set. Use only one of them.")
    if not auth_key and not env_auth_key:
        raise click.UsageError("Authentication key must be provided either via --auth_key option or I9_EVERYWHERE_API_KEY environment variable.")
    final_auth_key = auth_key or env_auth_key
    ctx.obj['CLIENT'] = I9EverywhereClient(final_auth_key)

@cli.command()
@click.option('--first_name', required=True, help='First name of the customer.')
@click.option('--last_name', required=True, help='Last name of the customer.')
@click.option('--email', required=True, help='Primary email address of the customer.')
@click.option('--hire_date', required=True, help='Hire date of the customer in MM/DD/YYYY format.')
@click.option('--create_date', required=True, help='Create date of the customer in MM/DD/YYYY format.', default=date.today().strftime('%m/%d/%Y'))
@click.option('--company_id', default=None, help='Company ID of the customer.')
@click.option('--phone_mobile', default=None, help='Mobile phone number of the customer.')
@click.option('--external_id', default=None, help='External ID of the customer.')
@click.pass_context
def add_customer(ctx, first_name, last_name, email, hire_date, create_date, company_id, phone_mobile, external_id):
    client = ctx.obj['CLIENT']
    customer = Customer(
        first_name=first_name,
        last_name=last_name,
        email_address_primary=email,
        hire_date=datetime.strptime(hire_date, '%m/%d/%Y').date(),
        create_date=datetime.strptime(create_date, '%m/%d/%Y').date(),
        company_id=company_id,
        phone_mobile=phone_mobile,
        external_id=external_id,
    )
    response = client.add_customer(customer)
    print(response)

@cli.command()
@click.option('--csv_file', type=click.Path(exists=True), default=None, help='Path to the CSV file containing customer data.')
@click.pass_context
def add_customers(ctx, csv_file):
    client = ctx.obj['CLIENT']

    if csv_file:
        with open(csv_file, 'r') as file:
            customer_data = list(csv.DictReader(file))
    else:
        customer_data = list(csv.DictReader(sys.stdin))

    customers = []
    for row in customer_data:
        customers.append(Customer(
            first_name=row['first_name'],
            last_name=row['last_name'],
            email_address_primary=row['email'],
            hire_date=datetime.strptime(row['hire_date'], '%m/%d/%Y').date(),
            create_date=datetime.strptime(row['create_date'], '%m/%d/%Y').date(),
            company_id=row.get('company_id', ''),
            phone_mobile=row.get('phone_mobile', ''),
            external_id=row.get('external_id', ''),
        ))

    response = client.add_customers(customers)
    print(response)

@cli.command()
@click.option('--hire_date', required=True, help='Hire date of the customer in MM/DD/YYYY format.')
@click.option('--email', default=None, help='Primary email address of the customer.')
@click.option('--ssn', default=None, help='Social Security Number of the customer.')
@click.option('--external_id', default=None, help='External ID of the customer.')
@click.pass_context
def get_customer_status(ctx, hire_date, email, ssn, external_id):
    client = ctx.obj['CLIENT']
    response = client.get_customer_status(
        hire_date=datetime.strptime(hire_date, '%m/%d/%Y').date(),
        email_address=email,
        ssn=ssn,
        external_id=external_id,
    )
    print(response)

@cli.command()
def update_termination_date():
    pass

@cli.command()
def update_hire_date():
    pass

if __name__ == '__main__':
    cli(obj={})
