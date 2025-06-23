expected_files = ['Warframes.json', 'Primary.json', 'Secondary.json', 'Melee.json', 'Misc.json', 'Archwing.json', 'Arch-Gun.json', 'Arch-Melee.json', 'Pets.json', 'Sentinels.json', 'SentinelWeapons.json']
"""
Script to run the data processor
"""

import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from api_client.data_processor import WarframeDataProcessor
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure data_processor.py is saved in src/api_client/")
    sys.exit(1)

def main():
    print("Warframe Data Processor")
    print("=" * 40)
    
    # Check if raw data exists
    raw_data_dir = "data/raw"
    if not os.path.exists(raw_data_dir):
        print(f"✗ Raw data directory '{raw_data_dir}' not found.")
        print("Please run the WFCD client first to fetch raw data.")
        return
    
    # Check for some expected files
    expected_files = ['Primary.json', 'Secondary.json', 'Melee.json', 'Warframes.json']
    missing_files = []
    
    for filename in expected_files:
        if not os.path.exists(os.path.join(raw_data_dir, filename)):
            missing_files.append(filename)
    
    if missing_files:
        print(f"✗ Missing raw data files: {', '.join(missing_files)}")
        print("Please run the WFCD client first to fetch all data.")
        return
    
    print("✓ Raw data files found")
    print("\nStarting data processing...")
    
    # Create and run processor
    processor = WarframeDataProcessor()
    
    try:
        # Process warframes only for now
        processor.process_warframes()
        
        print("\n" + "=" * 40)
        print("Data processing completed successfully!")
        print("Check the 'data/processed/' directory for cleaned data files.")
        
    except Exception as e:
        print(f"\n✗ Error during processing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()