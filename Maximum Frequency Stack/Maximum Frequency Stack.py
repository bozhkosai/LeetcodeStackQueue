"""freq stack"""
from collections import defaultdict, deque

class FreqStack:
    """freqstack"""
    def __init__(self):
        self.max_freq = 0
        self.stack = deque()
        self.freq = defaultdict(int)
        self.freq_list = defaultdict(list)

    def push(self, item):
        """push"""
        if item not in self.freq:
            self.freq[item] = 1
        else:
            self.freq[item] += 1
        freq = self.freq[item]
        self.freq_list[freq].append(item)
        self.max_freq = max(self.max_freq, freq)
        self.stack.appendleft(item)

    def pop(self):
        """pop"""
        elem = self.freq_list[self.max_freq].pop()
        self.freq[elem] -= 1
        self.stack.remove(elem)
        if not self.freq_list[self.max_freq]:
            self.max_freq -= 1
        return elem
