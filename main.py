# main.py
from read_log import read_log_file
from group_match_data import group_match_data
from generate_reports import (
    generate_match_report,
    generate_player_ranking,
    generate_death_cause_report
)

# Caminho para o arquivo de log
log_file_path = "quake_log.log"

# Ler o arquivo de log
log_data = read_log_file(log_file_path)

# Agrupar os dados da partida
match_data = group_match_data(log_data)

# Gerar relatórios
match_report = generate_match_report(match_data)
player_ranking = generate_player_ranking(match_data)
death_cause_report = generate_death_cause_report(match_data)

# Imprimir os relatórios
print("Relatório da Partida:")
print(match_report)

print("\nRanking dos Jogadores:")
print(player_ranking)

print("\nRelatório de Causas de Morte:")
print(death_cause_report)
