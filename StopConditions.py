class StopConditions:
    def __init__(self, tolerance = 0.0001, value=100, stoppingConditionType='Maximal iterations'):
        self.value = value
        self.tolerance = tolerance
        self.stoppingConditionType = stoppingConditionType
