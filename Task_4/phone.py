class Phone:
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be a 10-digit number.")
        self.value = value

    def __str__(self):
        return str(self.value)
