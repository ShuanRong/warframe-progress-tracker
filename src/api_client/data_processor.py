"""
Simple Warframe Data Processor - Starting with just Warframes
Build this step by step
"""

import json
import os
from typing import Dict, List, Any

class WarframeDataProcessor:
    """Simple processor starting with just Warframes"""
    
    def __init__(self, raw_data_dir: str = "data/raw", processed_data_dir: str = "data/processed"):
        self.raw_data_dir = raw_data_dir
        self.processed_data_dir = processed_data_dir
        self.raw_data = {}
        
        # Create processed directory if it doesn't exist
        os.makedirs(processed_data_dir, exist_ok=True)
    
    def load_raw_data(self) -> None:
        """Load the raw Warframes.json and Primary.json files"""
        # Load Warframes
        warframes_file = os.path.join(self.raw_data_dir, 'Warframes.json')
        if os.path.exists(warframes_file):
            with open(warframes_file, 'r', encoding='utf-8') as f:
                self.raw_data['warframes'] = json.load(f)
                print(f"✓ Loaded {len(self.raw_data['warframes'])} items from Warframes.json")
        else:
            print("✗ Warframes.json not found!")
            self.raw_data['warframes'] = []
        
        # Load Primary weapons
        primary_file = os.path.join(self.raw_data_dir, 'Primary.json')
        if os.path.exists(primary_file):
            with open(primary_file, 'r', encoding='utf-8') as f:
                self.raw_data['primary'] = json.load(f)
                print(f"✓ Loaded {len(self.raw_data['primary'])} items from Primary.json")
        # Load Secondary weapons
        secondary_file = os.path.join(self.raw_data_dir, 'Secondary.json')
        if os.path.exists(secondary_file):
            with open(secondary_file, 'r', encoding='utf-8') as f:
                self.raw_data['secondary'] = json.load(f)
                print(f"✓ Loaded {len(self.raw_data['secondary'])} items from Secondary.json")
        # Load Melee weapons
        melee_file = os.path.join(self.raw_data_dir, 'Melee.json')
        if os.path.exists(melee_file):
            with open(melee_file, 'r', encoding='utf-8') as f:
                self.raw_data['melee'] = json.load(f)
                print(f"✓ Loaded {len(self.raw_data['melee'])} items from Melee.json")
        # Load Misc items
        misc_file = os.path.join(self.raw_data_dir, 'Misc.json')
        if os.path.exists(misc_file):
            with open(misc_file, 'r', encoding='utf-8') as f:
                self.raw_data['misc'] = json.load(f)
                print(f"✓ Loaded {len(self.raw_data['misc'])} items from Misc.json")
        # Load Archwings
        archwing_file = os.path.join(self.raw_data_dir, 'Archwing.json')
        if os.path.exists(archwing_file):
            with open(archwing_file, 'r', encoding='utf-8') as f:
                self.raw_data['archwing'] = json.load(f)
                print(f"✓ Loaded {len(self.raw_data['archwing'])} items from Archwing.json")
        # Load Arch-Guns
        archgun_file = os.path.join(self.raw_data_dir, 'Arch-Gun.json')
        if os.path.exists(archgun_file):
            with open(archgun_file, 'r', encoding='utf-8') as f:
                self.raw_data['arch-gun'] = json.load(f)
                print(f"✓ Loaded {len(self.raw_data['arch-gun'])} items from Arch-Gun.json")
        else:
            print("✗ Arch-Gun.json not found!")
            self.raw_data['arch-gun'] = []
            
        # Load Arch-Melee
        archmelee_file = os.path.join(self.raw_data_dir, 'Arch-Melee.json')
        if os.path.exists(archmelee_file):
            with open(archmelee_file, 'r', encoding='utf-8') as f:
                self.raw_data['arch-melee'] = json.load(f)
                print(f"✓ Loaded {len(self.raw_data['arch-melee'])} items from Arch-Melee.json")
        else:
            print("✗ Arch-Melee.json not found!")
            self.raw_data['arch-melee'] = []
            
        # Load Pets
        pets_file = os.path.join(self.raw_data_dir, 'Pets.json')
        if os.path.exists(pets_file):
            with open(pets_file, 'r', encoding='utf-8') as f:
                self.raw_data['pets'] = json.load(f)
                print(f"✓ Loaded {len(self.raw_data['pets'])} items from Pets.json")
        else:
            print("✗ Pets.json not found!")
            self.raw_data['pets'] = []
        
        # Load Sentinels
        sentinels_file = os.path.join(self.raw_data_dir, 'Sentinels.json')
        if os.path.exists(sentinels_file):
            with open(sentinels_file, 'r', encoding='utf-8') as f:
                self.raw_data['sentinels'] = json.load(f)
                print(f"✓ Loaded {len(self.raw_data['sentinels'])} items from Sentinels.json")
        else:
            print("✗ Sentinels.json not found!")
            self.raw_data['sentinels'] = []
            
        # Load Sentinel Weapons
        sentinel_weapons_file = os.path.join(self.raw_data_dir, 'SentinelWeapons.json')
        if os.path.exists(sentinel_weapons_file):
            with open(sentinel_weapons_file, 'r', encoding='utf-8') as f:
                self.raw_data['sentinelweapons'] = json.load(f)
                print(f"✓ Loaded {len(self.raw_data['sentinelweapons'])} items from SentinelWeapons.json")
        else:
            print("✗ SentinelWeapons.json not found!")
            self.raw_data['sentinelweapons'] = []
            
        # Load Incarnon weapons
        incarnon_file = os.path.join(self.raw_data_dir, 'Incarnon.json')
        if os.path.exists(incarnon_file):
            with open(incarnon_file, 'r', encoding='utf-8') as f:
                self.raw_data['incarnon'] = json.load(f)
                print(f"✓ Loaded {len(self.raw_data['incarnon'])} items from Incarnon.json")
        else:
            print("✗ Incarnon.json not found!")
            self.raw_data['incarnon'] = []
            
        # Load Amps
        amps_file = os.path.join(self.raw_data_dir, 'Amps.json')
        if os.path.exists(amps_file):
            with open(amps_file, 'r', encoding='utf-8') as f:
                self.raw_data['amps'] = json.load(f)
                print(f"✓ Loaded {len(self.raw_data['amps'])} items from Amps.json")
        else:
            print("✗ Amps.json not found!")
            self.raw_data['amps'] = []

    def explore_warframes(self) -> None:
        """Let's see what's actually in the Warframes data"""
        if not self.raw_data.get('warframes'):
            print("No warframes data loaded")
            return
        
        print("\n=== Exploring Warframes Data ===")
        
        # Look at the first few items
        print("First 3 items:")
        for i, item in enumerate(self.raw_data['warframes'][:3]):
            print(f"\n{i+1}. {item.get('name', 'Unknown')}")
            print(f"   Type: {item.get('type', 'Unknown')}")
            print(f"   Unique Name: {item.get('uniqueName', 'Unknown')}")
            print(f"   Description: {item.get('description', 'No description')[:50]}...")
        
        # See all the different types
        print("\n=== All Item Types in Warframes.json ===")
        types = {}
        for item in self.raw_data['warframes']:
            item_type = item.get('type', 'No Type')
            types[item_type] = types.get(item_type, 0) + 1
        
        for item_type, count in sorted(types.items()):
            print(f"  '{item_type}': {count} items")
    
    def extract_warframes_only(self) -> List[Dict[str, Any]]:
        """Extract only actual Warframes (not Necramechs, etc.)"""
        warframes = []
        
        if not self.raw_data.get('warframes'):
            return warframes
        
        for item in self.raw_data['warframes']:
            # Check unique_name to filter out Necramechs
            unique_name = item.get('uniqueName', '')
            
            # Skip if it's a Necramech (contains the Entrati Mech path)
            if '/Lotus/Powersuits/EntratiMech/' in unique_name:
                continue  # Skip this item, it's a Necramech
            
            # Now check if it's a regular Warframe
            item_type = item.get('type', '')
            if item_type == 'Warframe':
                warframes.append(item)
        
        print(f"✓ Found {len(warframes)} Warframes (filtered out Necramechs)")
        return warframes
    
    def extract_necramechs(self) -> List[Dict[str, Any]]:
        """Extract Necramechs based on unique_name"""
        necramechs = []
        
        if not self.raw_data.get('warframes'):
            return necramechs
        
        for item in self.raw_data['warframes']:
            # Check unique_name for Necramech path
            unique_name = item.get('uniqueName', '')
            
            # If it contains the Entrati Mech path, it's a Necramech
            if '/Lotus/Powersuits/EntratiMech/' in unique_name:
                necramechs.append(item)
        
        print(f"✓ Found {len(necramechs)} Necramechs")
        return necramechs
    
    def explore_primary_weapons(self) -> None:
        """Let's see what's actually in the Primary weapons data"""
        if not self.raw_data.get('primary'):
            print("No primary weapons data loaded")
            return
        
        print("\n=== Exploring Primary Weapons Data ===")
        
        # Look at the first few items
        print("First 3 primary weapons:")
        for i, item in enumerate(self.raw_data['primary'][:3]):
            print(f"\n{i+1}. {item.get('name', 'Unknown')}")
            print(f"   Type: {item.get('type', 'Unknown')}")
            print(f"   Unique Name: {item.get('uniqueName', 'Unknown')}")
            print(f"   Description: {item.get('description', 'No description')[:50]}...")
        
        # See all the different types
        print("\n=== All Item Types in Primary.json ===")
        types = {}
        for item in self.raw_data['primary']:
            item_type = item.get('type', 'No Type')
            types[item_type] = types.get(item_type, 0) + 1
        
        for item_type, count in sorted(types.items()):
            print(f"  '{item_type}': {count} items")
    
    def extract_primary_weapons(self) -> List[Dict[str, Any]]:
        """Extract primary weapons (excluding special types like Kitguns for now)"""
        primary_weapons = []
        
        if not self.raw_data.get('primary'):
            return primary_weapons
    
    def explore_secondary_weapons(self) -> None:
        """Let's see what's actually in the Secondary weapons data"""
        if not self.raw_data.get('secondary'):
            print("No secondary weapons data loaded")
            return
        
        print("\n=== Exploring Secondary Weapons Data ===")
        
        # Look at the first few items
        print("First 3 secondary weapons:")
        for i, item in enumerate(self.raw_data['secondary'][:3]):
            print(f"\n{i+1}. {item.get('name', 'Unknown')}")
            print(f"   Type: {item.get('type', 'Unknown')}")
            print(f"   Unique Name: {item.get('uniqueName', 'Unknown')}")
            print(f"   Description: {item.get('description', 'No description')[:50]}...")
        
        # See all the different types
        print("\n=== All Item Types in Secondary.json ===")
        types = {}
        for item in self.raw_data['secondary']:
            item_type = item.get('type', 'No Type')
            types[item_type] = types.get(item_type, 0) + 1
        
        for item_type, count in sorted(types.items()):
            print(f"  '{item_type}': {count} items")
    
    def extract_secondary_weapons(self) -> List[Dict[str, Any]]:
        """Extract secondary weapons (same pattern as primary)"""
        secondary_weapons = []
        
        if not self.raw_data.get('secondary'):
            return secondary_weapons
    
    def explore_melee_weapons(self) -> None:
        """Let's see what's actually in the Melee weapons data"""
        if not self.raw_data.get('melee'):
            print("No melee weapons data loaded")
            return
        
        print("\n=== Exploring Melee Weapons Data ===")
        
        # Look at the first few items
        print("First 3 melee weapons:")
        for i, item in enumerate(self.raw_data['melee'][:3]):
            print(f"\n{i+1}. {item.get('name', 'Unknown')}")
            print(f"   Type: {item.get('type', 'Unknown')}")
            print(f"   Unique Name: {item.get('uniqueName', 'Unknown')}")
            print(f"   Description: {item.get('description', 'No description')[:50]}...")
        
        # See all the different types
        print("\n=== All Item Types in Melee.json ===")
        types = {}
        for item in self.raw_data['melee']:
            item_type = item.get('type', 'No Type')
            types[item_type] = types.get(item_type, 0) + 1
        
        for item_type, count in sorted(types.items()):
            print(f"  '{item_type}': {count} items")
    
    def extract_melee_weapons(self) -> List[Dict[str, Any]]:
        """Extract melee weapons (excluding Zaw components)"""
        melee_weapons = []
        
        if not self.raw_data.get('melee'):
            return melee_weapons
        
        # Debug: Let's see what we're actually getting
        print("\n=== DEBUG: First 5 melee items and their types ===")
        for i, item in enumerate(self.raw_data['melee'][:5]):
            print(f"{i+1}. {item.get('name', 'Unknown')} - Type: '{item.get('type', 'No Type')}'")
        
        for item in self.raw_data['melee']:
            item_type = item.get('type', '')
            
            # Skip Zaw components - they go in their own file
            if item_type == 'Zaw Component':
                continue  # Skip this item, it's a Zaw component
            
            # Take all other items that have a type
            if item_type:
                melee_weapons.append(item)
        
        print(f"✓ Found {len(melee_weapons)} melee weapons (filtered out Zaw components)")
        
        # Show type breakdown
        type_counts = {}
        for item in melee_weapons:
            item_type = item.get('type', 'No Type')
            type_counts[item_type] = type_counts.get(item_type, 0) + 1
        
        print("Type breakdown:")
        for item_type, count in sorted(type_counts.items()):
            print(f"  '{item_type}': {count} items")
        
        return melee_weapons
    
    def extract_zaws(self) -> List[Dict[str, Any]]:
        """Extract Zaw components based on type"""
        zaws = []
        
        if not self.raw_data.get('melee'):
            return zaws
        
        for item in self.raw_data['melee']:
            # Check type for Zaw components
            item_type = item.get('type', '')
            unique_name = item.get('uniqueName', '')
            # If it's a Zaw Component, it goes here
            if item_type == 'Zaw Component':
                
                if 'pvp' in unique_name.lower():
                    continue
                
                if any(zaw_part in unique_name for zaw_part in ['/Tip/', '/Tips/']):
                    zaws.append(item)
        
        print(f"✓ Found {len(zaws)} Zaw components")
        return zaws
    
    def extract_kitguns(self) -> List[Dict[str, Any]]:
        """Extract Kitgun barrels from misc.json based on unique_name and masterable status"""
        kitguns = []
        
        print(f"\n=== DEBUG: Looking for kitgun barrels in Misc ===")
        
        # Check misc.json for kitgun barrels
        if self.raw_data.get('misc'):
            found_items = []
            for item in self.raw_data['misc']:
                unique_name = item.get('uniqueName', '')
                masterable = item.get('masterable', False)
                
                # Look for "/Barrel/" in the unique_name AND must be masterable
                if ('/Barrel/' in unique_name or '/Barrels/' in unique_name) and '/OperatorAmplifiers/' not in unique_name:
                    # Filter out PvP variants
                    if 'pvp' not in unique_name.lower():
                        found_items.append(item)
                        kitguns.append(item)
            
            print(f"Found {len(found_items)} kitgun barrels in MISC:")
            for item in found_items:
                print(f"  • {item.get('name', 'Unknown')} - Type: '{item.get('type', 'Unknown')}'")
                print(f"    Unique: {item.get('uniqueName', 'Unknown')}")
                print(f"    Masterable: {item.get('masterable', False)}")
        
        # Also check primary and secondary just in case
        for category in ['primary', 'secondary']:
            if self.raw_data.get(category):
                found_items = []
                for item in self.raw_data[category]:
                    unique_name = item.get('uniqueName', '')
                    masterable = item.get('masterable', False)
                    
                    # Look for "/Barrel/" in the unique_name AND must be masterable
                    if ('/Barrel/' in unique_name or '/Barrels/' in unique_name) and '/OperatorAmplifiers/' not in unique_name:
                        # Filter out PvP variants
                        if 'pvp' not in unique_name.lower():
                            found_items.append(item)
                            kitguns.append(item)
                
                if found_items:
                    print(f"Found {len(found_items)} kitgun barrels in {category.upper()}:")
                    for item in found_items:
                        print(f"  • {item.get('name', 'Unknown')} - Type: '{item.get('type', 'Unknown')}'")
                        print(f"    Unique: {item.get('uniqueName', 'Unknown')}")
                        print(f"    Masterable: {item.get('masterable', False)}")
        
        print(f"✓ Found {len(kitguns)} total kitgun barrels")
        return kitguns
    
    def explore_archwings(self) -> None:
        """Let's see what's actually in the Archwing data"""
        if not self.raw_data.get('archwing'):
            print("No archwing data loaded")
            return
        
        print("\n=== Exploring Archwing Data ===")
        
        # Look at the first few items
        print("First 3 archwing items:")
        for i, item in enumerate(self.raw_data['archwing'][:3]):
            print(f"\n{i+1}. {item.get('name', 'Unknown')}")
            print(f"   Type: {item.get('type', 'Unknown')}")
            print(f"   Unique Name: {item.get('uniqueName', 'Unknown')}")
            print(f"   Description: {item.get('description', 'No description')[:50]}...")
        
        # See all the different types
        print("\n=== All Item Types in Archwing.json ===")
        types = {}
        for item in self.raw_data['archwing']:
            item_type = item.get('type', 'No Type')
            types[item_type] = types.get(item_type, 0) + 1
        
        for item_type, count in sorted(types.items()):
            print(f"  '{item_type}': {count} items")
    
    def extract_archwings(self) -> List[Dict[str, Any]]:
        """Extract archwings"""
        archwings = []
        
        if not self.raw_data.get('archwing'):
            return archwings
    
    def explore_arch_guns(self) -> None:
        """Let's see what's actually in the Arch-Gun data"""
        if not self.raw_data.get('arch-gun'):
            print("No arch-gun data loaded")
            return
        
        print("\n=== Exploring Arch-Gun Data ===")
        
        # Look at the first few items
        print("First 3 arch-gun items:")
        for i, item in enumerate(self.raw_data['arch-gun'][:3]):
            print(f"\n{i+1}. {item.get('name', 'Unknown')}")
            print(f"   Type: {item.get('type', 'Unknown')}")
            print(f"   Unique Name: {item.get('uniqueName', 'Unknown')}")
            print(f"   Description: {item.get('description', 'No description')[:50]}...")
        
        # See all the different types
        print("\n=== All Item Types in Arch-Gun.json ===")
        types = {}
        for item in self.raw_data['arch-gun']:
            item_type = item.get('type', 'No Type')
            types[item_type] = types.get(item_type, 0) + 1
        
        for item_type, count in sorted(types.items()):
            print(f"  '{item_type}': {count} items")
    
    def extract_arch_guns(self) -> List[Dict[str, Any]]:
        """Extract arch-guns"""
        arch_guns = []
        
        if not self.raw_data.get('arch-gun'):
            return arch_guns
        
        # Debug: Let's see what we're actually getting
        print("\n=== DEBUG: First 5 arch-gun items and their types ===")
        for i, item in enumerate(self.raw_data['arch-gun'][:5]):
            print(f"{i+1}. {item.get('name', 'Unknown')} - Type: '{item.get('type', 'No Type')}'")
        
        for item in self.raw_data['arch-gun']:
            item_type = item.get('type', '')
            unique_name = item.get('uniqueName', '')
            
            # Filter out PvP variants
            if 'pvp' in unique_name.lower():
                continue
            
            # Take all items that have a type
            if item_type:
                arch_guns.append(item)
        
        print(f"✓ Found {len(arch_guns)} arch-guns (filtered PvP)")
        
        # Show type breakdown
        type_counts = {}
        for item in arch_guns:
            item_type = item.get('type', 'No Type')
            type_counts[item_type] = type_counts.get(item_type, 0) + 1
        
        print("Type breakdown:")
        for item_type, count in sorted(type_counts.items()):
            print(f"  '{item_type}': {count} items")
        
        return arch_guns
    
    def explore_arch_melees(self) -> None:
        """Let's see what's actually in the Arch-Melee data"""
        if not self.raw_data.get('arch-melee'):
            print("No arch-melee data loaded")
            return

        print("\n=== Exploring Arch-Melee Data ===")

        # Look at the first few items
        print("First 3 arch-melee items:")
        for i, item in enumerate(self.raw_data['arch-melee'][:3]):
            print(f"\n{i+1}. {item.get('name', 'Unknown')}")
            print(f"   Type: {item.get('type', 'Unknown')}")
            print(f"   Unique Name: {item.get('uniqueName', 'Unknown')}")
            print(f"   Description: {item.get('description', 'No description')[:50]}...")
        
        # See all the different types
        print("\n=== All Item Types in Arch-Gun.json ===")
        types = {}
        for item in self.raw_data['arch-gun']:
            item_type = item.get('type', 'No Type')
            types[item_type] = types.get(item_type, 0) + 1
        
        for item_type, count in sorted(types.items()):
            print(f"  '{item_type}': {count} items")

    def extract_arch_melees(self) -> List[Dict[str, Any]]:
        """Extract arch-melee"""
        arch_melees = []

        if not self.raw_data.get('arch-melee'):
            return arch_melees

        # Debug: Let's see what we're actually getting
        print("\n=== DEBUG: First 5 arch-melee items and their types ===")
        for i, item in enumerate(self.raw_data['arch-melee'][:5]):
            print(f"{i+1}. {item.get('name', 'Unknown')} - Type: '{item.get('type', 'No Type')}'")

        for item in self.raw_data['arch-melee']:
            item_type = item.get('type', '')
            unique_name = item.get('uniqueName', '')
            
            # Filter out PvP variants
            if 'pvp' in unique_name.lower():
                continue
            
            # Take all items that have a type
            if item_type:
                arch_melees.append(item)

        print(f"✓ Found {len(arch_melees)} arch-melees (filtered PvP)")

        # Show type breakdown
        type_counts = {}
        for item in arch_melees:
            item_type = item.get('type', 'No Type')
            type_counts[item_type] = type_counts.get(item_type, 0) + 1
        
        print("Type breakdown:")
        for item_type, count in sorted(type_counts.items()):
            print(f"  '{item_type}': {count} items")

        return arch_melees

    def explore_companions(self) -> None:
        """Let's see what's actually in the companion data (pets + sentinels)"""
        print("\n=== Exploring Companion Data ===")
        
        # Explore pets
        if self.raw_data.get('pets'):
            print(f"\nPETS ({len(self.raw_data['pets'])} items):")
            print("First 3 pets:")
            for i, item in enumerate(self.raw_data['pets'][:3]):
                print(f"  {i+1}. {item.get('name', 'Unknown')} - Type: '{item.get('type', 'Unknown')}'")
            
            # See all pet types
            types = {}
            for item in self.raw_data['pets']:
                item_type = item.get('type', 'No Type')
                types[item_type] = types.get(item_type, 0) + 1
            
            print("Pet types:")
            for item_type, count in sorted(types.items()):
                print(f"  '{item_type}': {count} items")
        else:
            print("No pets data loaded")
        
        # Explore sentinels
        if self.raw_data.get('sentinels'):
            print(f"\nSENTINELS ({len(self.raw_data['sentinels'])} items):")
            print("First 3 sentinels:")
            for i, item in enumerate(self.raw_data['sentinels'][:3]):
                print(f"  {i+1}. {item.get('name', 'Unknown')} - Type: '{item.get('type', 'Unknown')}'")
            
            # See all sentinel types
            types = {}
            for item in self.raw_data['sentinels']:
                item_type = item.get('type', 'No Type')
                types[item_type] = types.get(item_type, 0) + 1
            
            print("Sentinel types:")
            for item_type, count in sorted(types.items()):
                print(f"  '{item_type}': {count} items")
        else:
            print("No sentinels data loaded")

    def extract_companions(self) -> List[Dict[str, Any]]:
        """Extract all companions (pets + sentinels)"""
        companions = []
        
        print(f"\n=== DEBUG: Extracting companions ===")
        
        # Extract pets
        if self.raw_data.get('pets'):
            pets_added = 0
            for item in self.raw_data['pets']:
                unique_name = item.get('uniqueName', '')
                item_type = item.get('type', '')
                
                # Filter out parts
                if item_type == 'Pets':
                    # Filter out PvP variants
                    if 'pvp' in unique_name.lower():
                        continue
                    
                    companions.append(item)
                    pets_added += 1
            
            print(f"Added {pets_added} pets to companions")
        
        # Extract sentinels
        if self.raw_data.get('sentinels'):
            sentinels_added = 0
            for item in self.raw_data['sentinels']:
                unique_name = item.get('uniqueName', '')
                item_type = item.get('type', '')
                
                # Filter out PvP variants
                if 'pvp' in unique_name.lower():
                    continue
                
                # Take all items that have a type
                if item_type:
                    companions.append(item)
                    sentinels_added += 1
            
            print(f"Added {sentinels_added} sentinels to companions")
        
        print(f"✓ Found {len(companions)} total companions (filtered PvP)")
        
        # Show type breakdown
        type_counts = {}
        for item in companions:
            item_type = item.get('type', 'No Type')
            type_counts[item_type] = type_counts.get(item_type, 0) + 1
        
        print("Combined companion type breakdown:")
        for item_type, count in sorted(type_counts.items()):
            print(f"  '{item_type}': {count} items")
        
        return companions

    def explore_sentinel_weapons(self) -> None:
        """Extract all sentinel weapons"""
        print(f"\n=== DEBUG: Extracting Sentinel Weapons ===")
        if self.raw_data.get('sentinelweapons'):
            print(f"Sentinel Weapons ({len(self.raw_data['sentinelweapons'])} items):")
            for i, item in enumerate(self.raw_data['sentinelweapons'][:3]):
                print(f"  {i+1}. {item.get('name', 'Unknown')} - Type: '{item.get('type', 'Unknown')}'")
        else:
            print("No sentinel weapons data loaded")

    def extract_sentinel_weapons(self) -> List[Dict[str, Any]]:
        """Extract all sentinel weapons"""
        print(f"\n=== DEBUG: Extracting Sentinel Weapons ===")
        return self.raw_data.get('sentinelweapons', [])
    
    def explore_incarnon_weapons(self) -> None:
        """Let's see what's actually in the Misc data for Equipment Adapters"""
        if not self.raw_data.get('misc'):
            print("No misc data loaded")
            return
        
        print("\n=== Exploring Misc Data for Equipment Adapters ===")
        
        # Look for equipment adapters specifically
        adapters = []
        for item in self.raw_data['misc']:
            name = item.get('name', '').lower()
            item_type = item.get('type', '').lower()
            
            if item_type == 'equipment adapter' and 'incarnon' in name:
                adapters.append(item)
        
        print(f"Found {len(adapters)} items with 'adapter' in name/type/unique_name:")
        for item in adapters[:5]:  # Show first 5
            print(f"  • {item.get('name', 'Unknown')} - Type: '{item.get('type', 'Unknown')}'")
            print(f"    Unique: {item.get('uniqueName', 'Unknown')}")
        
        # See all the different types in misc
        print("\n=== All Item Types in Misc.json ===")
        types = {}
        for item in self.raw_data['misc']:
            item_type = item.get('type', 'No Type')
            types[item_type] = types.get(item_type, 0) + 1
        
        for item_type, count in sorted(types.items()):
            print(f"  '{item_type}': {count} items")
        
        
        # Look at the first few items
        print("First 3 Incarnon weapons:")
        for i, item in enumerate(self.raw_data['incarnon'][:3]):
            print(f"\n{i+1}. {item.get('name', 'Unknown')}")
            print(f"   Type: {item.get('type', 'Unknown')}")
            print(f"   Unique Name: {item.get('uniqueName', 'Unknown')}")
            print(f"   Description: {item.get('description', 'No description')[:50]}...")
        
        # See all the different types
        print("\n=== All Item Types in Incarnon.json ===")
        types = {}
        for item in self.raw_data['incarnon']:
            item_type = item.get('type', 'No Type')
            types[item_type] = types.get(item_type, 0) + 1
        
        for item_type, count in sorted(types.items()):
            print(f"  '{item_type}': {count} items")
            
    def extract_incarnon_weapons(self) -> List[Dict[str, Any]]:
        """Extract Equipment Adapters from misc.json"""
        incarnon_adapters = []
        
        if not self.raw_data.get('misc'):
            return incarnon_adapters
        
        print("\n=== DEBUG: Looking for Equipment Adapters in Misc ===")
        
        for item in self.raw_data['misc']:
            name = item.get('name', '').lower()
            item_type = item.get('type', '').lower()
            
            # Look for Equipment Adapters
            if item_type == 'equipment adapter' and 'incarnon' in name:
                incarnon_adapters.append(item)
        
        print(f"✓ Found {len(incarnon_adapters)} Equipment Adapters")
        
        # Show what we found
        for item in incarnon_adapters:
            print(f"  • {item.get('name', 'Unknown')} - Type: '{item.get('type', 'Unknown')}'")
            print(f"    Unique: {item.get('uniqueName', 'Unknown')}")
        
        return incarnon_adapters
    
    def explore_amps(self) -> None:
        """Explore the loaded Amp data"""
        print("=== Exploring Amps Data ===")

        if not self.raw_data.get('misc'):
            print("✗ No Amp data found!")
            return

        # Look for equipment adapters specifically
        amps = []
        for item in self.raw_data['misc']:
            name = item.get('name', '').lower()
            item_type = item.get('type', '').lower()
            
            if item_type == 'amp' and 'prism' in name:
                amps.append(item)

        print(f"Found {len(amps)} items with 'amp' in name/type:")
        for item in amps[:5]:  # Show first 5
            print(f"  • {item.get('name', 'Unknown')} - Type: '{item.get('type', 'Unknown')}'")
            print(f"    Unique: {item.get('uniqueName', 'Unknown')}")
    
    def extract_amps(self) -> List[Dict[str, Any]]:
        """Extract Amp data"""
        amps = []
        
        if not self.raw_data.get('misc'):
            return amps
        
        print("\n=== DEBUG: Extracting Amps ===")
        
        for item in self.raw_data['misc']:
            name = item.get('name', '').lower()
            item_type = item.get('type', '').lower()
                       
            # Take all items that have a type
            if item_type == 'amp' and 'prism' in name:
                amps.append(item)
        
        print(f"✓ Found {len(amps)} Amps")
        
        return amps

    def clean_weapon_data(self, weapon: Dict[str, Any]) -> Dict[str, Any]:
        """Clean and simplify weapon data"""
        return {
            'name': weapon.get('name', 'Unknown'),
            'unique_name': weapon.get('uniqueName', ''),
            'type': weapon.get('type', ''),
            'description': weapon.get('description', ''),
            'mastery_rank': weapon.get('masteryReq', 0),
            'tradable': weapon.get('tradable', False),
            'vaulted': weapon.get('vaulted', False),
            # Weapon-specific stats
            'total_damage': weapon.get('totalDamage', 0),
            'fire_rate': weapon.get('fireRate', 0),
            'accuracy': weapon.get('accuracy', 0),
            'critical_chance': weapon.get('criticalChance', 0),
            'status_chance': weapon.get('statusChance', 0)
        }
    
    def clean_warframe_data(self, warframe: Dict[str, Any]) -> Dict[str, Any]:
        """Clean and simplify warframe data"""
        return {
            'name': warframe.get('name', 'Unknown'),
            'unique_name': warframe.get('uniqueName', ''),
            'type': warframe.get('type', ''),
            'description': warframe.get('description', ''),
            'mastery_rank': warframe.get('masteryReq', 0),
            'tradable': warframe.get('tradable', False),
            'vaulted': warframe.get('vaulted', False)
        }
    
    def process_warframes(self) -> None:
        """Process warframes, necramechs, and primary weapons"""
        print("=== Processing Warframes and Primary Weapons ===")
        
        # Load data
        self.load_raw_data()
        
        # Explore what we have
        self.explore_warframes()
        self.explore_primary_weapons()
        self.explore_secondary_weapons()
        self.explore_melee_weapons()
        self.explore_archwings()
        self.explore_arch_guns()
        self.explore_arch_melees()
        self.explore_companions()
        self.explore_sentinel_weapons()
        self.explore_incarnon_weapons()
        self.explore_amps()
        
        # Extract everything
        print("\n=== Extracting Data ===")
        warframes = self.extract_warframes_only() or []
        print(f"Warframes extracted: {len(warframes)}")
        
        necramechs = self.extract_necramechs() or []
        print(f"Necramechs extracted: {len(necramechs)}")
        
        primary_weapons = self.extract_primary_weapons() or []
        print(f"Primary weapons extracted: {len(primary_weapons)}")
        
        secondary_weapons = self.extract_secondary_weapons() or []
        print(f"Secondary weapons extracted: {len(secondary_weapons)}")
        
        melee_weapons = self.extract_melee_weapons() or []
        print(f"Melee weapons extracted: {len(melee_weapons)}")
        
        zaws = self.extract_zaws() or []
        print(f"Zaws extracted: {len(zaws)}")
        
        kitguns = self.extract_kitguns() or []
        print(f"Kitguns extracted: {len(kitguns)}")
        
        archwings = self.extract_archwings() or []
        print(f"Archwings extracted: {len(archwings)}")
        
        arch_guns = self.extract_arch_guns() or []
        print(f"Arch-guns extracted: {len(arch_guns)}")

        arch_melees = self.extract_arch_melees() or []
        print(f"Arch-melees extracted: {len(arch_melees)}")
        
        companions = self.extract_companions() or []
        print(f"Companions extracted: {len(companions)}")
        
        sentinel_weapons = self.extract_sentinel_weapons() or []
        print(f"Sentinel weapons extracted: {len(sentinel_weapons)}")
        
        incarnon_weapons = self.extract_incarnon_weapons() or []
        print(f"Incarnon weapons extracted: {len(incarnon_weapons)}")
        
        amps = self.extract_amps() or []
        print(f"Amps extracted: {len(amps)}")

        # Clean the data (with safety checks)
        print("\n=== Cleaning Data ===")
        cleaned_warframes = [self.clean_warframe_data(wf) for wf in warframes] if warframes else []
        cleaned_necramechs = [self.clean_warframe_data(nm) for nm in necramechs] if necramechs else []
        cleaned_primary_weapons = [self.clean_weapon_data(wp) for wp in primary_weapons] if primary_weapons else []
        cleaned_secondary_weapons = [self.clean_weapon_data(wp) for wp in secondary_weapons] if secondary_weapons else []
        cleaned_melee_weapons = [self.clean_weapon_data(wp) for wp in melee_weapons] if melee_weapons else []
        cleaned_zaws = [self.clean_weapon_data(zw) for zw in zaws] if zaws else []
        cleaned_kitguns = [self.clean_weapon_data(kg) for kg in kitguns] if kitguns else []
        cleaned_archwings = [self.clean_warframe_data(aw) for aw in archwings] if archwings else []
        cleaned_arch_guns = [self.clean_weapon_data(ag) for ag in arch_guns] if arch_guns else []
        cleaned_arch_melees = [self.clean_weapon_data(am) for am in arch_melees] if arch_melees else []
        cleaned_companions = [self.clean_warframe_data(c) for c in companions] if companions else []
        cleaned_sentinel_weapons = [self.clean_weapon_data(sw) for sw in sentinel_weapons] if sentinel_weapons else []
        cleaned_incarnon_weapons = [self.clean_weapon_data(inc) for inc in incarnon_weapons] if incarnon_weapons else []
        cleaned_amps = [self.clean_weapon_data(amp) for amp in amps] if amps else []

        # Save warframes to file
        warframes_file = os.path.join(self.processed_data_dir, 'warframes.json')
        with open(warframes_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_warframes, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved {len(cleaned_warframes)} warframes to warframes.json")
        
        # Save necramechs to file
        necramechs_file = os.path.join(self.processed_data_dir, 'necramechs.json')
        with open(necramechs_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_necramechs, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved {len(cleaned_necramechs)} necramechs to necramechs.json")
        
        # Save primary weapons to file
        primary_file = os.path.join(self.processed_data_dir, 'primary_weapons.json')
        with open(primary_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_primary_weapons, f, indent=2, ensure_ascii=False)
        # Save secondary weapons to file
        secondary_file = os.path.join(self.processed_data_dir, 'secondary_weapons.json')
        with open(secondary_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_secondary_weapons, f, indent=2, ensure_ascii=False)
        # Save melee weapons to file
        melee_file = os.path.join(self.processed_data_dir, 'melee_weapons.json')
        with open(melee_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_melee_weapons, f, indent=2, ensure_ascii=False)
        # Save zaws to file
        zaws_file = os.path.join(self.processed_data_dir, 'zaws.json')
        with open(zaws_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_zaws, f, indent=2, ensure_ascii=False)
        # Save kitguns to file
        kitguns_file = os.path.join(self.processed_data_dir, 'kitguns.json')
        with open(kitguns_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_kitguns, f, indent=2, ensure_ascii=False)
        # Save archwings to file
        archwings_file = os.path.join(self.processed_data_dir, 'archwings.json')
        with open(archwings_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_archwings, f, indent=2, ensure_ascii=False)
        # Save arch-guns to file
        arch_guns_file = os.path.join(self.processed_data_dir, 'arch_guns.json')
        with open(arch_guns_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_arch_guns, f, indent=2, ensure_ascii=False)
        # Save arch-melees to file
        arch_melees_file = os.path.join(self.processed_data_dir, 'arch_melees.json')
        with open(arch_melees_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_arch_melees, f, indent=2, ensure_ascii=False)
        # Save companions to file
        companions_file = os.path.join(self.processed_data_dir, 'companions.json')
        with open(companions_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_companions, f, indent=2, ensure_ascii=False)        
        # Save sentinel weapons to file
        sentinel_weapons_file = os.path.join(self.processed_data_dir, 'sentinel_weapons.json')
        with open(sentinel_weapons_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_sentinel_weapons, f, indent=2, ensure_ascii=False)
        # Save incarnon weapons to file
        incarnon_file = os.path.join(self.processed_data_dir, 'incarnon_weapons.json')
        with open(incarnon_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_incarnon_weapons, f, indent=2, ensure_ascii=False)
        # Save amps to file
        amps_file = os.path.join(self.processed_data_dir, 'amps.json')
        with open(amps_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_amps, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved {len(cleaned_amps)} amps to amps.json")

        # Show samples
        if cleaned_warframes:
            print("\nSample warframe:")
            sample = cleaned_warframes[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")
        
        if cleaned_necramechs:
            print("\nSample necramech:")
            sample = cleaned_necramechs[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")
            print(f"  unique_name: {sample.get('unique_name', 'Unknown')}")
        
        if cleaned_primary_weapons:
            print("\nSample primary weapon:")
            sample = cleaned_primary_weapons[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")
        
        if cleaned_secondary_weapons:
            print("\nSample secondary weapon:")
            sample = cleaned_secondary_weapons[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")
        
        if cleaned_melee_weapons:
            print("\nSample melee weapon:")
            sample = cleaned_melee_weapons[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")
        
        if cleaned_zaws:
            print("\nSample zaw component:")
            sample = cleaned_zaws[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")
        
        if cleaned_kitguns:
            print("\nSample kitgun component:")
            sample = cleaned_kitguns[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")
        
        if cleaned_archwings:
            print("\nSample archwing:")
            sample = cleaned_archwings[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")
        
        if cleaned_arch_guns:
            print("\nSample arch-gun:")
            sample = cleaned_arch_guns[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")
                
        if cleaned_arch_melees:
            print("\nSample arch-melee:")
            sample = cleaned_arch_melees[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")
        
        if cleaned_companions:
            print("\nSample companion:")
            sample = cleaned_companions[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")
        
        if cleaned_sentinel_weapons:
            print("\nSample sentinel weapon:")
            sample = cleaned_sentinel_weapons[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")

        if cleaned_incarnon_weapons:
            print("\nSample incarnon weapon:")
            sample = cleaned_incarnon_weapons[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")
                
        if cleaned_amps:
            print("\nSample amp:")
            sample = cleaned_amps[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")

def main():
    """Run the simple processor"""
    processor = WarframeDataProcessor()
    processor.process_warframes()

if __name__ == "__main__":
    main()