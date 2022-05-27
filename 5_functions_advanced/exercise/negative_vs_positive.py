def negative_vs_positive(nums):
    positives = []
    negatives = []
    result = ''
    for el in nums:
        if el > 0:
            positives.append(el)
        else:
            negatives.append(el)
    pos_sum = sum(positives)
    neg_sum = sum(negatives)
    result = f"{neg_sum}\n{pos_sum}"
    if abs(neg_sum) > pos_sum:
        result += '\n' + "The negatives are stronger than the positives"
    else:
        result += '\n' + "The positives are stronger than the negatives"
    return result


numbers = [int(x) for x in input().split()]
print(negative_vs_positive(numbers))
