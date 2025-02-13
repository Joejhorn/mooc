# Write your solution here:
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

    def __str__(self):
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished}'

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
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
            return [order for order in self.orders if order.finished == 'NOT FINISHED' and order.programmer == progammer]
        else:
            return [order for order in self.orders if order.finished == 'NOT FINISHED']

    def status_of_programmer(self, programmer):
        for pro in self.orders:
            if pro.programmer == programmer:
                sum_finished = self.finished_orders(programmer)
                sum_unfinished = self.unfinished_orders(programmer)
                hours_finished = [info.workload for info in sum_finished if info.finished == 'FINISHED']
                hours_unfinished = [info.workload for info in sum_unfinished if info.finished == 'NOT FINISHED']
                return ((len(sum_finished)), len(sum_unfinished), sum(hours_finished), sum(hours_unfinished))
        raise ValueError


if __name__ == '__main__':
    t = OrderBook()
    t.add_order("program webstore", "Andy", 10)
    t.status_of_programmer("JohnDoe")