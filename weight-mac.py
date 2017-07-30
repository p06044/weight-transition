# -*- coding: utf-8 -*-
import xlrd
import numpy as np
import os
from matplotlib import pyplot as plt
book = xlrd.open_workbook('/Users/sortme/Documents/統計記録.xls')
sheet = book.sheet_by_index(1)
nrows = sheet.nrows
data = np.zeros(2*nrows).reshape((nrows,2))
date = []
for col in [0, 1]:
	for row in range(sheet.nrows):
		if col==0:
			d =  xlrd.xldate.xldate_as_datetime(sheet.cell(row,col).value, book.datemode)
			date.append(d)
		data[row,col] = sheet.cell(row,col).value
weight = data[:,1]
plt.xticks(rotation =12)
plt.plot(date, weight, label="weight transition")
plt.legend()
#plt.savefig("/Users/sortme/weight.png")
plt.show()
