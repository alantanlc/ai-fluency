import math

class LinearSupportVectorMachine:

    def __init__(self, zeros: list, ones: list):
        self.weight = 0
        self.bias = 0
        self.zeros = zeros
        self.ones = ones

    def train(self):
        # find the two support vectors (points) with the minimum distance
        min_dist = float('infinity')
        d0, d1 = None, None
        for p0 in zeros:
            for p1 in ones:
                dist = math.dist(p0, p1)
                if dist < min_dist:
                    min_dist = dist
                    d0, d1 = p0, p1

        # compute the weight and bias
        x1, y1 = d0
        x2, y2 = d1

        # weight
        self.weight = -(x2-x1)/(y2-y1)

        # bias
        mid_x = (x1+x2)/2
        mid_y = (y1+y2)/2
        self.bias = mid_y - self.weight * mid_x

    def test(self, x: float, y: float) -> float:
        # given input xy, and learned weight and bias, predict the output label
        c = y - self.weight * x
        return 0 if c < self.bias else 1

    def eval(self) -> float:
        pass

if __name__ == '__main__':
    # train
    zeros = [(0,0)]
    ones = [(1,1)]
    model = LinearSupportVectorMachine(zeros, ones)
    model.train()

    # test
    print(f'{model.test(2,2)=}')
    print(f'{model.test(-1,-1)=}')
    print(f'{model.test(0.5,0.5)=}')
    print(f'{model.test(0.49,0.49)=}')

