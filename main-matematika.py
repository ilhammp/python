import module_matematika

module_matematika.kurang(7,3)
module_matematika.tambah(3,4)
print("\n")

import module_matematika as math

math.tambah(4,3)
math.kurang(10,9)
print("\n")

from module_matematika import tambah,kurang

tambah(4,3)
kurang(10,7)
print("\n")

from module_matematika import tambah as t

t(4,5)
print("\n")