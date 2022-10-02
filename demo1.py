print("hello world")
import datetime
from tkinter.tix import WINDOW
dtstr = input("enter the datetime:")
print(datetime)
dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
another_dystr = dtstr[:4] + "0101"
another_dt = datetime.datetime.strptime(another_dystr, "%Y%m%d")
print(int((dt - another_dt).days) + 1)
WINDOW