from collections import defaultdict
from pathlib import Path
from prettytable import PrettyTable
from typing import List, Dict
from base import Raffle
from raffles import raffle_01, raffle_02, raffle_03, raffle_04, raffle_05, raffle_06
import csv


def triples(bag: list[int]) -> int:
    sets = 0

    while True:
        bag = sorted(bag)  # sorts from low to high

        value = bag[2]

        if value == 0:
            break

        bag[2] -= value
        bag[3] -= value
        bag[4] -= value

        sets += value

    return sets


def make_snapshot(raffles: List[Raffle]) -> Dict[str, List[int]]:
    snappy = defaultdict(lambda: [0] * len(raffles))

    ticket_count = 0

    for index, raffle in enumerate(raffles):
        for address, assets in raffle.snapshot:
            snappy[address][index] += 1
            ticket_count += 1

    return snappy


def calculate_sets(raffles: List[Raffle]):
    numbers = list(map(lambda raffle: raffle.number, raffles))
    headers = ["addr"] + numbers + ["sets"]

    csv_file = open(path / "sets.csv", "w+")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)

    table = PrettyTable(headers)

    ticket_count = 0
    set_count = 0

    for address, tickets in make_snapshot(raffles).items():
        *previous, last = tickets
        sets = min(triples(previous), last)

        set_count += sets
        ticket_count += sum(tickets)

        row = [address] + tickets + [sets]

        csv_writer.writerow(row)
        table.add_row(row)

    # print
    print("Tickets:", ticket_count)
    print("Sets:", set_count)
    print()
    print(str(table))

    # write txt
    with open(path / "sets.txt", "w+") as file:
        file.write(f"Tickets: {ticket_count}\n")
        file.write(f"Sets: {set_count}\n")
        file.write("\n")
        file.write(str(table))

    # write csv
    csv_file.close()


if __name__ == "__main__":
    path = Path(f"../../files/sets")
    path.mkdir(parents=True, exist_ok=True)

    assert min(triples([5, 4, 2, 1, 6]), 6) == 6
    assert min(triples([10, 10, 10, 10, 10]), 15) == 10
    assert min(triples([7, 8, 2, 1, 0]), 20) == 3
    assert min(triples([7, 11, 5, 10, 20]), 20) == 16
    assert min(triples([1, 1, 1, 1, 1]), 3) == 1

    calculate_sets([raffle_01, raffle_02, raffle_03, raffle_04, raffle_05, raffle_06])
