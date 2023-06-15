import os
import time
from typing import List, Iterable, Tuple

import requests

import utils
from constants import JPGSTORE_ADDRESS

HEADERS = {
    "project_id": os.getenv("BLOCKFROST_PROJECT_ID"),
}


def get_assets(policy_id: str) -> Iterable[dict]:
    time.sleep(0.1)

    page = 0

    while True:
        page += 1

        url = f"https://cardano-mainnet.blockfrost.io/api/v0/assets/policy/{policy_id}"
        response = requests.get(url, params={"page": page}, headers=HEADERS)

        json = response.json()

        if not json:
            break

        for item in json:
            if item["asset"] == policy_id:
                continue

            yield item["asset"]


def get_holder(asset_id: str) -> str:
    time.sleep(0.1)

    url = f"https://cardano-mainnet.blockfrost.io/api/v0/assets/{asset_id}/addresses"

    response = requests.get(url, headers=HEADERS)
    json = response.json()

    for item in json:
        try:
            return item["address"]
        except:
            return None

def snapshot(
    policy_id: str,
    golden_asset_ids: List[str] = None,
    skip_jpg: bool = True,
    verbose: bool = False,
) -> Iterable[Tuple[str, str]]:
    print(f"fetching assets for {policy_id}")

    assets = []

    for asset_id in get_assets(policy_id):
        assets.append(asset_id)

        if verbose:
            _, asset_name = utils.split(asset_id)
            print(f"  * found: {asset_id}: {asset_name}")

    print()
    print(f"assets for {policy_id}: {len(assets)} assets")

    assets.extend(list(golden_asset_ids or []))
    print(f"assets for {policy_id} + goldens: {len(assets)} assets")

    print()
    print(f"fetching owners for {len(assets)} assets")

    for asset_id in assets:
        owner = get_holder(asset_id)

        policy_id, asset_name = utils.split(asset_id)

        if not owner:
            if verbose:
                print(f"  *  {asset_name} was not minted")
            continue

        if owner == JPGSTORE_ADDRESS:
            if verbose:
                print(f"  * found owner: {owner} (jpg)")

            if skip_jpg:
                if verbose:
                    print(f"    > skipping asset listed in jpg.store")
                continue
        else:
            if verbose:
                print(f"  * found owner: {owner}")

        yield asset_id, owner
