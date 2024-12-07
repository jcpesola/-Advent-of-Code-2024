from collections import defaultdict

with open('input.txt', 'r') as file:
    input_data = file.read()

lines = input_data.strip().split('\n')
numbers = [tuple(map(int, line.split())) for line in lines]

left_list = [pair[0] for pair in numbers]
right_list = [pair[1] for pair in numbers]

left_list.sort()
right_list.sort()

total_distance = 0

for i in range(len(left_list)):
    if left_list[i] != right_list[i]:
        difference = max(left_list[i], right_list[i]) - min(left_list[i], right_list[i])
        total_distance += difference
       
print("Total Distance: ", total_distance)

#part 2: create a similarity score
# number in left_list x frequency of times it appears in right_list --> add up 

hashmap = defaultdict(int)
for num in right_list:
    hashmap[num] += 1

similarity_score = 0
for num in left_list:
    if num in hashmap:
        similarity_score += (num * hashmap[num])

print("Similarity Score:", similarity_score)
