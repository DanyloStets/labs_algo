def find_needle_indices(haystack, needle):
    transition = transmition_to_bad_table(needle)
    n, m = len(haystack), len(needle)
    state = 0
    indices = []
    for i in range(n):
        state = transition[state].get(haystack[i], 0)
        print(state)
        if state == m:
            indices.append(i - m + 1)
    return indices

def transmition_to_bad_table(needle):
    m = len(needle)
    transition = [{} for _ in range(m + 1)]
    print(transition)
    for state in range(m + 1):
        for char in set(needle):
            k = min(m, state + 1)
            while k > 0 and needle[:k] != needle[state - k + 1:state] + char:
                k -= 1
            transition[state][char] = k
        print(transition)
    return transition


# find_needle_indices(haystack, needle)



# def get_unique_chars_from_string(pattern):
#     return list(set(pattern))

# if __name__ == '__main__':
#     print(find_the_indices_of_all_occurrences("ababaca", "ababacababacabbb"))