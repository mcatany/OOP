# Inheritance 

# Parent class

class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoIsThis(self):
        print("Bird")
    
    def swim(self):
        print("Swim faster")

# Child class:

class Penguin(Bird):
    
    def __init__(self):
        #call super() function
        super().__init__()
        print("Penguin is ready")

    def whoIsThis(self):
        print("Penguin")

    def run(Self):
        print("Run faster")

# Example of usage
if __name__ == "__main__":			
	peggy = Penguin()
	peggy.whoIsThis()
	peggy.swim()
	peggy.run()
