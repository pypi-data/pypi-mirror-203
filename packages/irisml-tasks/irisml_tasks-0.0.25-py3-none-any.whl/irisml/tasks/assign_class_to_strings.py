import dataclasses
import logging
import random
import typing
import torch
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Assigns a class to a string based on the class name being present in the string.

    If no class name is found, a random class is assigned.

    Note that this class assumes that the class names don't overlap. For example, if
    the class names are ['a', 'ab'] and the string is 'ab', the first class will be
    assigned.

    Config:
        assign_random_class (bool): If True, a random class will be assigned if no class name is found. If False, the class will be set to -1.
    """
    VERSION = '0.1.1'

    @dataclasses.dataclass
    class Inputs:
        strings: typing.List[str]
        class_names: typing.List[str]

    @dataclasses.dataclass
    class Config:
        assign_random_class: bool = True

    @dataclasses.dataclass
    class Outputs:
        classes: torch.Tensor  # Shape: (N, )

    def execute(self, inputs):
        results = [self._find_class(s, inputs.class_names) for s in inputs.strings]
        num_unknowns = results.count(None)
        if num_unknowns > 0:
            if self.config.assign_random_class:
                results = [c if c is not None else random.randrange(len(inputs.class_names)) for c in results]
                logger.info(f"Assigned {num_unknowns}/{len(inputs.strings)} strings to a random class")
            else:
                results = [c if c is not None else -1 for c in results]
                logger.info(f"Assigned {num_unknowns}/{len(inputs.strings)} strings to class -1")
        return self.Outputs(torch.tensor(results))

    def dry_run(self, inputs):
        return self.execute(inputs)

    @staticmethod
    def _find_class(s, class_names):
        for i, c in enumerate(class_names):
            if c in s:
                return i
        return None
