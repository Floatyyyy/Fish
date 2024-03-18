class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        # Længden af vektoren
        return 2

    def dot(self, u):
        # Prikprodukt mellem to vektorer
        return self.x * u.x + self.y * u.y

    def __add__(self, u):
        # Addition af to vektorer
        return Vector(self.x + u.x, self.y + u.y)

    def __sub__(self, u):
        # Subtraktion af to vektorer
        return Vector(self.x - u.x, self.y - u.y)

    def scale(self, k):
        # Skalering af vektoren med en konstant
        return Vector(k * self.x, k * self.y)

    def __eq__(self, u):
        # Sammenligning af to vektorer
        return self.x == u.x and self.y == u.y

    def __str__(self):
        # lavet om til streng for pæn udskrivning
        return f"({self.x}, {self.y})"

# Eksempel på brug:
v1 = Vector(3, 4)
v2 = Vector(4, 5)

print(len(v1))         
print(v1.dot(v2))       
print(v1 + v2)           
print(v1 - v2)           
print(v1.scale(2))       
print(v1 == Vector(3, 4))  
