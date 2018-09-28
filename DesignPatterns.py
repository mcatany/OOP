# Design Patterns

# Decorator

def sum(func):
	s = 0
	for i in func():
		s += i
	return s

def interate():
	a = []
	for i in range(10):
		a.append(i)
	return a

print(sum(interate))