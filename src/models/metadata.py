class Metadata:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def to_dict(self):
        return self.__dict__

    def __repr__(self):
        return f"Metadata({self.to_dict()})"