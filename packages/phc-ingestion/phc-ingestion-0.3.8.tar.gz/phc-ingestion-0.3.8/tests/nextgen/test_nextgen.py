import tempfile
from threading import local
from unittest import mock
from pathlib import Path
import os

from ingestion.nextgen import process

BASE_PATH = os.path.abspath(os.path.dirname(__file__))


class MockLog:
    def info(self, _: str):
        pass


mock_log = MockLog()

files = {
    "somaticVcfFile": f"{BASE_PATH}/resources/Fankhauser_PA33390-BM2_output-tnscope.vcf.gz",
    "germlineVcfFile": f"{BASE_PATH}/resources/Fankhauser_PA33390-S2_output-dnascope.vcf.gz",
    "pdfFile": f"{BASE_PATH}/resources/RPT28095.pdf",
    "somaticBamFile": f"{BASE_PATH}/resources/Fankhauser_PA33390-BM2_recal.bam",
    "germlineBamFile": f"{BASE_PATH}/resources/Fankhauser_PA33390-S2_recal.bam.bai",
    "xmlFile": f"{BASE_PATH}/resources/RPT28095.xml",
}


def test_process():
    local_output_dir = f"{tempfile.TemporaryDirectory().name}/PA33391"
    os.makedirs(local_output_dir, exist_ok=True)
    response = process(
        account_id="account-id",
        vendor_files=files,
        local_output_dir=local_output_dir,
        source_file_id="archive_file_id",
        prefix="PA33391",
    )

    assert response == {
        "cnv_path_name": f"{local_output_dir}/PA33391.copynumber.csv",
        "manifest_path_name": f"{local_output_dir}/PA33391.ga4gh.genomics.yml",
        "structural_path_name": f"{local_output_dir}/PA33391.structural.csv",
        "somatic_vcf_meta_data": {
            "vcf_path_name": f"{local_output_dir}/PA33391.modified.somatic.vcf.gz",
            "vcf_line_count": 256,
        },
        "germline_vcf_meta_data": {
            "vcf_path_name": f"{local_output_dir}/PA33391.modified.germline.vcf.gz",
            "vcf_line_count": 256,
        },
    }
    resulting_files = [path.name for path in Path(f"{local_output_dir}").iterdir()]
    print(resulting_files)
    assert "PA33391.copynumber.csv" in resulting_files
    assert "PA33391.ga4gh.genomics.yml" in resulting_files
    assert "PA33391.structural.csv" in resulting_files
    assert "PA33391.modified.somatic.vcf.gz" in resulting_files
    assert "PA33391.modified.germline.vcf.gz" in resulting_files
