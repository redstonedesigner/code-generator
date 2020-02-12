# Code Generator
This project is intended to allow users to generate codes that can then be used in gift-cards, vouchers, coupons or anything else that would need a code.

## Dependencies
Install using `pip install -r requirements.txt` or, if using PipEnv, `pipenv install -r requirements.txt`
* PyYAML - 5.1.1
* Colorama - 0.4.3

## Configuration
The configuration file has two options - `format` and `charset`.
* `charset` (String) - A list of all possible characters to be included in a code (Default: `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ`)
* `format` (String) - The code format to be used.  Hashtags (`#`) will be replaced with a random character from the character set (Default: `####-####-####-####`)

## Usage
To use the script, type `python app.py <amount>` where `<amount>` is the desired amount of codes.

## Output
The program will output a file, called `codes.txt` which will have all of your codes within it, each on its own line.
To read these in to a Python program, the following line of code works best:
```py
with open('codes.txt','r') as file:
  codes = file.read().splitlines()
  file.close()
```
