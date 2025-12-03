puzzle = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def get_invalid(first_id: int, last_id: int):
    invalid_ids = []
    for each in range(first_id, last_id + 1):
        str_id = str(each)
        start = 0
        subseq = str_id[start]
        while subseq != str_id:
            num_repeats = str_id.count(subseq)
            if subseq * num_repeats == str_id and (num_repeats >= 2):
                invalid_ids.append(each)
                break
            else:
                start += 1
                subseq = subseq + str_id[start]
    return invalid_ids


# with open("inputs/day_2/puzzle_1.txt", "r", encoding="utf8") as f:
#     puzzle = f.read()
ranges = puzzle.split(",")
invalid_ids = []
for i in range(len(ranges)):
    first_id, last_id = list(map(int, ranges[i].split("-")))

    invalid_ids.extend(get_invalid(first_id, last_id))
print(sum(invalid_ids))
