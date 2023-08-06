class DigitalUnit:
    def __init__(self) -> None:
        self.type = "NONE"
    

class Lenth(DigitalUnit):
    def __init__(self) -> None:
        self.type = 'Lenth'

class Metre(Lenth):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 1.0
    def __str__(self) -> str:
        return 'm'

class KiloMetre(Lenth):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 1000.0
    def __str__(self) -> str:
        return 'km'

class CentiMeter(Lenth):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 0.01
    def __str__(self) -> str:
        return 'cm'

class MilliMeter(Lenth):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 0.001
    def __str__(self) -> str:
        return 'mm'


class Area(DigitalUnit):
    def __init__(self) -> None:
        self.type = 'Area'

class SquareMeter(Area):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 1.0 
    def __str__(self) -> str:
        return 'm²'

class SquareKiloMeter(Area):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 1000_000.0
    def __str__(self) -> str:
        return 'km²'

class Hectare(Area):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 10_000.0
    def __str__(self) -> str:
        return 'hm²'

class SquareCentiMeter(Area):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 1.0
    def __str__(self) -> str:
        return 'cm²'

class Number:
    def __init__(self, number, unit) -> None:
        self.digital_part = number
        if unit.__class__.__base__.__base__ == DigitalUnit:
            self.unit = unit
        else:
            print(unit.__class__.__base__.__base__)
            raise TypeError('You should set the unit parameter to numerical units.')

    def change_unit(self, new_unit):
        if new_unit.__class__.__base__.__base__ == DigitalUnit:
            if new_unit.type == self.unit.type:
                self.digital_part = self.digital_part * self.unit.measure / new_unit.measure
                self.unit = new_unit
            else:
                raise TypeError('Different unit types')
        else:
            raise TypeError('You should set the unit parameter to numerical units.')
    
    def __str__(self) -> str:
        return f'{self.digital_part}{self.unit}'
    
if __name__ == '__main__':
    _1cm = Number(1.0, CentiMeter()) # Create the data. Don't forget the parentheses!
    print(_1cm)
    _1cm.change_unit(MilliMeter()) # Changes to the unit. Don't forget the parentheses!
    print(_1cm)