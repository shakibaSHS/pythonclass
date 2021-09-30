class car():
    def __init__(self,brand,motor,current_speed):
        self.brand=brand
        self.current_speed=int(current_speed)
        self.motor=motor

    def gaz_bede(self):
        if self.current_speed >89:
            print('sorat reside be 100 nemishe ziad beshe')
        else:
            self.current_speed +=10
            print('daram sorat {} km/h miram'.format(self.current_speed))

my_new_car= car('bmw', '8_supap', 90)

print('gaze aval')
my_new_car.gaz_bede()
print('gaze 2')
my_new_car.gaz_bede()
