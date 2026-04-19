class phone:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def use(self, minutes):
        self.battery -= 0.5 * minutes
        print(self.battery) #my_phone이라 하면 안된다.
        #배터리 사용량에 따라 전량을 차감시키고 print
    def charge(self, minutes):
        self.battery += minutes
        print(self.battery)
        #배터리 사용량에 따라 전량을 증가시키고 print

my_phone = phone("galaxy", 80)

my_phone.use(30)
my_phone.charge(20)
