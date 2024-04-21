from typing import Iterable, List, Dict, Tuple

import maestro


class Raffle:
    def __init__(
        self,
        id: str,
        number: int,
        name: str,
        policy_id: str,
        goldens: Dict[str, str],
        previous: List["Raffle"],
    ):
        self.id: str = id
        self.number: int = number
        self.name: str = name
        self.policy_id: str = policy_id
        self.goldens: Dict[str, str] = goldens
        self.previous: List[Raffle] = previous

    @property
    def snapshot(self) -> Iterable[Tuple[str, List[str]]]:
        print(f"{self.id}: snapshotting tickets")
        yield from maestro.get_snapshot(self.policy_id, self.goldens)

    @property
    def golden_snapshot(self) -> Iterable[Tuple[str, List[str]]]:
        print(f"{self.id}: snapshotting golden tickets")
        yield from maestro.get_snapshot(self.policy_id, self.goldens, gold_only=True)

    @property
    def full_snapshot(self) -> Iterable[Tuple[str, List[str]]]:
        yield from self.snapshot

        for previous in self.previous:
            yield from previous.golden_snapshot
