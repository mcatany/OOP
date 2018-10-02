# Instance vs class attributes

class MyClass:
        
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var

# Example of usage
if __name__ == "__main__":			
	foo = MyClass(2)
	bar = MyClass(3)
