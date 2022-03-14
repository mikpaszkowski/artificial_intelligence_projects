class StopConditions:
    def __init__(self, iterations=10000, desired=0.01, timeout=1000, tolerance=0.0001):
        self.maxNumOfIterations = iterations
        self.desiredValue = desired
        self.timeout = timeout
        self.tolerance = tolerance
