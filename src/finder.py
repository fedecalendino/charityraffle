from raffles import raffle_07

import maestro

assets = []

for asset in maestro.get_snapshot(raffle_07.policy_id, {}):
    assets.append(asset)


for address, asset_name in sorted(assets, key=lambda x: x[1]):
    print(asset_name)
