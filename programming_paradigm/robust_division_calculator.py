def safe_divide(numerator, denominator):
    """
    Try to divide numerator by denominator.
    Returns a user-friendly string for success or specific error messages.
    """
    try:
        # Try converting inputs to floats (this may raise ValueError)
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"

