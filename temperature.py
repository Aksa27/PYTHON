class temperture():
    def __init__(self,temperature):
        self.temp=temperature
    def convert_fahrenheit(self):
        self.convert_fahrenheit=self.temp*(9/5)+32
        return self.convert_fahrenheit
    def covert_celcius(self):
        self.covert_celcius=(self.temp-32)*5/9
        return self.covert_celcius
r=int(input("enter the temperature:"))    
temperture=temperture(r)
print("fahrenheit:",temperture.convert_fahrenheit())
print("celcius:",temperture.covert_celcius())
    