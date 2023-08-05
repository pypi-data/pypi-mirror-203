from abc import ABC, abstractmethod
from fastcore.dispatch import *
from . import core
from typing import Self

class RunManager(): 
    def __new__(cls: type[Self]
        ) -> Self:
        
        
    
        return super().__new__()

    def __init__(self) -> None:
        super().__init__()

    @typedispatch
    def run(self, trainer: core.automl.trainer.Trainer): 
        ...

    @typedispatch
    def run(self, evaluator: core.automl.evaluator.Evaluator): 
        ...

    @typedispatch
    def run(self, inferer: core.automl.inferer.Inferer): 
        ...

