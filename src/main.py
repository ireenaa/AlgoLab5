def dfs(level, position, company, memory):
    if level == len(company):
        return 0

    if (level, position) in memory:
        return memory[(level, position)]

    max_experience = 0
    for next_position in range(position, position + 2):
        if next_position < len(company[level]):
            experience = company[level][next_position] + dfs(level + 1, next_position, company, memory)
            max_experience = max(max_experience, experience)

    memory[(level, position)] = max_experience
    return max_experience


with open('career.in', 'r') as file:
    lines = file.readlines()
    L = int(lines[0])
    company = []
    for line in lines[1:]:
        company.append(list(map(int, line.split())))

memory = {}
max_total_experience = dfs(0, 0, company, memory)

with open('career.out', 'w') as file:
    file.write(str(max_total_experience))
