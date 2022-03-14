from dataclasses import dataclass
from typing import Callable, TypeVar
import numpy as np

Numeric = TypeVar('Numeric')

@dataclass
class Data:
    name: str
    exact_sol: Callable[[Numeric, Numeric], Numeric]
    