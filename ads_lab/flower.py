# 01. Flower

# ------ For Execution --------
# cd ads_lab
# pwd
# python flower.py


class Flower:
    def __init__(self,name: str ="unknown", petals: int=0, price: float=0.0):
        self._name = str(name)
        self._petals = str(petals)
        self._price = str(price)

    def set_name(self, name: str)-> None:
        self._name = str(name)

    def set_petals(self, petals: int)-> None:
        if petals < 0:
            raise ValueError("Number of petals cannot be negative.") 
        self._petals = int(petals)

    def set_price(self, price: float)-> None:
        if price < 0:
            raise ValueError("price cannot be negative.")
        self._price = float(price)

    def get_name(self) -> str:
        return self._name

    def get_petals(self) -> int:
        return self._petals # type: ignore
        
    def get_price(self) -> float:
        return self._price # type: ignore

    def __str__(self) -> str:
        return f"flower (name= '{self._name}', petals= {self._petals}, price= ${self._price:.2f})"
    
def main():
    rose = Flower("rose",24,5.99)
    print("Initial flower details:")
    print("rose")
    print("\n using getters:")
    print(f"Name : {rose.get_name()}")
    print(f"petals : {rose.get_petals()}")
    print(f"price : {rose.get_price()}")
    print("\n updating flower using setters....")
    rose.set_name("Red Rose")
    rose.set_petals(30)
    rose.set_price(7.49)
    print("\n updated flower details:")
    print(rose)

if __name__=="__main__":
    main()

