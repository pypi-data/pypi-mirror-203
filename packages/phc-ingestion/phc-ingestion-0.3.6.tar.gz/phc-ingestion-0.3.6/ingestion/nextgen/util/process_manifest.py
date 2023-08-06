from ruamel.yaml import YAML
from logging import Logger


def process_manifest(xml_in_file: str, root_path: str, prefix: str, files: dict, log: Logger):
    yaml = YAML()
    manifest = {}
    manifest["testType"] = "NextGen"
    manifest_path = f"{root_path}/{prefix}/{prefix}.ga4gh.genomics.yml"
    with open(manifest_path, "w") as file:
        yaml.dump(manifest, file)

    return manifest_path
