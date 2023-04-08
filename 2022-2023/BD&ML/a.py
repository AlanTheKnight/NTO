def get_weights(inputs):
    print("GW", inputs)
    out_weights = []
    sum_inputs = sum(inputs)
    positive_weight = 2
    b = -(sum_inputs * positive_weight - 1)
    negative_weight = -(sum_inputs * positive_weight + 1)
    if b > 0:
        negative_weight -= b
    for inp in inputs:
        out_weights.append(positive_weight if inp == 1 else negative_weight)
    out_weights.append(b)
    return out_weights


K = int(input())
all_inputs = []
for i in range(2 ** K):
    num = list(map(int, str(bin(i)[2:]).rjust(K, '0')))[::-1]
    all_inputs.append((int(input()), num))

n = 2 ** K // 2
print(2)
print(n, 1)

for (expected_output1, inputs1), (expected_output2, inputs2) in zip(all_inputs[::2], all_inputs[1::2]):
    if expected_output1 == expected_output2 == 0:
        print('0 ' * K + '-0.5')
        continue
    weights1 = []
    weights2 = []

    if expected_output1 == 1:
        weights1 = get_weights(inputs1)
    if expected_output2 == 1:
        weights2 = get_weights(inputs2)
    if expected_output1 == expected_output2:
        new_inputs = [inputs1[i] for i in range(K) if inputs1[i] == inputs2[i]]
        new_weights = get_weights(new_inputs)
        result_weights = []
        for i in range(K):
            if inputs1[i] != inputs2[i]:
                result_weights.append(0)
                continue
            result_weights.append(new_weights.pop(0))
        result_weights.append(new_weights.pop(0))
        print(' '.join(map(str, result_weights)))
        continue
    if expected_output1 == 1:
        print(' '.join(map(str, weights1)))
    else:
        print(' '.join(map(str, weights2)))

print('1 ' * n + '-0.5')
