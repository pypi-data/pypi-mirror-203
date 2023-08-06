import dataclasses
import logging
import typing
import irisml.core


PLACEHOLDER = '<|placeholder|>'
logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Make a prompt with a list of strings.

    For example, if the template is "What is <placeholder>?" and the strings are ["a", "b", "c"], the prompt will be "What is a, b, c?".

    Config:
        template (str): The template to use for the prompt. Must contain "<placeholder>".
        delimiter (str): The delimiter to use between the strings. Defaults to ", ".
    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Inputs:
        strings: typing.List[str]

    @dataclasses.dataclass
    class Config:
        template: str
        delimiter: str = ', '

    @dataclasses.dataclass
    class Outputs:
        prompt: str

    def execute(self, inputs):
        if PLACEHOLDER not in self.config.template:
            raise ValueError(f'"{PLACEHOLDER}" must be in template')

        prompt = self.config.template.replace(PLACEHOLDER, self.config.delimiter.join(inputs.strings))
        logger.info(f"Created a prompt: {prompt}")
        return self.Outputs(prompt=prompt)

    def dry_run(self, inputs):
        return self.execute(inputs)
