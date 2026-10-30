# School Event: Reusing a Python Package

This example includes the supplied snack_shack package and a separate program,
school_event.py, that uses its functions. The supplied Python files are unchanged.
No pip installation or external libraries are needed.

## Run it

1. Extract the ZIP.
2. Open the school_event_example folder in VS Code.
3. Open a terminal in that folder (the folder containing school_event.py).
4. Run:

```powershell
python school_event.py
```

The school_event.py file sits beside the snack_shack folder, outside the package.
Do not put school_event.py inside snack_shack.

## How the import works

```python
from snack_shack import display, pricing, validation
```

This imports three modules from the package. Then the program calls their functions:

```python
display.display_welcome()
quantity = validation.get_valid_quantity()
total = pricing.calculate_total(quantity)
display.display_receipt(item_name, quantity, total)
```

The package's __init__.py does not need extra imports for this approach.
Importing these modules does not run snack_shack/app.py or __main__.py.
The school event program controls its own mainline and reuses the tools it needs.

## Example run

```text
School Movie Night - Snack Sales

Welcome to the snack shack
Most snacks are $4.00
What snack are we selling? Popcorn
Enter a quantity: 3

Snack: Popcorn
Quantity: 3
Total: $12.00
Thanks for supporting our school movie night!
```

## Try a different price

In school_event.py, replace:

```python
total = pricing.calculate_total(quantity)
```

with:

```python
total = pricing.calculate_total(quantity, unit_price=3.00)
```

Three snacks now cost $9.00. The supplied welcome function still displays its fixed
$4.00 message; update that message if you make this teaching variation permanent.

## Run the package's original application

From the same terminal folder:

```powershell
python -m snack_shack
```

That runs snack_shack/__main__.py, which calls the original app's main function.
It is a separate entry point from school_event.py. The supplied original app uses
$3.00, while its welcome message says most snacks are $4.00.

## A small validation detail

The supplied get_valid_quantity() rejects non-integer input, but accepts zero
and negative integers. school_event.py adds a loop to require a positive quantity
without changing the package.
