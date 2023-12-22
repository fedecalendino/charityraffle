import toolkit
from goldens import GOLDENS, ALL_GOLDENS

ID = "kumwe_hub"
NAME = "Raffle for Kumwe Hub - Save the Children"

POLICY_ID = "eed8d82ba538429e6b11af6db02196c07b7505c1a8334ed16ed9a6e0"


toolkit.take_snapshot(
    ID,
    NAME,
    POLICY_ID,
    goldens=GOLDENS,
    all_goldens=ALL_GOLDENS,
    verbose=True,
    stake_key=True,
)
