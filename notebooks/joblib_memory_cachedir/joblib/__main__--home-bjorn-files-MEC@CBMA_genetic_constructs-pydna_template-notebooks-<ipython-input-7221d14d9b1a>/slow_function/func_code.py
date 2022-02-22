# first line: 1
@memory.cache
def slow_function(x):
    for i in tqdm_notebook(range(x), desc='1st loop'):
        for j in tqdm_notebook(range(100), desc='2nd loop'):
            sleep(0.001)
    return "done!"
