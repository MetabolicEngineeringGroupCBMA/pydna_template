# first line: 1
@memory.cache
def slow_function(x):
    for i in trange(x, desc='1st loop'):
        for j in tqdm(range(100), desc='2nd loop'):
            sleep(0.01)
    return "done!"
