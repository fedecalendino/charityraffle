import goldens
import toolkit

ID = "syrian_earthquake"
NAME = "Charity raffle for earthquake victims in Syria"

POLICY_ID = "dcaae559714f022242d3302378374d8e117abff4c2ab6de2ed235c98"


toolkit.take_snapshot(
    ID,
    NAME,
    POLICY_ID,
    extra_asset_ids=goldens.GOLDENS.keys(),
    verbose=True,
)
