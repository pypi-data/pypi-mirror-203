from enum import Enum


class AnalysisTypes(str, Enum):
    WGS: str = "wgs"
    WES: str = "wes"
    TGS: str = "tgs"
    RNA: str = "rna"
    OTHER: str = "other"
