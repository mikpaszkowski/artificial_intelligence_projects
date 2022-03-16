from prompt_toolkit.validation import Validator, ValidationError
import re

class NumberValidator(Validator):
    def validate(self, document):
        ok = re.match('\\d+(\\.\\d+)*', str(document.text))
        if not ok:
            raise ValidationError(
                message='You must provide a valid number',
                cursor_position=len(document.text)
            )
