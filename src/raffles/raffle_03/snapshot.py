import toolkit
from goldens import GOLDENS, ALL_GOLDENS

ID = "syrian_earthquake"
NAME = "Charity raffle for earthquake victims in Syria"

POLICY_ID = "dcaae559714f022242d3302378374d8e117abff4c2ab6de2ed235c98"


toolkit.take_snapshot(
    ID,
    NAME,
    POLICY_ID,
    goldens=GOLDENS,
    all_goldens=ALL_GOLDENS,
    verbose=True,
    stake_key=True,
)
