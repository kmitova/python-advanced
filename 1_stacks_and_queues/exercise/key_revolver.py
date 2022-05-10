from collections import deque

bullets_shot = 0
bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(y) for y in input().split()])
intelligence_value = int(input())
earned = 0
total_shot = 0

while locks or bullets:
    if len(bullets) == 0 or len(locks) == 0:
        break
    lock = locks[0]
    bullet = bullets[-1]
    if lock < bullet:
        bullets.pop()
        print("Ping!")
    else:
        locks.popleft()
        bullets.pop()
        print("Bang!")
    bullets_shot += 1
    total_shot += 1
    if bullets_shot == barrel_size and bullets:
        print("Reloading!")
        bullets_shot = 0

earned = intelligence_value - total_shot * bullet_price
if len(bullets) > 0 and not locks:
    print(f"{len(bullets)} bullets left. Earned ${earned}")
elif len(locks) > 0 and not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")
elif not bullets and not locks:
    print(f"0 bullets left. Earned ${earned}")
