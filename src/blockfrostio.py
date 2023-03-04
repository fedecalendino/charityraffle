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
        params = {"page": page}

        response = requests.get(url, params=params, headers=HEADERS)
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
        return item["address"]


def snapshot(
    policy_id: str,
    extra_asset_ids: List[str] = None,
    skip_jpg: bool = True,
    verbose: bool = False,
) -> Iterable[Tuple[str, str]]:
    print(f"🔎 fetching assets for {policy_id}")

    asset_ids = []

    for asset_id in get_assets(policy_id):
        asset_ids.append(asset_id)

    asset_ids.extend(list(extra_asset_ids or []))

    for asset_id in asset_ids:
        policy_id, asset_name = utils.split(asset_id)

        if verbose:
            print(f"  * fetching addresses for '{asset_name}'")

        address = get_holder(asset_id)

        if not address:
            continue

        if address == JPGSTORE_ADDRESS and skip_jpg:
            if verbose:
                print(f"    > skipping asset listed in jpg.store")
            continue

        yield asset_id, address
