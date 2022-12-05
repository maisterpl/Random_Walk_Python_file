from random import choice

class RandomWalk():
    def __init__(self, num_points = 5000) -> None:
        # inicialize how many points to create
        self.num_points = num_points

        # start points is 0, 0
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.__get_step_x()
            y_step = self.__get_step_y()

            if x_step == 0 and y_step == 0: continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def __get_step_x(self):
        x_direction = choice([1, -1])
        x_distance = choice([i for i in range(5)])  # [0, 1, 2, 3, 4]
        x_step = x_distance * x_direction
        return x_step

    def __get_step_y(self):
        y_direction = choice([1, -1])
        y_distance = choice([i for i in range(5)])  # [0, 1, 2, 3, 4]
        y_step = y_distance * y_direction
        return y_step

