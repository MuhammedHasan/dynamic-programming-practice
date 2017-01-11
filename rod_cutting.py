import math


class RodCutter(object):

    def __init__(self, prices):
        self.prices = prices
        self.memory = dict()

    def cut_road(self, road_length):
        if road_length == 0:
            return 0
        profit = -math.inf
        for i, v in enumerate(self.prices):
            i += 1
            if road_length >= i:
                t_profit = v + self.cut_road(road_length - i)
                profit = max(profit, t_profit)
        return profit

    def memorized_cut_rod(self, road_length):
        self.memory = dict()
        return self.memorized_cut_rod_x(road_length)

    def memorized_cut_rod_x(self, road_length):
        if self.memory.get(road_length):
            return self.memory[road_length]
        if road_length == 0:
            profit = 0
        else:
            profit = -math.inf
            for i, v in enumerate(self.prices):
                i += 1
                if road_length >= i:
                    t_profit = v + self.memorized_cut_rod_x(road_length - i)
                    profit = max(profit, t_profit)
        self.memory[road_length] = profit
        return profit

    def bottom_up_cut_rod(self, road_length):
        memory = {0: 0}
        for j in range(1, road_length + 1):
            profit = -math.inf
            for i, p in enumerate(self.prices):
                i += 1
                if j >= i:
                    t_profit = p + memory[j - i]
                    profit = max(profit, t_profit)
            memory[j] = profit

        return memory[road_length]

    def bottom_up_cut_rod_solutions_table(self, road_length):
        memory = {0: 0}
        solutions = {0: 0}
        for j in range(1, road_length + 1):
            profit = -math.inf
            for i, p in enumerate(self.prices):
                i += 1
                if j >= i:
                    t_profit = p + memory[j - i]
                    if profit < t_profit:
                        profit = t_profit
                        solutions[j] = i
            memory[j] = profit

        return solutions

    def solution_of_rod(self, road_length):
        solutions_table = self.bottom_up_cut_rod_solutions_table(road_length)
        while road_length > 0:
            yield solutions_table[road_length]
            road_length = road_length - solutions_table[road_length]
