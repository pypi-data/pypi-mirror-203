class ValidationError(Exception):

    def __init__(self, field=None, detail=None):
        self.detail = detail


class FieldInvalidDataError(Exception):

    def __init__(self, field, data=None, expected_type=None, extra=None):
        self.field = field
        self.data = data
        self.expected_type = expected_type
        self.extra = extra

    def __str__(self):
        text = f'Field {self.field} has invalid data: [{self.data}] => [{type(self.data)}]'
        if self.expected_type:
            text += f', expected type: {self.expected_type}'
        if self.extra:
            text += f', extra: {self.extra}'
        return text

