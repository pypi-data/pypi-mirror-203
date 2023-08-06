from typing import List, IO
from .instruction import parse, Instruction, InstructionInvoker
from .strings import GameStringTable, GameStringLanguage


class Recipe:
    _instructions: List[Instruction]

    @property
    def instructions(self):
        return self._instructions

    def load(self, fp: IO):
        self._instructions = [parse(line) for line in fp.readlines()]

        return self

    def build(self, stbl: GameStringTable, invoker: InstructionInvoker = InstructionInvoker.default):
        for inst in self._instructions:
            s = stbl.find(inst.query)
            s.update({lang: invoker.invoke(inst, s[lang]) for lang in GameStringLanguage.get_values()})
