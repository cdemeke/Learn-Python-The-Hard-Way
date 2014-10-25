sample_list = "blue green yellow black white purple brown orange tan watermelon"

array_sample_list = sample_list.split(' ')
print array_sample_list

sorted_sample_list = sorted(array_sample_list, key = len)
print sorted_sample_list