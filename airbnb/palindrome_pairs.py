import collections


def palindrome_pairs(words):
    reverse, res = collections.defaultdict(int), []
    for ind, val in enumerate(words):
        reverse[val[::-1]] = ind

    for ind, val in enumerate(words):
        if val == "":
            for k, v in reverse.items():
                if k and k == k[::-1]:
                    res.append([ind, v])

        for j in range(len(val)):
            prefix, suffix = val[:j], val[j:]
            if prefix in reverse and suffix == suffix[::-1] and ind != reverse[prefix]:
                res.append([ind, reverse[prefix]])
            if suffix in reverse and prefix == prefix[::-1] and ind != reverse[suffix]:
                res.append([reverse[suffix], ind])
    return res


print(palindrome_pairs(["", "aa", "baa"]))
