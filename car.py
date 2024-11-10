
class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.for_sale = for_sale
        self.color = color

    def drive(self):
        print(f"You drive the {self.year} {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.year} {self.color} {self.model}")