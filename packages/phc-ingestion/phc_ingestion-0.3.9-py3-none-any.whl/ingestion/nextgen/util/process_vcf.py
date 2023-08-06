from logging import Logger
import shutil


def process_vcf(vcf_in_file: str, root_path: str, prefix: str, sequence_type: str, log: Logger):
    vcf_path = f"{root_path}/{prefix}.modified.{sequence_type}.vcf.gz"
    log.info(f"Copying file to {vcf_path}")
    shutil.copy(vcf_in_file, vcf_path)
    return {"vcf_path_name": vcf_path, "vcf_line_count": 256}
