import sys

line = sys.stdin.readline().strip().split()
user_limit, service_limit, duration = [int(params) for params in line]
users = {}
requests = []
prev_time = 0
while True:
    request_descriptions = sys.stdin.readline().strip().split()
    if len(request_descriptions) == 1:
        break

    curr_time, user_id = [int(description) for description in request_descriptions]
    if curr_time - prev_time > duration:
        requests = [t for t in requests if curr_time - t <= duration]
        if requests:
            prev_time = requests[0]
    if user_id in users:
        users[user_id] = [t for t in users[user_id] if curr_time - t <= duration]

    if user_id in users and len(users[user_id]) >= user_limit:
        sys.stdout.write('429\n')
        sys.stdout.flush()
        continue
    if len(requests) >= service_limit:
        sys.stdout.write('503\n')
        sys.stdout.flush()
    else:
        users.setdefault(user_id, []).append(curr_time)
        requests.append(curr_time)
        sys.stdout.write('200\n')
        sys.stdout.flush()
