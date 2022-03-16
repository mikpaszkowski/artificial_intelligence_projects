from prompt_toolkit.validation import Validator, ValidationError
import re

class NumberValidator(Validator):
    def validate(self, document):
        ok = re.match('\\d+(\\.\\d+)*', str(document.text))
        if not ok:
            raise ValidationError(
                message='You must provide numeric value',
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