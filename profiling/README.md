
# Profiling

![](mandelbort.png)

Run the code in [mandelbrot.py](mandelbrot.py) and time its execution with cProfile, the Python profiler:

    python -m cProfile -s cumtime mandelbrot.py > profile.txt

Inspect the output and look for bottlenecks.

Insert the line

    z[index] = z[index] ** 2 + c[index]

Re-run the profiling.

## Timing in IPython/Jupyter

In IPython environments, you can time single Python expressions with

    %time list(range(1000000))

and

    %timeit list(range(1000000))
