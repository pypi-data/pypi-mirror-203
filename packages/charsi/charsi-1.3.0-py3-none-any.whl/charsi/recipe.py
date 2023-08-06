from typing import List, IO
from .instruction import parse, Instruction, InstructionInvoker
from .strings import GameStringTable, GameStringLanguage
from .utils import filter_irrelevant


class Recipe:
    _instructions: List[Instruction]

    @property
    def instructions(self):
        return self._instructions

    def load(self, fp: IO):
        self._instructions = [parse(line) for line in filter_irrelevant(fp.readlines())]

        return self

    def build(self, stbl: GameStringTable, invoker: InstructionInvoker = InstructionInvoker.default):
        for inst in self._instructions:
            langs = GameStringLanguage.get_values() if inst.lang is None else [inst.lang]

            for s in stbl.findall(inst.query):
                s.update({lang: invoker.invoke(inst, s[lang]) for lang in langs})
