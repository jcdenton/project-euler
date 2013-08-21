from itertools import imap, izip
from operator import itemgetter


class CollatzDict(dict):
    def __init__(self):
        super(CollatzDict, self).__init__({0: 1, 1: 1})

    def get(self, k, d=None):
        value = super(CollatzDict, self).get(k, d)
        if value is None:
            if k % 2 == 0:
                value = 1 + self.get(k / 2)
            else:
                value = 1 + self.get(3 * k + 1)
            self[k] = value
        return value


values = CollatzDict()

print next(iter(sorted(
    izip(xrange(10 ** 6),
         imap(values.get, xrange(10 ** 6))),
    reverse=True,
    key=itemgetter(1))))
