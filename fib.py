def fibonacci( n ) :
    """
    Calcul la suite de Fibonacci : u_{n+1} = u_{n} + u_{n-1}
    avec u_{0} = 0, u_{1} = 1
    """
    a = 0.0
    b = 1.0
    for i in range(n):
        a,b = a + b, a
    return a

if __name__ == '__main__':
    import timeit
    r0 = timeit.timeit(
        """
import fib
r =fib.fibonacci(0)
        """)
    r1 = timeit.timeit(
        """
import fib
r =fib.fibonacci(90)
        """)
    r2 = timeit.timeit(
        """
import fib
r =fib.fibonacci(180)
        """)

    print("Temps pris for Fibonacci(0) : {}".format(r0))
    print("Temps pris for Fibonacci(90) : {}".format(r1))
    print("Temps pris for Fibonacci(180) : {}".format(r2))
    
