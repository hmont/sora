from annotation import decorator

@decorator(a=2)
def run(**kwargs):
    print(kwargs)

run()