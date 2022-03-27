from enum import Enum, unique


@unique
class MethodType(Enum):
    GRADIENT_DESCENT = 'Gradient Descent'
    NEWTON = 'Newton'

    def fromString(value):
        if value == 'Gradient Descent':
            return MethodType.GRADIENT_DESCENT
        elif value == 'Newton':
            return MethodType.NEWTON
        else:
            raise TypeError("There is enum of type ", value)


@unique
class StartingPointType(Enum):
    MANUAL = 'Defined manually',
    RANDOM = 'Randomly generated'

    def fromString(value):
        if value == 'Defined manually':
            return StartingPointType.MANUAL
        elif value == 'Randomly generated':
            return StartingPointType.RANDOM
        else:
            raise TypeError("There is enum of type ", value)


@unique
class FunctionType(Enum):
    SCALAR = 'F(x)'
    VECTOR = 'G(x)'

    def fromString(value):
        if value == 'F(x)':
            return FunctionType.SCALAR
        elif value == 'G(x)':
            return FunctionType.VECTOR
        else:
            raise TypeError("There is enum of type ", value)


@unique
class StoppingConditionType(Enum):
    ITERATIONS = 'Maximal iterations',
    DESIRED_VALUE = "Desired value",
    TIMEOUT = "Timeout"

    def fromString(value):
        if value == 'Maximal iterations':
            return StoppingConditionType.ITERATIONS
        elif value == "Desired value":
            return StoppingConditionType.DESIRED_VALUE
        elif value == "Timeout":
            return StoppingConditionType.TIMEOUT
        else:
            raise TypeError("There is enum of type ", value)