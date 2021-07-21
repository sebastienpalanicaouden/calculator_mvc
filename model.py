class Model:
    def __init__(self):
        self.value = ''
        self.operator = ''
        self.previous_value = ''

    def calculate(self, caption):
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''
        elif caption =='+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
        elif caption == '%':
            value = float(self.value) if '.' in self.value else int(self.value)
            self.value = str(value / 100)
        elif caption == '=':
            if self.value and self.operator and self.previous_value:
                self.value = str(self._evaluate())
        elif caption == '.':
            if not caption in self.value:
                self.value += caption
        elif isinstance(caption, int):
            self.value += str(caption)
        else:
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value = ''
        
        return self.value
    
    def _evaluate(self):
        self.result = eval(self.previous_value + self.operator + self.value)
        if int(self.result) == self.result:
            self.result = int(self.result)
        return self.result