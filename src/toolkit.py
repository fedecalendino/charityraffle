import blockfrostio
import utils


def take_snapshot(
    id: str,
    name: str,
    policy_id: str,
    goldens: dict,
    all_goldens: dict = None,
    stake_key: bool = False,
    verbose: bool = False,
):
    print(f"SNAPSHOT:{name} ({id})")

    all_goldens = all_goldens or {}

    golden_lines = []

    with open(f"./files/snapshot.txt", "w+") as file:
        snapshot = blockfrostio.snapshot(
            policy_id,
            golden_asset_ids=all_goldens.keys(),
            verbose=False,
            skip_jpg=True,
            stake_key=stake_key,
        )

        for asset_id, address in snapshot:
            policy_id, asset_name = utils.split(asset_id)

            if asset_id in all_goldens:
                asset_name = all_goldens[asset_id]

            line = f"{address}: {asset_name}"

            if verbose:
                print(f"{line}")

            file.write(f"{line} \n")

            if asset_id in goldens:
                golden_lines.append(line)

    print()
    print("GOLDEN TICKET OWNERS")

    with open(f"./files/goldens.txt", "w+") as file:
        for line in golden_lines:
            print(f"  * {line}")
            file.write(f"{line} \n")


def make_golden_asset_ids(policy_id: str, amount: int, raffle_number: int):
    for i in range(amount):
        asset_name = f"{raffle_number:02}RaffleTicket{i:04}"
        enconded_asset_name = asset_name.encode("UTF-8").hex().lower()

        print(
            f'"{policy_id}{enconded_asset_name}": "{asset_name} (golden ticket raffle #{raffle_number})",'
        )
