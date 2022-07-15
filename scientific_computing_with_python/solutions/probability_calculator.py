import copy
import random


class Hat:
    # balls being added during init
    contents = []
    # balls for draw method
    drawn_balls = []

    # seed for testing
    # random.seed(95)

    def __init__(self, **balls):
        # put individual balls in a list
        self.contents = []
        for b, n in balls.items():
            for i in range(n):
                self.contents.append(b)

    # make objects in this class return the contents of Hat when called
    def __str__(self):
        return f"{self.contents}"

    # draw a random ball and remove it from the list once it's drawn
    def draw(self, numdraws):
        drawn_balls = []
        if numdraws >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls

        else:
            for i in range(numdraws):
                randint = random.choice(self.contents)
                drawn_balls.append(randint)
                self.contents.remove(randint)
            return sorted(drawn_balls)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(num_experiments):
        # make sure contents don't actually get deleted from the hat
        new_hat = copy.deepcopy(hat)
        # make sure the desired outcome don't get deleted from input
        desired_outcome = copy.deepcopy(expected_balls)
        # map each tests draw to a variable for use
        this_exp = new_hat.draw(num_balls_drawn).copy()
        print(this_exp)
        for ball in this_exp:
            if ball in desired_outcome.keys():
                desired_outcome[ball] = desired_outcome.get(ball, 0) - 1

        if all(value <= 0 for value in desired_outcome.values()) is True:
            success += 1

    return success / num_experiments


# testing area
dog = Hat(red=10, blue=5)
print(experiment(hat=dog, expected_balls={"red": 1, "blue": 2}, num_balls_drawn=5, num_experiments=10))
