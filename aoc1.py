sumA = 0
sumB = 0
digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
with open('input1.txt', 'r') as source:
    for line in source.read().splitlines():
        print('line: ', line)
        nums = [int(i) for i in line if i.isdigit()]
        sumA += nums[0] * 10 + nums[-1]
        start = ''
        end = ''
        for j in line:
            if j.isdigit():
                sumB += int(j) * 10
                break

            start += j
            for k, v in digits.items():
                start = start.replace(k, str(v))

            if start[-1].isdigit():
                sumB += int(start[-1]) * 10
                break

        for j in line[::-1]:
            if j.isdigit():
                sumB += int(j)
                break

            end = j + end

            for k, v in digits.items():
                end = end.replace(k, str(v))
            if end[0].isdigit():
                sumB += int(end[0])
                break

print('part A: ', sumA)
print('Part B: ', sumB)
