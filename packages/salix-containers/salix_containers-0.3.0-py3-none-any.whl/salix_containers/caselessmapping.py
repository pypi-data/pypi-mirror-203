
from collections.abc import Mapping


class CaselessMapping(Mapping):

    def __init__(self, init):
        if not isinstance(init, Mapping):
            raise ValueError('init argument must be a mapping')
        self._data = {self.norm_key(key): (key, value) for key, value in init.items()}

    @staticmethod
    def norm_key(key):
        if isinstance(key, str):
            return key.lower()
        else:
            return key

    def __getitem__(self, key):
        return self._data[self.norm_key(key)][1]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for key in self._data.keys():
            yield self._data[key][0]

    def get_raw_key_name(self, key):
        return self._data[self.norm_key(key)][0]

