from random import choice

class RandomWalk():
    """Class for modeling a simple random walk"""
    def __init__(self, num_points = 5000):
        """Basic constructor"""
        self.num_points = num_points
        # Lists for random walk
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Function for each step"""
        direction = choice([-1, 1]);
        step = choice([0,1,2,3,4])
        return direction * step


    def fill_walk(self):
        """Method for filling walk"""
        while len(self.x_values) < self.num_points:
            # Choose x
            x_distance = self.get_step()
            # Choose y
            y_distance = self.get_step()
            # Case 0 0
            if x_distance == 0 and y_distance ==0:
                continue
            # Set next step
            next_x = self.x_values[-1] + x_distance
            next_y = self.y_values[-1] + y_distance
            # Append it to list
            self.x_values.append(next_x)
            self.y_values.append(next_y)


