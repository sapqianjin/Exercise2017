#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.13
# lesson: convert xls excel file  to xlsx

import win32com.client
import os

for folder_name, subfolders, filenames in os.walk('./xls/'):
    for filename in filenames:
        report = os.path.join(os.getcwd()+'\\xls\\'+filename)
        # print(report)
        if report[-3:] == 'xls':
            excel = win32com.client.gencache.EnsureDispatch('Excel.Application')  # 要看MIME手册
            wb = excel.Workbooks.Open(report)
            wb.SaveAs(report + 'x', FileFormat=51)
            wb.Close()
            excel.Application.Quit()
            os.remove(report)