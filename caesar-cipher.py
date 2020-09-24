# encode

def let2int(c):
    return ord(c) - ord('a')


def int2let(n):
    return chr(ord('a') + n)


def shift(n,c):
    if c.islower():
        return int2let((let2int(c)+n)%26)
    return c


def encode(n,xs):
    return ''.join([shift(n,c) for c in xs])


# decode

table = [8.1, 1.5, 2.8, 4.2, 12.7, 2.2, 2.0, 6.1, 7.0,
         0.2, 0.8, 4.0, 2.4, 6.7, 7.5, 1.9, 0.1, 6.0,
         6.3, 9.0, 2.8, 1.0, 2.4, 0.2, 2.0, 0.1]

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
       'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
       's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def percent(n,m):
    return (float(n)/float(m))*100


def lowers(xs):
    return len([x for x in xs if x.islower()])


def freqs(xs):
    return [percent(xs.count(x), lowers(xs)) for x in alp]


def chisqr(os,es):
    return sum([((o-e)**2)/e for (o, e) in zip(os, es)])


def rotate(n,xs):
    return xs[n:] + xs[:n]


def positions(x,xs):
    return [i for (x1,i) in zip(xs,[j for j in range(0,len(xs))]) if x == x1]


def crack(xs):
    table1 = freqs(xs)
    chitab = [chisqr(rotate(n,table1), table) for n in range(0,26)]
    factor = positions(min(chitab),chitab)[0]
    return encode(-factor, xs)
