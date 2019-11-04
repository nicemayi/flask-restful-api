class ZW:
    name = 'zw'
    age = 34

    def __init__(self):
        self.gender = 'male'
    
    def keys(self):
        print('called me first')
        return ('name', 'age', 'gender',)
    
    def __getitem__(self, item):
        print('then me')
        return getattr(o, item)


o = ZW()
# print(o['name'])
# print(o['age'])
# print(o['gender'])
# print(o['gender1111'])

dict(o)
