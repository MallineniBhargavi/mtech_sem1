class Flower:
"""Represents a flower with a name, a petal count, and a price.
 Attributes:
 _name (str): The common name of the flower.
 _petals (int): The number of petals the flower has.
 _price (float): The price of the flower.
 """
def __init__(self, name: str = "Unknown", petals: int = 0, price: float = 0.0):
"""Initialize a new Flower instance.
 Args:
 name (str): Name of the flower. Defaults to "Unknown".
 petals (int): Number of petals. Defaults to 0.
 price (float): Price of the flower. Defaults to 0.0.
 """
self._name = str(name)
self._petals = int(petals)
self._price = float(price)