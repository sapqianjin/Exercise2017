#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.04
# lesson: if else

height = 1.75
weight = 80.5

BMI = weight / (height * height)

if BMI < 18.5:
    print("too light")
elif BMI <= 25:
    print("normal")
elif BMI <= 28:
    print("too heavy")
elif BMI <= 32:
    print("too fat")
else:
    print("very fat")
