def valid_number(lottery_numbers):
    try:
        for number in lottery_numbers:
            if int(number) < 0 or int(number) > 40:
                return False
        return True
    except(ValueError, NameError):
        return False

def filter_incorrect():
    try:
        with open('lottery_numbers.csv') as f, open("correct_numbers.csv", "w") as fc:
            for line in f:
                if line:
                    week_data = line.strip().split(';')
                else:
                    continue
                week = week_data[0].split()   
                try:
                    if week[0] != 'week' or int(week[1]) < 0 or int(week[1]) > 52:
                        continue      
                    else: 
                        lottery_numbers = week_data[1].split(',')   
                        duplicates = [i for i in set(lottery_numbers) if lottery_numbers.count(i) > 1]  
                        if not duplicates:
                            if  len(lottery_numbers) == 7 and valid_number(lottery_numbers):
                                lottery_numbers_string = ",".join(lottery_numbers)
                                fc.write(f'{week[0]} {week[1]};{lottery_numbers_string}\n')         
                except (ValueError, IndexError, NameError):
                    continue

    except (FileExistsError, ValueError):
        print("no file exists")

if __name__ == '__main__':
    filter_incorrect()





