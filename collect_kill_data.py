import re

def collect_kill_data(match):
    kill_pattern = re.compile(r'Kill: \d+ \d+ \d+: (.*) killed (.*) by (.*)')
    kills = []
    for line in match:
        match = kill_pattern.search(line)
        if match:
            killer, killed, method = match.groups()
            kills.append({
                'killer': killer,
                'killed': killed,
                'method': method
            })
    return kills
