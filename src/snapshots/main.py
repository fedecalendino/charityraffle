from pathlib import Path

from raffles import raffle_06

raffle = raffle_06

path = Path(f"../../files/{raffle.number}. {raffle.id}")
path.mkdir(parents=True, exist_ok=True)

with open(path / "snapshot.txt", "w+") as file:
    for address, asset_name in raffle.full_snapshot:
        line = f"{address}: {asset_name}"

        print(line)
        file.write(f"{line}\n")


with open(path / "golden.txt", "w+") as file:
    for address, asset_name in raffle.golden_snapshot:
        line = f"{address}: {asset_name}"

        print(line)
        file.write(f"{line}\n")
