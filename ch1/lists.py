
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

