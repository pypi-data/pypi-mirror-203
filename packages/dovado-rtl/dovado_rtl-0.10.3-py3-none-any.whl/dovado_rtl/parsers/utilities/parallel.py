from abc import ABC, abstractmethod
from typing import Optional

class Parallel(ABC):
    def __init__(self) -> None:
        self._jobs: Optional[int] = None

    @property
    @abstractmethod
    def jobs(self) -> int:
        if self._jobs is None:
            raise ValueError("Trying to retrieve None jobs")

        return self._jobs

    @jobs.setter
    def jobs(self, num_jobs: int):
        if self._jobs is not None:
            raise ValueError("Number of jobs is " + str(self._jobs) + " trying to set twice")

        self._jobs = num_jobs


