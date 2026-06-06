import os
import splitfolders

def preprocessing():

    dataset_path = os.path.abspath(
        "../dataset_raw/Rice_Image_Dataset"
    )

    output_path = os.path.abspath(
        "dataset_preprocessing"
    )

    print("="*50)
    print("AUTOMATED PREPROCESSING")
    print("="*50)

    print(f"Dataset Source : {dataset_path}")
    print(f"Output Folder  : {output_path}")

    splitfolders.ratio(
        dataset_path,
        output=output_path,
        seed=42,
        ratio=(0.7, 0.15, 0.15)
    )

    print("\nPreprocessing selesai.")

if __name__ == "__main__":
    preprocessing()