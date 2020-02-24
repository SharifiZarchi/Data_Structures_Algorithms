import random

from test_helper import *
from task import *

tests = [[57270, 70040],
 [84335, 98558],
 [29060, 43300],
 [39986, 95876],
 [89474, 91474],
 [98812, 99845],
 [60806, 70853],
 [5954, 43526],
 [14976, 47184],
 [5528, 12410],
 [61429, 93413],
 [79196, 93956],
 [87242, 96796],
 [40932, 42890],
 [25033, 87121],
 [59167, 81035],
 [9827, 93975],
 [54816, 79135],
 [36003, 45936],
 [57821, 86925],
 [82503, 86449],
 [79563, 93564],
 [80775, 83200],
 [35588, 94632],
 [72606, 75197],
 [66181, 93232],
 [4750, 69881],
 [24376, 54171],
 [30087, 45545],
 [33682, 74265],
 [57790, 90656],
 [87882, 89535],
 [34119, 83665],
 [6877, 30789],
 [55335, 73897],
 [89315, 98155],
 [87954, 98632],
 [17853, 53368],
 [30601, 84812],
 [32505, 96095],
 [1, 100000]
]


class Question:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.asked_questions = 0

    def ask(self, x, y):
        if self.asked_questions == 40:
            return random.choice([True, False])

        self.asked_questions += 1
        return (x <= self.a <= y) or (x <= self.b <= y) or (self.a <= x <= self.b) or (self.a <= y <= self.b)


if __name__ == '__main__':
    for test in tests:
        test_function(test, solve, Question(test[0], test[1]))
