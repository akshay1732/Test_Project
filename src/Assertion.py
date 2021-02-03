"""
Created on Nov 15, 2019

@author: 10644845
"""


def KelvinToFahrenheit(Temperature):
    try:
        assert (Temperature >= 0)
        return ((Temperature - 273) * 1.8) + 32
    except AssertionError:
        print("Negative value!")
        return ((Temperature - 273) * 1.8) + 32


print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))
