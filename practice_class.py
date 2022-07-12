class unit:
    def __init__(self):
        print("unit 생성자")
class flyable:
    def __init__(self):
        print("flyable 생성자")

class flyableUnit(unit,flyable):
    def __init__(self):
        #super().__init__() 문제생김
        unit.__init__(self)
        flyable.__init__(self)

drop = flyableUnit()