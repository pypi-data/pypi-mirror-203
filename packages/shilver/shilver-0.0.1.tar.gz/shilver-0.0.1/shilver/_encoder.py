
class Restriction:
    def __init__(self, position, number):
        self.position = position
        self.number = number
    
    def to_asp_fact(self):
        raise NotImplementedError('This class is not intended to be instanciated')

    def _to_asp_fact(self):
        return f'(vtx{self.position}, {self.number}).'

class White(Restriction):
    def to_asp_fact(self):
        return f'white{super()._to_asp_fact()}'
    
class Black(Restriction):
    def to_asp_fact(self):
        return f'black{super()._to_asp_fact()}'


class Encoder:

    def from_file(self, input_file):
        with open(input_file, 'r') as file:
            return self.from_text(file.read())

    def from_text(self, input_text):
        lines = input_text.strip().replace('  ',' ').split('\n')      
        y = len(lines)
        gridsize_fact = f'gridsize({y}).\n'
        circles = []
        for l in lines:
            x = 1
            for v in l.strip().split(' '):
                if   int(v) < 0:
                    circles.append(Black((x,y), abs(int(v))))
                elif int(v) > 0:
                    circles.append(White((x,y), v))
                x+=1
            y-=1
        return gridsize_fact + f'\n'.join([c.to_asp_fact() for c in circles])
