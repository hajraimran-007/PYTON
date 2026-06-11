#Given a list of strings strs, group the anagrams together. You can return the answer in any order.
def groupAnagrams(strs):
    groups = {}

    for word in strs:
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


# Example
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))