# These functions are derived from algorithms described in "K-M-P String Matching Revisited"
# https://drive.google.com/file/d/13jhYrPdJfF8HFycLtDgu8IIGnsZGB7sy/view
# Copyright 1997, Elsevier Science B.V.

# Specification: Return position of the first occurrence of
# pattern (needle) in text (haystack) (or -1 if pattern does not occur in text).

Prefix = []

def KMPmatch(needle, haystack):
    global Prefix
    Prefix = [-1] * len(needle)
    return match(needle, 0, haystack, 0)

def match(needle, m, haystack, n):

    if (m == len(needle)):
        return n-m # match
    if (n == len(haystack)):
        return -1 # no match
    newM = extend(needle, m, haystack[n])
    return match(needle, newM, haystack, n+1)

def extend(needle, j, c):
    if (needle[j] == c):
        return j+1
    if (j == 0):
        return 0
    return extend(needle, prefix(needle, j), c)

def prefix(needle, i):
    global Prefix
    if (Prefix[i] == -1):
        if (i == 1):
            Prefix[i] = 0
        else:
            Prefix[i] = extend(needle, prefix(needle, i-1), needle[i-1])
    return Prefix[i]

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus