import click


from somemanfib.fib_calcs.fib_number import recurring_fibonacci_number


@click.command()
@click.option(
    "--number", type=int, required=True, help="Fibonacci number to be  calculated."
)
def calculate_fib(number):
    print(f"Your fibonacci number : {recurring_fibonacci_number(number)}")
