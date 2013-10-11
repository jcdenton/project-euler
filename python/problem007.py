from collections import deque
from itertools import takewhile, imap
from operator import itemgetter

from util import primes


print deque(
    imap(itemgetter(1),
         takewhile(lambda (i, v): i < 10001, enumerate(primes()))),
    maxlen=1).pop()
