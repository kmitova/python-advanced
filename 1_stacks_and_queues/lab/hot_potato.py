from collections import deque

players = deque(input().split())
n = int(input())

while len(players) > 1:
    players.rotate(-n)
    print(f"Removed {players.pop()}")

print(f"Last is {players.pop()}")


