from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())
shot_bullets = 0
used_bullets = 0
while locks and bullets:
    if locks[0] >= bullets[-1]:
        locks.popleft()
        bullets.pop()
        print("Bang!")
    else:
        print("Ping!")
        bullets.pop()
    shot_bullets += 1
    if shot_bullets == barrel_size and bullets:
        print("Reloading!")
        shot_bullets = 0
    used_bullets += 1

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    pay = intelligence_value - (used_bullets * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${pay}")

