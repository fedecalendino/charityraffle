from pathlib import Path

from raffles import raffle_01, raffle_02, raffle_03, raffle_04, raffle_05, raffle_06

RAFFLES = [
    raffle_06,
    raffle_05,
    raffle_04,
    raffle_03,
    raffle_02,
    raffle_01,
]

MAIN, *GOLDENS = RAFFLES


path = Path(f"../files/{MAIN.id}")
path.mkdir(parents=True, exist_ok=True)

with open(f"{path}/snapshot.txt", "w+") as file:
    for address, asset_name in MAIN.snapshot:
        line = f"{address}: {asset_name}"

        print(line)
        file.write(f"{line}\n")

    for raffle in GOLDENS:
        for address, asset_name in raffle.golden_snapshot:
            line = f"{address}: {asset_name}"

            print(line)
            file.write(f"{line}\n")

with open(f"{path}/golden.txt", "w+") as file:
    for address, asset_name in MAIN.golden_snapshot:
        line = f"{address}: {asset_name}"

        print(line)
        file.write(f"{line}\n")
