# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]

max_index1 = -1
for i in range(0,n):
	if ((max_index1 == -1) | (a[i] > a[max_index1])): max_index1 = i

max_index2 = -1
for j in range(0,n):
	if ( (j!=max_index1) & ((max_index2 == -1) | (a[j] > a[max_index2])) ): max_index2 = j

result = a[max_index1] * a[max_index2]

print(result)
