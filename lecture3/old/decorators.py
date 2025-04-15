def kwak_announce(f):
    def kip_wrapper():
        print("About to run the function")
        f()
        print("Done running the function")
    return kip_wrapper

@kwak_announce
def hello():
    print("hello world and mars")
    
hello()