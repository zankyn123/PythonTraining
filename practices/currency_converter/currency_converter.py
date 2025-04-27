"""
Write a program to convert an amount of money from one currency to another
using fixed exchange rates. The user inputs the amount and selects the currencies
for conversion.

Optional Enhancements
• Modify the program so that the user can see the equivalent amount in several
different currencies at the same time. For example, converting 100 USD to
EUR, CAD, and GBP all at once.
• Expand the list of available currencies for conversion. This might involve
adding more fixed exchange rates to the program.
• Keep a history of the most recent conversions made during the session and
display this history at the end of the program.
"""



import pandas as pd
from pathlib import Path

# ROOTDIR = Path(__file__).parent.joinpath("Book1.xlsx")

# excel = pd.read_excel(ROOTDIR)
# a = excel.
# print(a)

dict = {
    "datas": {
        "key": "VND",
        "datas": {
            "USD": 260000  
        }   
    }
}

print(dict)
