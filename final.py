
# 7 Book class
class Book:

    def __init__(self, title:str, author:str, availability:str, cost:float):

        if cost < 0 or cost > 200:
            raise ValueError        
        if not title or not author or not availability:
            raise ValueError        

        self.title = title.upper()
        self.author = author.upper()
        self.availability = availability.upper()    # "HPE"  "E" is "electronic" "
        self.base_cost = cost        

    def get_base_cost(self):
        return self.base_cost
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author

    def __eq__(self, other: object) -> bool:
        return (self.title == other.title) and (self.author == other.author)

    def get_price_for(self, quantity, kind):

        if quantity < 0 or quantity > 50:
            raise ValueError
        
        if not self.is_available_as(kind):
            return 0
        
        else:
            if kind.upper() == "H":
                cost = self.base_cost * 1.2
            elif kind.upper() == "P":
                cost = self.base_cost * 0.9
            elif kind.upper() == "E":
                cost = self.base_cost * 0.7

            price = quantity * cost
            return price

    def is_available_as(self, kind):
        if kind.upper() == "H" or kind.upper() == "HARDCOVER":
            return ("H" in self.availability)
        
        elif kind.upper() == "P" or kind.upper() == "PAPERBACK":
            return ("P" in self.availability)
        
        elif kind.upper() == "E" or kind.upper() == "ELECTRONIC":
            return ("E" in self.availability)
        
    def __str__(self) -> str:
        return f"{self.title}:{self.author}:{self.base_cost}"
        
        
# 8 Function Objects
def make_upper(word):
    return word.upper()

def make_lower(word):
    return word.lower()

def capitalize(word):
    return word.capitalize()

def apply_to_all(function, _lst):
    for i in range(len(_lst)):
        _lst[i] = function(_lst[i])

# 9. (10 pts) File Handling. 


# 10. (10 pts) Recursion


# 11. (15 pts) Write a function that meets the following specifications.


# 12. (15 pts) Equal Stacks.

