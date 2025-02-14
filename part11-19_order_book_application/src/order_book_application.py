# Write your solution here:
import sys
class Task:
    id = 0

    def __init__(self, description, programmer, workload,  finished = 'NOT FINISHED'):
        self.id = Task.id + 1
        Task.id += 1
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.finished = finished

    def is_finished(self):
        return self.finished == 'FINISHED'
    
    def mark_finished(self):
        self.finished = "FINISHED"

    # def __repr__(self):
    #     return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished}'

    def __str__(self):
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished}'

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        for order in self.orders:
            if order.description == description:
                order.programmer = programmer
                order.workload = workload
                return
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return [order for order in self.orders]

    def programmers(self):
        programmers = [programmer.programmer for programmer in self.orders]
        return list(set(programmers))

    def mark_finished(self, int):
        for order in self.orders:
            if order.id == int:
                order.finished = "FINISHED"
                return
        raise ValueError('No id exists')

    def finished_orders(self, *argv):
        if argv:
            progammer = argv[0]
            return [order for order in self.orders if order.finished == 'FINISHED' and order.programmer == progammer]
        else:
            return [order for order in self.orders if order.finished == 'FINISHED']

    def unfinished_orders(self, *argv):
        if argv:
            progammer = argv[0]
            return ([order for order in self.orders if order.finished == 'NOT FINISHED' and order.programmer == progammer])
        else:
            return( [order for order in self.orders if order.finished == 'NOT FINISHED'])


    def status_of_programmer(self, programmer):
        for pro in self.orders:
            if pro.programmer == programmer:
                sum_finished = self.finished_orders(programmer)
                sum_unfinished = self.unfinished_orders(programmer)
                hours_finished = [info.workload for info in sum_finished if info.finished == 'FINISHED']
                hours_unfinished = [info.workload for info in sum_unfinished if info.finished == 'NOT FINISHED']
                breakpoint
                return ((len(sum_finished)), len(sum_unfinished), sum(hours_finished), sum(hours_unfinished))
        raise ValueError

class MenuOperation:
    def __init__(self):
        #was just messing around with this to see how to call a function form a variable
        #once I realized I couldn't do it the way the program demanded I went away from finishing
        #it. So that is why some is this way and the other stuff is handled in the command function
        self.command_options = [self.exit, self.add_order, None, self.unfinished_orders]

    def print_menu(self):
        print('commands:')     
        print('0 exit')
        print('1 add order')
        print('2 list finished tasks')
        print('3 list unfinished tasks')
        print('4 mark task as finished')
        print('5 programmers')
        print('6 status of programmer')

    def exit(self):
        sys.exit(0)

    def add_order(self, orders):
        try:
            description = input('description: ')
            programer, workload = input('programmer and workload estimate: ').split()
            orders.add_order(description, programer, int(workload))
            print('added!')
        except ValueError:
            print('erroneous input')
    
    def unfinished_orders(self, orders):
        orders = orders.unfinished_orders()
        if len(orders) == 0:
            print('no unfinished tasks')
        else:
            for order in orders:
                print(order)

    def finished_orders(self, orders):
        orders = orders.finished_orders()
        if len(orders) == 0:
            print('no finished tasks')
        else:
            for order in orders:
                print(order)

   
    def get_command(self, orders):
        while True:
            print()
            try:
                command = int(input('command: '))
                if command == 0:
                    break
                elif command == 2:
                    self.finished_orders(orders)
                elif command == 4:
                    id = int(input('id: '))
                    orders.mark_finished(id)
                    print('marked as finished')
                    continue
                elif command == 5:
                    programmers = orders.programmers()
                    for programer in programmers:
                        print(programer)
                elif command == 6:
                    name = input('programmer: ')
                    status = orders.status_of_programmer(name)
                    print(f'tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}')
                else:
                    self.command_options[command](orders)
            except (ValueError,IndexError):
                print('erroneous input')
        

orders = OrderBook()
orders.unfinished_orders()
menu = MenuOperation()
menu.print_menu()
menu.get_command(orders)







    
