class employee():
    def __init__(self):
        print(" employee created")
    def __del__(self):
        print("employee deleted")
def create_obj():
    print("creating object")
    obj = employee()
    print("object created")
    return obj
print("calling the create_obj function")
obj = create_obj()
print("object returned from create_obj function")
