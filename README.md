# Paystack4Python

A Python client library for the [Paystack API](https://paystack.com/docs/api/). This package provides convenient access to Paystack's payment services, allowing you to manage customers, transactions, plans, and more from your Python applications.

## Features

- Easy integration with Paystack's RESTful API
- Manage customers, transactions, and plans
- Error handling and utility functions
- Pythonic interface for common Paystack operations

## Installation

Install via pip:

```bash
pip install paystack4python
```

Or clone this repository and install locally:

```bash
git clone https://github.com/mwaiseghegift/paystack4python.git
cd paystack4python
pip install .
```

## Usage

First, import the relevant classes and initialize the API with your secret key:

```python
from paystack4python.baseapi import PaystackBaseAPI
from paystack4python.customers import CustomersAPI
from paystack4python.transactions import TransactionsAPI
from paystack4python.plans import PlansAPI

# Initialize the base API with your Paystack secret key
api = PaystackBaseAPI(secret_key='sk_test_xxx')

# Customers
customers = CustomersAPI(api)
response = customers.create(email='user@example.com', first_name='John', last_name='Doe')

# Transactions
transactions = TransactionsAPI(api)
response = transactions.initialize(email='user@example.com', amount=5000)

# Plans
plans = PlansAPI(api)
response = plans.create(name='Monthly Plan', amount=10000, interval='monthly')
```

## API Reference

### Authentication

All API requests require your Paystack secret key. Pass it when initializing `PaystackBaseAPI`.

### Modules

- `baseapi.py`: Core API request logic and authentication
- `customers.py`: Customer management (create, fetch, update, list)
- `transactions.py`: Transaction initialization, verification, listing
- `plans.py`: Plan creation, update, listing
- `errors.py`: Custom exceptions for error handling
- `utils.py`: Helper functions

### Example: Creating a Customer

```python
from paystack4python.baseapi import PaystackBaseAPI
from paystack4python.customers import CustomersAPI

api = PaystackBaseAPI(secret_key='sk_test_xxx')
customers = CustomersAPI(api)
response = customers.create(email='user@example.com', first_name='Jane', last_name='Doe')
print(response)
```

### Example: Initializing a Transaction

```python
from paystack4python.baseapi import PaystackBaseAPI
from paystack4python.transactions import TransactionsAPI

api = PaystackBaseAPI(secret_key='sk_test_xxx')
transactions = TransactionsAPI(api)
response = transactions.initialize(email='user@example.com', amount=10000)
print(response)
```

## Error Handling

All API errors raise custom exceptions defined in `errors.py`. Use try/except blocks to handle errors gracefully.

```python
from paystack4python.errors import PaystackAPIError

try:
    # ... your code ...
except PaystackAPIError as e:
    print(f"Paystack error: {e}")
```

## Testing

Run tests using pytest:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for bug fixes, features, or improvements.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the `LICENCE` file for details.
