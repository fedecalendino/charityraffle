import toolkit
from goldens import GOLDENS, ALL_GOLDENS

ID = "zeltschule"
NAME = "Charity raffle for Zeltschule e.V."

POLICY_ID = "acccccd01ef1519ae920d278fa34fa795a4a7728a276e941fcbbd83c"


toolkit.take_snapshot(
    ID,
    NAME,
    POLICY_ID,
    goldens=GOLDENS,
    all_goldens=ALL_GOLDENS,
    verbose=True,
    stake_key=True,
)
