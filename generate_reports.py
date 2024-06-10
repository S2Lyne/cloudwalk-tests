def generate_match_report(match_data):
    """
    Função para gerar o relatório de cada partida.

    Args:
    match_data (dict): Um dicionário contendo os dados agrupados de cada partida.

    Returns:
    str: O relatório da partida formatado como string.
    """
    match_report = ""

    for match_id, data in match_data.items():
        match_report += f"Partida: {match_id}\n"
        match_report += f"Total de kills: {data['total_kills']}\n"
        match_report += "Jogadores: " + ", ".join(data['players']) + "\n"
        match_report += "Kills por jogador:\n"
        for player, kills in data['kills'].items():
            match_report += f"  {player}: {kills}\n"
        match_report += "\n"

    return match_report

def generate_player_ranking(match_data):
    """
    Função para gerar o ranking dos jogadores.

    Args:
    match_data (dict): Um dicionário contendo os dados agrupados de cada partida.

    Returns:
    str: O ranking dos jogadores formatado como string.
    """
    player_scores = {}

    for data in match_data.values():
        for player, kills in data['kills'].items():
            if player not in player_scores:
                player_scores[player] = 0
            player_scores[player] += kills

    sorted_players = sorted(player_scores.items(), key=lambda item: item[1], reverse=True)
    player_ranking = "Ranking de Jogadores:\n"
    for player, score in sorted_players:
        player_ranking += f"  {player}: {score}\n"

    return player_ranking

def generate_death_cause_report(match_data):
    """
    Função para gerar o relatório de causas de morte.

    Args:
    match_data (dict): Um dicionário contendo os dados agrupados de cada partida.

    Returns:
    str: O relatório de causas de morte formatado como string.
    """
    death_cause_report = "Relatório de Causas de Morte:\n"

    for match_id, data in match_data.items():
        death_cause_report += f"Partida: {match_id}\n"
        for cause, count in data['kills_by_means'].items():
            death_cause_report += f"  {cause}: {count}\n"
        death_cause_report += "\n"

    return death_cause_report
