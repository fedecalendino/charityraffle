import os
from typing import Iterable, List, Dict, Tuple

from fetchfox.blockchains.cardano import Cardano

import utils

MAESTRO_API_KEY = os.getenv("MAESTRO_API_KEY")
JPGSTORE_ADDRESS = "addr1zxgx3far7qygq0k6epa0zcvcvrevmn0ypsnfsue94nsn3tvpw288a4x0xf8pxgcntelxmyclq83s0ykeehchz2wtspks905plm"


cardano = Cardano(
    maestro_api_key=MAESTRO_API_KEY,
)


def get_snapshot(
    policy_id: str, goldens: Dict[str, str], gold_only: bool = False
) -> Iterable[Tuple[str, List[str]]]:
    for holding in cardano.get_collection_snapshot(policy_id):
        address = holding.address

        if address == JPGSTORE_ADDRESS:
            continue

        asset_id = holding.asset_id
        policy_id, asset_name = utils.split(asset_id)

        if not asset_name:
            continue

        if asset_id in goldens:
            asset_name = goldens[asset_id]
        elif gold_only:
            continue

        yield address, asset_name
