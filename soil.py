class Soil:
    def __init__(self, name='', irrigation=-1, acidity=-1):
        self._name = name
        self._irrigation = irrigation
        self._acidity = acidity

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_acidity(self):
        return self._acidity

    def set_acidity(self, acidity):
        self._acidity = acidity

    def get_irrigation(self):
        return self._irrigation

    def set_irrigation(self, irrigation):
        self._irrigation = irrigation
