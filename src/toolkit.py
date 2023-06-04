import json
import os
from pathlib import Path
from typing import List

import blockfrostio
import utils


def take_snapshot(
    id: str,
    name: str,
    policy_id: str,
    goldens: dict,
    all_goldens: dict = None,
    verbose: bool = False,
):
    print(f"SNAPSHOT:{name} ({id})")

    all_goldens = all_goldens or {}

    golden_lines = []

    with open(f"./files/snapshot.txt", "w+") as file:
        snapshot = blockfrostio.snapshot(
            policy_id,
            golden_asset_ids=all_goldens.keys(),
            verbose=verbose,
            skip_jpg=True,
        )

        for asset_id, address in snapshot:
            policy_id, asset_name = utils.split(asset_id)

            line = f"{address}: {asset_name}"

            if verbose:
                print(f"{line}")

            file.write(f"{line} \n")

            if asset_id in goldens:
                golden_lines.append(line)

    print()
    print("GOLDEN TICKET OWNERS")

    for line in golden_lines:
        print(f"  * {line}")


def generate_metadata(
    metadata_template: callable,
    policy_id: str,
    collection_name: str,
    collection_author: str,
    collection_description: List[str],
    charity_name: str,
    charity_url: str,
    normal_ipfs: str,
    normal_supply: int,
    goldens: dict,
    make_zip: bool = False,
):
    os.system("rm -rf ./files/metadata")

    output = Path("./files/metadata")
    output.mkdir()

    for i in range(1, normal_supply + 1):
        id, name, metadata = metadata_template(
            policy_id=policy_id,
            collection_name=collection_name,
            collection_author=collection_author,
            collection_description=collection_description,
            charity_name=charity_name,
            charity_url=charity_url,
            name="Raffle Entry Ticket",
            variant="normal",
            ipfs=normal_ipfs,
            number=i,
        )

        print(f"Generated: {name}")

        with open(output / f"{id}.json", "w+") as file:
            file.write(json.dumps(metadata, indent=4))

    for prize, data in goldens.items():
        bonus = ["One perpetual entry ticket"]
        bonus.extend(data.get("bonus", []))

        id, name, metadata = metadata_template(
            policy_id=policy_id,
            collection_name=collection_name,
            collection_author=collection_author,
            collection_description=collection_description,
            charity_name=charity_name,
            charity_url=charity_url,
            name=f"Golden Entry Ticket: {prize}",
            variant="golden",
            ipfs=data["ipfs"],
            bonus=bonus,
        )

        print(f"Generated: {name}")

        with open(output / f"{id}.json", "w+") as file:
            file.write(json.dumps(metadata, indent=4))

    if make_zip:
        os.system(f"zip {output} ./{output} -r")
