#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    return 0.0


def square(a: float) -> float:
    return 0.0


def average(a, b, c):
    return (a + b + c)/3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return 0.0


def to_degrees(angle_rads):
    # Convertir en degrés, minutes, secondes un angle fourni au départ en radians
    degres = angle_rads * 180 / math.pi
    min = (degres - math.floor(degres)) * 60
    sec = (min - math.floor(min)) * 60
    return math.floor(degres), min, sec


def to_celsius(temperature: float) -> float:
    return 0.0


def to_farenheit(temperature: float) -> float:
    return 0.0


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    ma_moyenne = average(1, 2, 3)
    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
