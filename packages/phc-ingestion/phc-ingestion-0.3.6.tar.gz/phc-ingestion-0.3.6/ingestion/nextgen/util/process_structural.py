from logging import Logger


def process_structural(xml_in_file: str, root_path: str, prefix: str, log: Logger):
    structural_variant_path_name = f"{root_path}/{prefix}/{prefix}.structural.csv"
    with open(structural_variant_path_name, "w") as f:
        f.write(
            "sample_id,gene1,gene2,effect,chromosome1,start_position1,end_position1,chromosome2,start_position2,end_position2,interpretation,sequence_type,in_frame,attributes\n"
        )

    return structural_variant_path_name
