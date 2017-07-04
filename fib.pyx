def fibonacci( int n ) :
    """
    Calcul la suite de Fibonacci : u_{n+1} = u_{n} + u_{n-1}
    avec u_{0} = 0, u_{1} = 1
    """
    cdef double a = 0.0
    cdef double b = 1.0
    cdef int    i
    for i in range(n):
        a,b = a + b, a
    return a

if __name__ == '__main__':
    import time
    t1 = time.time()
    v = fibonacci(90)
    t2 = time.time()
    print("Temps pris pour calculer fib(150) : {} secondes".format(t2-t1))
    
    
