G = [1, 6]
Ly = [2, 7]
B = [3, 8]
Lu = [4, 9]
H = [5, 10]

fav_numbers = {
    'gary': G,
    'lyla': Ly,
    'brendan': B,
    'lucas': Lu,
    'hilda': H
    }

for name, nums in fav_numbers.items():
    print(name.title() + "'s favorite numbers are: " + str(nums[0]) + " and " + str(nums[1]))
