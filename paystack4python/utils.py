from .errors import InvalidDataError


def validate_amount(amount):
    if amount is None:
        raise InvalidDataError("Amount to be charged is required")

    if isinstance(amount, int) or isinstance(amount, float): #Save the sever some headaches
        if amount < 0:
            raise InvalidDataError("Negative amount is not allowed")
        return amount
    else:
        raise InvalidDataError("Amount should be a number")


def validate_interval(interval):

    interval = interval if interval.lower() in ['hourly', 'daily', 'weekly', 'monthly', 'annually'] else None
    if not interval:
        raise InvalidDataError("Please provide a valid plan interval")
    return interval



