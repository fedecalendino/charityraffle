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
    extra_asset_ids: List[str] = None,
    verbose: bool = False,
):
    print(f"SNAPSHOT:{name} ({id})")

    with open(f"./files/snapshot.txt", "w+") as file:
        snap = blockfrostio.snapshot(
            policy_id,
            extra_asset_ids=extra_asset_ids,
            verbose=verbose,
            skip_jpg=True,
        )

        for asset_id, address in snap:
            policy_id, asset_name = utils.split(asset_id)

            line = f"{address}: {asset_name}"

            file.write(f"{line} \n")

            if verbose:
                print(f"{line}")

            if "Gold" in asset_name and policy_id in asset_id:
                print(f"{address}: {asset_name} ({asset_id})")


def metadata_template(
    policy_id: str,
    name: str,
    variant: str,
    ipfs: str,
    number: int = None,
    bonus: str = None,
):
    if number is not None:
        name = f"{name} #{number:04}"

    id = name.title().replace(" ", "").replace("#", "").replace(":", "")

    metadata = {
        "721": {
            policy_id: {
                id: {
                    "author": "Book.io community",
                    "collection": "Charity raffle for Ripple Africa",
                    "charity": "Ripple Africa",
                    "description": [
                        "Ripple Africa is inspiring communities in Malawi, ",
                        "to achieve a sustainable future.",
                    ],
                    "image": f"ipfs://{ipfs}",
                    "name": name,
                    "type": "image/jpeg",
                    "url": "https://rippleafrica.org",
                    "variant": variant,
                }
            }
        }
    }

    if bonus:
        metadata["721"][policy_id][id]["bonus"] = bonus

    return id, name, metadata


def generate_metadata(
    policy_id: str,
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
            name="Raffle Entry Ticket",
            variant="normal",
            ipfs=normal_ipfs,
            number=i,
        )

        with open(output / f"{id}.json", "w+") as file:
            file.write(json.dumps(metadata, indent=4))

    for prize, data in goldens.items():
        bonus = ["One perpetual entry ticket"]
        bonus.extend(data.get("bonus", []))

        id, name, metadata = metadata_template(
            policy_id=policy_id,
            name=f"Golden Entry Ticket: {prize}",
            variant="golden",
            ipfs=data["ipfs"],
            bonus=bonus,
        )

        print(name)

        with open(output / f"{id}.json", "w+") as file:
            file.write(json.dumps(metadata, indent=4))

    if make_zip:
        os.system(f"zip {output} ./{output} -r")
