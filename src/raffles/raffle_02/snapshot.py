import toolkit

from goldens import GOLDENS, ALL_GOLDENS

ID = "ripple_africa"
NAME = "OG Community Raffle for Ripple Africa"

POLICY_ID = "3568e07d31ab3c217ea594bfff9744a00a91225fa53244514ffeefb5"


toolkit.take_snapshot(
    ID,
    NAME,
    POLICY_ID,
    goldens=GOLDENS,
    all_goldens=ALL_GOLDENS,
    verbose=True,
)
