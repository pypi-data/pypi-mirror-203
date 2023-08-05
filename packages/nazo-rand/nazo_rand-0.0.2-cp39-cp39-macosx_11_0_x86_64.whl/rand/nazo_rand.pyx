# cython: language_level=3
# distutils: language = c++
cimport cython
from libc.stdint cimport int64_t, uint64_t

cdef extern from "nazo_rand.hpp" namespace "Storm":
    ctypedef int64_t Integer
    void seed(uint64_t seed)
    Integer uniform_int_variate_noargs()
    Integer random_range(Integer start, Integer stop, Integer step)
    Integer random_below(Integer number)
    Integer uniform_int_variate(Integer a, Integer b)
    double uniform_real_variate_noargs()
    double uniform_real_variate(double a, double b)

cpdef int random_integer_noargs():
    return uniform_int_variate_noargs()

cpdef void shuffle(list array):
    for i in reversed(range(len(array) - 1)):
        j = randrange(i, len(array), 1)
        array[i], array[j] = array[j], array[i]


cpdef int randbelow(int a):
    return random_below(a)

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef object random_choice(object elements):
    cdef Py_ssize_t index = randbelow(len(elements))
    return elements[index]


cpdef int randint(int a, int b):
    return uniform_int_variate(a, b)

cpdef int randrange(int start, int stop=0, int step=1):
    if stop == 0:
        stop, start = start, 0
    return random_range(start, stop, step)


cpdef double random_double(double a, double b):
    return uniform_real_variate(a, b)


cpdef double random_double_noargs():
    return uniform_real_variate_noargs()
