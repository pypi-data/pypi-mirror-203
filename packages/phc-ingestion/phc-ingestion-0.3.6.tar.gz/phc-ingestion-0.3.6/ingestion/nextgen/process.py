from enum import Enum
from lifeomic_logging import scoped_logger

from ingestion.nextgen.util.process_cnv import process_cnv
from ingestion.nextgen.util.process_manifest import process_manifest
from ingestion.nextgen.util.process_structural import process_structural
from ingestion.nextgen.util.process_vcf import process_vcf


class NextGen_Files(str, Enum):
    SOMATIC_VCF = "somaticVcfFile"
    GERMLINE_VCF = "germlineVcfFile"
    PDF = "pdfFile"
    SOMATIC_BAM = "somaticBamFile"
    GERMLINE_BAM = "germlineBamFile"
    XML = "xmlFile"


def process(
    account_id: str,
    vendor_files: dict,
    local_output_dir: str,
    source_file_id: str,
    prefix: str,
    phc_output_dir: str = ".lifeomic/nextgen",
) -> None:
    with scoped_logger(__name__) as log:
        process_cnv(
            xml_in_file=vendor_files[NextGen_Files.XML],
            root_path=local_output_dir,
            prefix=prefix,
            files=vendor_files,
            log=log,
        )
        process_manifest(
            xml_in_file=vendor_files[NextGen_Files.XML],
            root_path=local_output_dir,
            prefix=prefix,
            log=log,
        )
        process_structural(
            xml_in_file=vendor_files[NextGen_Files.XML],
            root_path=local_output_dir,
            prefix=prefix,
            log=log,
        )
        process_vcf(
            xml_in_file=vendor_files[NextGen_Files.SOMATIC_VCF],
            root_path=local_output_dir,
            prefix=prefix,
            sequence_type="somatic",
            log=log,
        )
        process_vcf(
            xml_in_file=vendor_files[NextGen_Files.GERMLINE_BAM],
            root_path=local_output_dir,
            prefix=prefix,
            sequence_type="germline",
            log=log,
        )
