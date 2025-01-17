# Tee ratkaisusi tähän:
class DecreasingCounter:
    orginal_value = 0

    def __init__(self, initial_value: int):
        self.value = initial_value
        DecreasingCounter.orginal_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 1:
            self.value -= 1
        else:
            self.value = 0
    def set_to_zero(self):
        self.value = 0
    
    def reset_original_value(self):
        self.value = DecreasingCounter.orginal_value



    # Write the rest of the methods here!
if __name__ == '__main__':
    counter = DecreasingCounter(10)
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter = DecreasingCounter(100)
    counter.print_value()
    counter.set_to_zero()
    counter.print_value()