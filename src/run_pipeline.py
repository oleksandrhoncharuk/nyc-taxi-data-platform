from download_raw_data import main as download_raw_data
from load_raw_data import main as load_raw_data

def main():
    print("=== STEP 1: DOWNLOAD RAW DATA ===")
    download_raw_data()

    print("\n=== STEP 2: LOAD DATA INTO POSTGRESQL ===")
    load_raw_data()

    print("\n=== PIPELINE COMPLETED ===")


if __name__ == "__main__":
    main()