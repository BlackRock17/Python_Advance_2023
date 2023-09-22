def pos_or_neg(pos, neg):
    print(neg)
    print(pos)

    if abs(neg) > pos:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")

numbers = [int(x) for x in input().split()]

negatives = sum([x for x in numbers if x < 0])
positives = sum([x for x in numbers if x > 0])

pos_or_neg(positives, negatives)
