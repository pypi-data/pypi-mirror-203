from enum import Enum


class NextGen_Files(str, Enum):
    SOMATIC_VCF = "somaticVcfFile"
    GERMLINE_VCF = "germlineVcfFile"
    PDF = "pdfFile"
    SOMATIC_BAM = "somaticBamFile"
    GERMLINE_BAM = "germlineBamFile"
    XML = "xmlFile"
