# function to check if index is even in a list and append it to a new list
# and return that new list (line 7-9)

def sum_of_even(nums):
    new_list = []
    for i in nums:
        if (i % 2) == 0:
            new_list.append(i)
            total = sum(new_list)
        else:
            total = 0
    print(total)
    return total


sum_of_even()

# function to calculate mediam, the calculations happen from line 27 to 32
# line 27 checks from index 0 looking for the mediam in the lower half
# line 28 checks the upper half of the list (in reverse) and we find the
# mediam in line 30


def calculate_mediam(nums):
    nums.sort()
    lnth = len(nums)

    if lnth // 2 == 0:
        median_1 = nums[lnth // 2]
        median_2 = nums[lnth // 2 - 1]
        median = (median_1 + median_2) / 2
    else:
        median = nums[lnth // 2]

    print(median)


nums = [2, 4, 6]
calculate_mediam(nums)

# Function the loops through a given list to find a missing number


def find_missing_number(nums):
    nums.sort()

    if not nums:
        return None
    else:
        max = nums[0]
        for i in nums:
            if i > max:
                max = i

        min = nums[0]
        for i in nums:
            if i < min:
                min = i

        lst = []

        for num in range(min + 1, max):
            if num not in nums:
                lst.append(num)

        return lst


nums = [2, 3, 4]
print(find_missing_number(nums))

# A function that removes duplicate characters in a string


def remove_duplicates(str):
    s = ""

    for char in str:
        if char not in s:
            s = s + char
    return s


string = "STEVE"
print(remove_duplicates(string))

# Function that removes the first characters in a string that
# do not repeat


def first_non_repeating_char(str):
    new_str = []
    new_form = []

    for i in range(0, len(str)):
        if i == 0:
            return None
        else:
            if str[i] not in new_str:
                new_str += str[i]
    new_form.append("".join(new_str))
    new_form.append(len(new_form[0]))
    return new_form


string = "Steve"
print(first_non_repeating_char(string))
