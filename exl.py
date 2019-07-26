#-*- coding:utf-8 -*-
import xlrd,xlwt
book = xlrd.open_workbook('class.xls')
sheet = book.sheet_by_index(0)
print(sheet)
