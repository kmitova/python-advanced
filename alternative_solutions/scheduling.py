jobs = [int(x) for x in input().split(', ')]
index = int(input())
needed = jobs[index]
cycles = 0

while True:
    cycles += min(jobs)
    if min(jobs) == needed and jobs.count(needed) == 1:
        break
    jobs.remove(min(jobs))

print(cycles)
