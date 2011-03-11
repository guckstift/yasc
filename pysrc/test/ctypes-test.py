
import ctypes as ct

lt = ct.CDLL ("bin/test/libtest.so")

arr = [[1,2,3],[4,5,6]]

INT = ct.c_int
PINT = ct.POINTER(INT)
PPINT = ct.POINTER(PINT)

INT3ARR = INT * 3
PINT2ARR = PINT * 2

vals = PINT2ARR ()
for y in range(2):
	vals[y] = INT3ARR ()
	for x in range(3):
		vals[y][x] = arr[y][x]

lt.give_matrix (3, 2, vals);
