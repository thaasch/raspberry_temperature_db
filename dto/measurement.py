class Measurement:
    def __int__(self, **kwargs):
        self.name = kwargs['name']
        self.value = kwargs['value']
        self.timestamp = kwargs['timestamp']
