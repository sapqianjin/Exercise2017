#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.13
# lesson: excel file processing

import openpyxl

wb = openpyxl.load_workbook('./Automatic/Boo1.xlsx')
print(type(wb))
print(wb.get_sheet_names())