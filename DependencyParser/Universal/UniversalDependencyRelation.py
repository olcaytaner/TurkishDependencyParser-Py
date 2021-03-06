from DependencyParser.DependencyRelation import DependencyRelation
from DependencyParser.Universal.UniversalDependencyPosType import UniversalDependencyPosType
from DependencyParser.Universal.UniversalDependencyType import UniversalDependencyType


class UniversalDependencyRelation(DependencyRelation):

    __universalDependencyType: UniversalDependencyType

    universalDependencyTypes = ["ACL", "ADVCL",
                                "ADVMOD", "AMOD",
                                "APPOS",
                                "AUX", "AUXPASS",
                                "CASE", "CC", "CCOMP",
                                "CLF", "COMPOUND",
                                "CONJ", "COP", "CSUBJ",
                                "DEP", "DET",
                                "DISCOURSE", "DISLOCATED",
                                "EXPL",
                                "FIXED", "FLAT",
                                "FOREIGN",
                                "GOESWITH",
                                "IOBJ",
                                "LIST",
                                "MARK",
                                "NMOD", "NSUBJ",
                                "NUMMOD",
                                "OBJ", "OBL", "ORPHAN",
                                "PARATAXIS", "PUNCT",
                                "REPARANDUM", "ROOT",
                                "VOCATIVE",
                                "XCOMP"]

    universalDependencyTags = [UniversalDependencyType.ACL, UniversalDependencyType.ADVCL,
                               UniversalDependencyType.ADVMOD, UniversalDependencyType.AMOD,
                               UniversalDependencyType.APPOS,
                               UniversalDependencyType.AUX, UniversalDependencyType.AUXPASS,
                               UniversalDependencyType.CASE, UniversalDependencyType.CC, UniversalDependencyType.CCOMP,
                               UniversalDependencyType.CLF, UniversalDependencyType.COMPOUND,
                               UniversalDependencyType.CONJ, UniversalDependencyType.COP, UniversalDependencyType.CSUBJ,
                               UniversalDependencyType.DEP, UniversalDependencyType.DET,
                               UniversalDependencyType.DISCOURSE, UniversalDependencyType.DISLOCATED,
                               UniversalDependencyType.EXPL,
                               UniversalDependencyType.FIXED, UniversalDependencyType.FLAT,
                               UniversalDependencyType.FOREIGN,
                               UniversalDependencyType.GOESWITH,
                               UniversalDependencyType.IOBJ,
                               UniversalDependencyType.LIST,
                               UniversalDependencyType.MARK,
                               UniversalDependencyType.NMOD, UniversalDependencyType.NSUBJ,
                               UniversalDependencyType.NUMMOD,
                               UniversalDependencyType.OBJ, UniversalDependencyType.OBL, UniversalDependencyType.ORPHAN,
                               UniversalDependencyType.PARATAXIS, UniversalDependencyType.PUNCT,
                               UniversalDependencyType.REPARANDUM, UniversalDependencyType.ROOT,
                               UniversalDependencyType.VOCATIVE,
                               UniversalDependencyType.XCOMP]

    universalDependencyPosTypes = ["ADJ", "ADV", "INTJ", "NOUN", "PROPN", "VERB", "ADP", "AUX", "CCONJ",
                                   "DET", "NUM", "PART", "PRON", "SCONJ", "PUNCT", "SYM", "X"]

    universalDependencyPosTags = [UniversalDependencyPosType.ADJ, UniversalDependencyPosType.ADV,
                                  UniversalDependencyPosType.INTJ, UniversalDependencyPosType.NOUN,
                                  UniversalDependencyPosType.PROPN,
                                  UniversalDependencyPosType.VERB, UniversalDependencyPosType.ADP,
                                  UniversalDependencyPosType.AUX, UniversalDependencyPosType.CCONJ,
                                  UniversalDependencyPosType.DET, UniversalDependencyPosType.NUM,
                                  UniversalDependencyPosType.PART,
                                  UniversalDependencyPosType.PRON, UniversalDependencyPosType.SCONJ,
                                  UniversalDependencyPosType.PUNCT, UniversalDependencyPosType.SYM,
                                  UniversalDependencyPosType.X]

    @staticmethod
    def getDependencyTag(tag: str) -> UniversalDependencyType:
        """
        The getDependencyTag method takes an dependency tag as string and returns the UniversalDependencyType
        form of it.

        PARAMETERS
        ----------
        tag : str
            Type of the dependency tag in string form

        RETURNS
        -------
        UniversalDependencyType
            Type of the dependency in UniversalDependencyType form
        """
        for j in range(len(UniversalDependencyRelation.universalDependencyTags)):
            if tag == UniversalDependencyRelation.universalDependencyTypes[j]:
                return UniversalDependencyRelation.universalDependencyTags[j]
        return None

    @staticmethod
    def getDependencyPosType(tag: str) -> UniversalDependencyPosType:
        for j in range(len(UniversalDependencyRelation.universalDependencyPosTypes)):
            if tag == UniversalDependencyRelation.universalDependencyPosTypes[j]:
                return UniversalDependencyRelation.universalDependencyPosTags[j]
        return None

    def __init__(self, toWord: int, dependencyType: str = None):
        """
        Overriden Universal Dependency Relation constructor. Gets toWord as input and calls it super class's constructor

        PARAMETERS
        ----------
        toWord : int
            Index of the word in the sentence that dependency relation is related
        """
        super().__init__(toWord)
        if dependencyType is not None:
            self.__universalDependencyType = UniversalDependencyRelation.getDependencyTag(dependencyType)

    def __str__(self) -> str:
        return self.__universalDependencyType.name
