def is_empty_hamsters(original_hamsters, amounth):
    all_sum = sum(sorted([hamster[0] + hamster[1] * len(original_hamsters) for hamster in original_hamsters]))
    if all_sum <= amounth:
        return True
    
def max_hamsters(amounth, count_of_hamsters, original_hamsters):
    sum_for_diff_hamsters = [0] * count_of_hamsters
    if is_empty_hamsters(original_hamsters, amounth): return count_of_hamsters
    return find_max_hamsters(0, count_of_hamsters - 1, amounth,
                             sum_for_diff_hamsters,
                             original_hamsters)

def find_max_hamsters(start_pos, end_pos, amounth,
                        sum_for_diff_hamsters,
                        original_hamsters):
    midle = (start_pos + end_pos) // 2
    food_hamsters = sorted([hamster[0] + hamster[1] * midle for hamster in original_hamsters])
    sum_food_hamsters_midle = sum(food_hamsters[:midle + 1])
    if sum_food_hamsters_midle == amounth:
        return midle
    elif sum_food_hamsters_midle < amounth:
        sum_for_diff_hamsters[midle] = sum_food_hamsters_midle
        if sum_for_diff_hamsters[midle + 1] > amounth:
            return midle + 1
        else:
            return find_max_hamsters(midle + 1, end_pos, amounth,
                                    sum_for_diff_hamsters, original_hamsters)
    else:
        sum_for_diff_hamsters[midle] = sum_food_hamsters_midle
        return find_max_hamsters(start_pos, midle - 1, amounth,
                                sum_for_diff_hamsters, original_hamsters)

print(max_hamsters(100, 2, [[1,2], [4,5], [5,0]]))  