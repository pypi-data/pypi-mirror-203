from enum import Enum


class AnalysisTypes(str, Enum):
    WGS: str = "wgs"
    WES: str = "wes"
    TGS: str = "tgs"
    RNA: str = "rna"
    WTS: str = "wts"
    OTHER: str = "other"
