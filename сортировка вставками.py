def selection(sort_nums):
    for i in range(len(sort_nums)):
        index = i
        for j in range(i + 1, len(sort_nums)):
            if sort_nums[j] < sort_nums[index]:
                index = j
        sort_nums[i], sort_nums[index] = sort_nums[index], sort_nums[i]

