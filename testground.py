def func():





import timeit
runs = 1000000
duration = timeit.Timer(func).timeit(number = runs)
avg_duration = duration/runs
print(f'On average it took {avg_duration} seconds')