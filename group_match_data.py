import re

def group_match_data(lines):
    matches = {}
    current_match = None
    kill_pattern = re.compile(r'Kill: \d+ \d+ \d+: (.*) killed (.*) by (.*)')
    for line in lines:
        if "InitGame" in line:
            if current_match:
                matches[f"game_{len(matches) + 1}"] = current_match
            current_match = {
                "total_kills": 0,
                "players": set(),
                "kills": {},
                "kills_by_means": {}
            }
        elif "Kill:" in line:
            current_match["total_kills"] += 1
            parts = line.split()
            killer_id = parts[3]
            killed_id = parts[4]
            means_of_death = parts[5].strip()

            if killer_id == '1022':  # <world> ID
                killed_name = parts[7]
                current_match["kills"].setdefault(killed_name, 0)
                current_match["kills"][killed_name] -= 1
            else:
                killer_name = parts[7]
                killed_name = parts[9]
                current_match["players"].add(killer_name)
                current_match["players"].add(killed_name)
                current_match["kills"].setdefault(killer_name, 0)
                current_match["kills"][killer_name] += 1

            current_match["kills_by_means"].setdefault(means_of_death, 0)
            current_match["kills_by_means"][means_of_death] += 1

    if current_match:
        matches[f"game_{len(matches) + 1}"] = current_match

    return matches
