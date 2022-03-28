import re

import numpy
from prompt_toolkit.validation import Validator, ValidationError


class NumberValidator(Validator):
    def validate(self, document):
        ok = re.match('\\d+(\\.\\d+)*', str(document.text))
        if not ok:
            raise ValidationError(
                message='You must provide numeric value',
                cursor_position=len(document.text)
            )

class ProbabilityValidator(Validator):
    def validate(self, document):
        ok = re.match('\\d+(\\.\\d+)*', str(document.text))
        if not ok:
            raise ValidationError(
                message='You must provide numeric value',
                cursor_position=len(document.text)
            )
        probability = float(document.text)
        is_probability_valid = 0 <= probability <= 1
        if not is_probability_valid:
            raise ValidationError(
                message='Probability value is not valid. It must be in range <0,1>',
                cursor_position=len(document.text)
            )




class IntegerValidator(Validator):
    def validate(self, document):
        ok = re.match('^\\d+$', str(document.text))
        if not ok:
            raise ValidationError(
                message='You must provide a valid integer number',
                cursor_position=len(document.text)
            )


class PositiveIntegerValidator(Validator):
    def validate(self, document):
        ok = re.match('^\\d+$', str(document.text))
        if not ok:
            raise ValidationError(
                message='You must provide a valid integer number',
                cursor_position=len(document.text)
            )
        if int(document.text) < 1:
            raise ValidationError(
                message='Integer must be >= 1',
                cursor_position=len(document.text)
            )


class SymmetricMatrixValidator(Validator):
    def validate(self, document):
        row, col = numpy.matrix(document.text).shape
        ok = row == col
        if not ok:
            raise ValidationError(
                message="Matrix should be symmetric!",
                cursor_position=len(document.text)
            )


class VectorValidator(Validator):
    def validate(self, document):
        matrix = numpy.matrix(document.text)
        row, col = matrix.shape
        ok = col == 1
        if not ok:
            raise ValidationError(
                message="Provided vector is not valid!",
                cursor_position=len(document.text)
            )
