def split(asset_id: str) -> tuple:
    return asset_id[:56], bytes.fromhex(asset_id[56:]).decode()
