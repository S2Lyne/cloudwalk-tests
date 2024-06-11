import re

MEANS_OF_DEATH = {
    "MOD_UNKNOWN": 0,
    "MOD_SHOTGUN": 1,
    "MOD_GAUNTLET": 2,
    "MOD_MACHINEGUN": 3,
    "MOD_GRENADE": 4,
    "MOD_GRENADE_SPLASH": 5,
    "MOD_ROCKET": 6,
    "MOD_ROCKET_SPLASH": 7,
    "MOD_PLASMA": 8,
    "MOD_PLASMA_SPLASH": 9,
    "MOD_RAILGUN": 10,
    "MOD_LIGHTNING": 11,
    "MOD_BFG": 12,
    "MOD_BFG_SPLASH": 13,
    "MOD_WATER": 14,
    "MOD_SLIME": 15,
    "MOD_LAVA": 16,
    "MOD_CRUSH": 17,
    "MOD_TELEFRAG": 18,
    "MOD_FALLING": 19,
    "MOD_SUICIDE": 20,
    "MOD_TARGET_LASER": 21,
    "MOD_TRIGGER_HURT": 22,
    "MOD_NAIL": 23,
    "MOD_CHAINGUN": 24,
    "MOD_PROXIMITY_MINE": 25,
    "MOD_KAMIKAZE": 26,
    "MOD_JUICED": 27,
    "MOD_GRAPPLE": 28
}

def group_match_data(log_data):
    matches = {}
    current_match = None
    players = set()

    for line in log_data:
        match_start = re.match(r'^ *(\d+):(\d+) InitGame:', line)
        if match_start:
            current_match = f"game_{len(matches) + 1}"
            matches[current_match] = {
                "total_kills": 0,
                "players": [],
                "kills": {},
                "kills_by_means": {death_type: 0 for death_type in MEANS_OF_DEATH.keys()}
            }
            players.clear()

        if current_match:
            player_match = re.match(r'^ *(\d+):(\d+) ClientUserinfoChanged: \d+ n\\\\([^\\\\]+)\\\\t\\\\', line)
            if player_match:
                player = player_match.group(3)
                players.add(player)
                if player not in matches[current_match]["players"]:
                    matches[current_match]["players"].append(player)
                    matches[current_match]["kills"][player] = 0

            kill_match = re.match(r'^ *(\d+):(\d+) Kill: \d+ \d+ \d+: ([^:]+) killed ([^:]+) by (.*)$', line)
            if kill_match:
                matches[current_match]["total_kills"] += 1
                killer = kill_match.group(3)
                victim = kill_match.group(4)
                death_cause = kill_match.group(5)

                if killer != "<world>":
                    if killer not in matches[current_match]["kills"]:
                        matches[current_match]["kills"][killer] = 0
                    matches[current_match]["kills"][killer] += 1
                else:
                    if victim in matches[current_match]["kills"]:
                        matches[current_match]["kills"][victim] -= 1

                if death_cause in MEANS_OF_DEATH.keys():
                    matches[current_match]["kills_by_means"][death_cause] += 1

    return matches
