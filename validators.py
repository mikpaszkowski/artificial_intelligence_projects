from prompt_toolkit.validation import Validator, ValidationError


class CoefficientValidator(Validator):
    def validate(self, document):
        ok = str(document.text).isdigit()
        if not ok:
            raise ValidationError(
                message='Function coefficient must be a number',
                cursor_position=len(document.text)
            )
