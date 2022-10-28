class FourDigitYearConverter:
    regex = '[0-9]{4}'
    
    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return f'{value:4d}'  # where 4 is the 4 digit space and 'd' for the integer
        # or 
        # return '%04d' % value  # in seashell