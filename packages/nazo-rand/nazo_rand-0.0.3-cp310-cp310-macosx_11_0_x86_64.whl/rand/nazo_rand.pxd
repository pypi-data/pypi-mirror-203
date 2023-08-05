# cython: language_level=3
# distutils: language = c++

#cpdef void seed(int rseed = ?)
cpdef void shuffle(list array)
cpdef int random_integer_noargs()
cpdef object random_choice(object elements)
cpdef int randbelow(int a)
cpdef int randint(int a,int b)
cpdef int randrange(int start,int stop=?,int step=?)
cpdef double random_double(double a, double b)
cpdef double random_double_noargs()