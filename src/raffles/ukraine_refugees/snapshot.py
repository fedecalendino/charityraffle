import toolkit
from goldens import GOLDENS

ID = "ukraine"
NAME = "OG Community Raffle for Ukraine Refugees and Displaced Persons"

POLICY_ID = "12c1f9c6754952e2c26b37af3c8facee41ed5b398c0223ff9f4848c4"


toolkit.take_snapshot(
    ID,
    NAME,
    POLICY_ID,
    goldens=GOLDENS,
    verbose=True,
)
