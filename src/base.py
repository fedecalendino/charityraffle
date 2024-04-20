from typing import Iterable, List, Dict, Tuple

import maestro


class Raffle:
    def __init__(self, id: str, name: str, policy_id: str, goldens: Dict[str, str]):
        self.id: str = id
        self.name: str = name
        self.policy_id: str = policy_id
        self.goldens: Dict[str, str] = goldens

    @property
    def snapshot(self) -> Iterable[Tuple[str, List[str]]]:
        yield from maestro.get_snapshot(self.policy_id, self.goldens)

    @property
    def golden_snapshot(self) -> Iterable[Tuple[str, List[str]]]:
        yield from maestro.get_snapshot(self.policy_id, self.goldens, gold_only=True)
