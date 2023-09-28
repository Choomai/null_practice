n, m = [int(elem) for elem in input().split()]
# input() # Useless N and M...
distances = [int(elem) for elem in input().split()]
consume_rates = [int(elem) for elem in input().split()]
sorted_dist = sorted(distances, reverse=True)
sorted_csm_rt = sorted(consume_rates)

def calc(dist_arr: list, csm_arr: list) -> list:
    result, indexes = 0,[]
    for index in range(len(dist_arr)): # or csm_arr
        tmp = dist_arr[index] * csm_arr[index]
        result += tmp
        indexes.append(str(consume_rates.index(csm_arr[index]) + 1))
    
    return [result, indexes]

if len(distances) == len(consume_rates):
    print(calc(sorted_dist, sorted_csm_rt))
    exit(0)

for _ in range(m - n): consume_rates.remove(sorted_csm_rt.pop())
final_result = calc(sorted_dist, sorted_csm_rt)
print(final_result[0])
print("\n".join(final_result[1]))