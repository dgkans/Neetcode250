from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.val = {}                        # key -> value
        self.freq = {}                       # key -> freq
        self.group = defaultdict(OrderedDict)  # freq -> OrderedDict of keys (LRU within freq)
        self.minf = 0                        # current minimum frequency

    def _bump(self, key: int, new_value=None) -> None:
        """Increase a key's frequency and keep LRU order within the new bucket."""
        if new_value is not None:
            self.val[key] = new_value

        f = self.freq[key]
        # remove from old freq bucket
        od = self.group[f]
        od.pop(key, None)
        if not od:
            del self.group[f]
            if self.minf == f:
                self.minf += 1

        # add to new freq bucket at MRU end
        f2 = f + 1
        self.freq[key] = f2
        self.group[f2][key] = None

    def get(self, key: int) -> int:
        if self.cap == 0 or key not in self.val:
            return -1
        self._bump(key)
        return self.val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.val:
            # update value and bump frequency
            self._bump(key, new_value=value)
            return

        # evict if full: LFU, tie-broken by LRU within that freq
        if len(self.val) == self.cap:
            od = self.group[self.minf]
            evict_key, _ = od.popitem(last=False)  # LRU in the min-freq bucket
            del self.val[evict_key]
            del self.freq[evict_key]
            if not od:
                del self.group[self.minf]

        # insert new key with freq = 1
        self.val[key] = value
        self.freq[key] = 1
        self.group[1][key] = None
        self.minf = 1
