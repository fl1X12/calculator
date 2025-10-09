"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""

import sys
import click
# This script assumes a 'calculator.py' file exists in the 'src' directory
# with the required mathematical functions.
from src.calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """A simple command-line calculator."""
    try:
        # Validate that operations requiring two numbers receive them
        if operation in ["add", "subtract", "multiply", "divide", "power"]:
            if num2 is None:
                click.echo(f"Error: The '{operation}' operation requires two numbers.")
                sys.exit(1)

        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation == "square_root" or operation == "sqrt":
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Print the result, which will align with test expectations (e.g., 8.0)
        click.echo(result)

    except ValueError as e:
        # Handle errors raised from the calculator module (e.g., division by zero)
        click.echo(e)
        sys.exit(1)
    
    except ZeroDivisionError:
        # Specifically handle division by zero to match the test case
        click.echo("Cannot divide by zero")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
