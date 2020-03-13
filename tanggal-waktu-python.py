import time;  # Digunakan untuk meng-import modul time
from builtins import print

ticks = time.time()
print ("Berjalan sejak 12:00am, January 1, 1970:", ticks)
print("\n")

import time;

localtime = time.localtime(time.time())
print("Waktu lokal saat ini :", localtime)
print("\n")

import time;

localtime = time.asctime( time.localtime(time.time()) )
print ("Waktu lokal saat ini :", localtime)
print("\n")

#mendapatkan kalender
import calendar

cal = calendar.month(2020, 2)
print ("Dibawah ini adalah kalender:")
print (cal)