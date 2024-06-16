passenger = 0
num_passenger = []

for _ in range(10) :
    out, come = map(int, input().split())
    passenger += come - out
    num_passenger.append(passenger)

print(max(num_passenger))