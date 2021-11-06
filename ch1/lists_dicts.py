"""
Most important methods of a list this usage:
    len(L) returns the number of elements of the list L O(1)
    sorted(L) returns a sorted copy of the list L O(n log n)
    L.sort() sorts L in place O(n log n)
    L.count(c) the number of occurrences of c in L O(n)
    c in L is the element c found in L? O(n)
    L.append(c) append c to the end of L amortised O(1)
    L.pop() extracts and returns the last element of L amortised O(1)

    Ranges and Other Iterators
    To loop over ranges of integers, the code for i in range(n): can be used to run over
    the integers from 0 to n − 1. Several variants exist:
    range(k, n) from k to n − 1
    range(k, n, 2) from k to n − 1 two by two
    range(n - 1, -1, -1) from n − 1 to 0 (−1 excluded) in decreasing order.

"""
my_list = ["Hola", 1, True, 3.4, "Salut"]

months = ["january", "february", "march", "april", "may", "june", "july", "august",
          "september", "october", "november", "december"]

MONTH_OPTIONS = [(i, i.title()) for i in months]

nums = [(i, str(i)) for i in range(1, 11)]
print(nums[::-2])

print([i for i in my_list])
print(my_list[2:])  # Elements from such index and onwards: 0, 2
print(my_list[1:3])  # Elements from that index to the specified
print(my_list[:3])  # Elements before index 3: 0, 1, 2
print(my_list[-3:])  # The last 3 elements

# Elements from ith up to (but not including) the jth, taking only
# every th element.
print(nums[2:10:15])

print(my_list[::2])  # Elements with even indices
print(my_list[::-1])  # A reverse copy

val = [index for index in range(len(my_list))]
print(val)

n = 5
squared_nums = [x ** 2 for x in range(n + 1)]
print(squared_nums)

# Initialize a list of n
t = [0 for _ in range(n)]  # [0, 0, 0, 0, 0]
print(t)

# Initialize counters for the letters in a string, dictionary comprehension.
my_string = "cowboy"
nb_occurrences = {letter: 0 for letter in my_string}  # {'c': 0, 'o': 0, 'w': 0, 'b': 0, 'y': 0}
print(nb_occurrences)

# A Dictionary comprehension example equivalent
nb_occurrences2 = {}
for letter in my_string:
    nb_occurrences2[letter] = 0

print(nb_occurrences2)


def all_pairs(ma_list):
    k = len(ma_list)
    for i in range(k):
        for j in range(i + 1, k):
            yield ma_list[i], my_list[j]


num_list = [i for i in range(1, 11)]
pair_nums = all_pairs(num_list)
print(pair_nums)
