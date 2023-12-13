import os
import sys
from datasets import load_dataset

def download_and_store(dataset_name, output_folder):
    dataset = load_dataset(dataset_name)
    output_path = os.path.join(output_folder, dataset_name)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for split in dataset.keys():
        dataset[split].to_csv(os.path.join(output_path, f"{split}.csv"))

    print(f"Dataset '{dataset_name}' downloaded and stored in '{output_path}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python download_dataset.py [dataset_name] [output_folder]")
        sys.exit(1)

    dataset_name = sys.argv[1]
    output_folder = sys.argv[2]

    download_and_store(dataset_name, output_folder)