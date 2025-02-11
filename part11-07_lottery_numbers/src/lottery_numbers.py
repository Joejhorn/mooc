# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week_num, lottery_numbers):
        self.week_num = week_num
        self.lottery_numbers = lottery_numbers
    
    def number_of_hits(self, lottery_numbers):
        return len([number for number in lottery_numbers if number in self.lottery_numbers])

    def hits_in_place(self, numbers):
        return [number if number in self.lottery_numbers else -1 for number in numbers]

if __name__ == '__main__':
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))