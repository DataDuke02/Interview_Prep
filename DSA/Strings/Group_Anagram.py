def group_anagrams(strs):
    groups = {}

    for word in strs:
        key = "".join(sorted(word))  # sort chars alphabetically
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# [["eat","tea","ate"], ["tan","nat"], ["bat"]]