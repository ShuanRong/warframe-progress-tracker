"""
WFCD API Client for fetching Warframe items data
Uses the warframe-items JSON data from WFCD GitHub repository
"""

import requests
import json
import os
from typing import Dict, List, Optional
import time

class WFCDClient:
    """Client for fetching Warframe data from WFCD sources"""
    
    def __init__(self, cache_dir: str = "data/raw"):
        self.base_url = "https://raw.githubusercontent.com/WFCD/warframe-items/master/data/json"
        self.cache_dir = cache_dir
        self.session = requests.Session()
        
        # Ensure cache directory exists
        os.makedirs(cache_dir, exist_ok=True)
        
        # Map of item types to their corresponding JSON files
        self.endpoints = {
            'primary': 'Primary.json',
            'secondary': 'Secondary.json', 
            'melee': 'Melee.json',
            'warframes': 'Warframes.json',
            'kitguns': 'Primary.json',  # Kitguns are in Primary
            'zaws': 'Melee.json',       # Zaws are in Melee
            'companions': 'Pets.json',
            'sentinels': 'Sentinels.json',
            'voidrigs': 'Warframes.json',  # Necramechs are in Warframes
            'archwings': 'Archwing.json',
            'archguns': 'Arch-Gun.json',
            'archmelees': 'Arch-Melee.json',
            'mods': 'Mods.json',
            'robotics': 'Gear.json',      # Robotics might be in Gear
            'amps': 'Primary.json',        # Amps might be in Primary
            'incarnons': 'Primary.json',   # Incarnon weapons in Primary/Secondary/Melee
            'vehicles': 'Misc.json',        # Vehicles likely in Misc
            'sentinelweapons': 'SentinelWeapons.json',  # Sentinel weapons
        }
    
    def fetch_json(self, filename: str, force_refresh: bool = False) -> Optional[Dict]:
        """Fetch JSON data from WFCD repository"""
        cache_file = os.path.join(self.cache_dir, filename)
        
        # Use cached version if exists and not forcing refresh
        if os.path.exists(cache_file) and not force_refresh:
            print(f"Loading cached {filename}")
            with open(cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # Fetch from remote
        url = f"{self.base_url}/{filename}"
        print(f"Fetching {filename} from {url}")
        
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            # Cache the data
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"✓ Successfully fetched and cached {filename}")
            return data
            
        except requests.RequestException as e:
            print(f"✗ Error fetching {filename}: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"✗ Error parsing JSON for {filename}: {e}")
            return None
    
    def fetch_primary_weapons(self) -> List[Dict]:
        """Fetch all primary weapons including kitguns and amps"""
        data = self.fetch_json('Primary.json')
        if not data:
            return []
        
        # Filter for different types
        primaries = []
        kitguns = []
        amps = []
        
        for item in data:
            if 'kitgun' in item.get('name', '').lower() or 'kitgun' in item.get('category', '').lower():
                kitguns.append(item)
            elif 'amp' in item.get('name', '').lower() or 'amp' in item.get('category', '').lower():
                amps.append(item)
            else:
                primaries.append(item)
        
        print(f"✓ Found {len(primaries)} primary weapons, {len(kitguns)} kitguns, {len(amps)} amps")
        return {
            'primary': primaries,
            'kitguns': kitguns, 
            'amps': amps
        }
    
    def fetch_secondary_weapons(self) -> List[Dict]:
        """Fetch all secondary weapons"""
        data = self.fetch_json('Secondary.json')
        if not data:
            return []
        
        print(f"✓ Found {len(data)} secondary weapons")
        return data
    
    def fetch_melee_weapons(self) -> List[Dict]:
        """Fetch all melee weapons including zaws"""
        data = self.fetch_json('Melee.json')
        if not data:
            return []
        
        # Separate zaws from regular melee
        melee = []
        zaws = []
        
        for item in data:
            if 'zaw' in item.get('name', '').lower() or 'zaw' in item.get('category', '').lower():
                zaws.append(item)
            else:
                melee.append(item)
        
        print(f"✓ Found {len(melee)} melee weapons, {len(zaws)} zaws")
        return {
            'melee': melee,
            'zaws': zaws
        }
    
    def fetch_warframes(self) -> List[Dict]:
        """Fetch all warframes including necramechs"""
        data = self.fetch_json('Warframes.json')
        if not data:
            return []
        
        # Separate warframes from necramechs
        warframes = []
        voidrigs = []
        
        for item in data:
            if 'necramech' in item.get('name', '').lower() or 'mech' in item.get('category', '').lower():
                voidrigs.append(item)
            else:
                warframes.append(item)
        
        print(f"✓ Found {len(warframes)} warframes, {len(voidrigs)} necramechs")
        return {
            'warframes': warframes,
            'voidrigs': voidrigs
        }
    
    def fetch_companions(self) -> Dict[str, List[Dict]]:
        """Fetch all companions (pets and sentinels)"""
        pets_data = self.fetch_json('Pets.json') or []
        sentinels_data = self.fetch_json('Sentinels.json') or []
        
        print(f"✓ Found {len(pets_data)} pets, {len(sentinels_data)} sentinels")
        return {
            'pets': pets_data,
            'sentinels': sentinels_data
        }
    
    def fetch_archwing_items(self) -> Dict[str, List[Dict]]:
        """Fetch all archwing related items"""
        archwings = self.fetch_json('Archwing.json') or []
        archguns = self.fetch_json('Arch-Gun.json') or []
        archmelees = self.fetch_json('Arch-Melee.json') or []
        
        print(f"✓ Found {len(archwings)} archwings, {len(archguns)} arch-guns, {len(archmelees)} arch-melees")
        return {
            'archwings': archwings,
            'archguns': archguns,
            'archmelees': archmelees
        }
    
    def fetch_mods(self) -> List[Dict]:
        """Fetch all mods"""
        data = self.fetch_json('Mods.json')
        if not data:
            return []
        
        print(f"✓ Found {len(data)} mods")
        return data
    
    def fetch_misc_items(self) -> Dict[str, List[Dict]]:
        """Fetch miscellaneous items including gear, vehicles, etc."""
        gear_data = self.fetch_json('Gear.json') or []
        misc_data = self.fetch_json('Misc.json') or []
        
        # Try to identify robotics and vehicles from the data
        robotics = []
        vehicles = []
        other_gear = []
        other_misc = []
        
        for item in gear_data:
            name_lower = item.get('name', '').lower()
            if any(keyword in name_lower for keyword in ['spectre', 'beacon', 'cipher']):
                robotics.append(item)
            else:
                other_gear.append(item)
        
        for item in misc_data:
            name_lower = item.get('name', '').lower()
            if any(keyword in name_lower for keyword in ['k-drive', 'vehicle', 'hoverboard']):
                vehicles.append(item)
            else:
                other_misc.append(item)
        
        print(f"✓ Found {len(robotics)} robotics, {len(vehicles)} vehicles, {len(other_gear)} other gear, {len(other_misc)} other misc")
        return {
            'robotics': robotics,
            'vehicles': vehicles,
            'gear': other_gear,
            'misc': other_misc
        }
    
    def fetch_incarnon_weapons(self) -> List[Dict]:
        """Fetch incarnon weapons from all weapon categories"""
        incarnons = []
        
        # Check all weapon types for incarnon variants
        for weapon_type in ['Primary.json', 'Secondary.json', 'Melee.json']:
            data = self.fetch_json(weapon_type) or []
            for item in data:
                name_lower = item.get('name', '').lower()
                description = item.get('description', '').lower()
                if 'incarnon' in name_lower or 'incarnon' in description:
                    incarnons.append(item)
        
        print(f"✓ Found {len(incarnons)} incarnon weapons")
        return incarnons
    
    def fetch_sentinel_weapons(self) -> List[Dict]:
        """Fetch all sentinel weapons"""
        data = self.fetch_json('SentinelWeapons.json')
        if not data:
            return []
        
        print(f"✓ Found {len(data)} sentinel weapons")
        return data
    
    def fetch_all_data(self, force_refresh: bool = False) -> Dict[str, any]:
        """Fetch all Warframe data"""
        print("=== Starting WFCD Data Fetch ===")
        start_time = time.time()
        
        all_data = {}
        
        # Fetch all categories
        primary_data = self.fetch_primary_weapons()
        all_data.update(primary_data)
        
        all_data['secondary'] = self.fetch_secondary_weapons()
        
        melee_data = self.fetch_melee_weapons()
        all_data.update(melee_data)
        
        warframe_data = self.fetch_warframes()
        all_data.update(warframe_data)
        
        companion_data = self.fetch_companions()
        all_data.update(companion_data)
        
        all_data['sentinelweapons'] = self.fetch_sentinel_weapons()

        archwing_data = self.fetch_archwing_items()
        all_data.update(archwing_data)
        
        all_data['mods'] = self.fetch_mods()
        
        misc_data = self.fetch_misc_items()
        all_data.update(misc_data)
        
        all_data['incarnons'] = self.fetch_incarnon_weapons()
        
        elapsed_time = time.time() - start_time
        print(f"\n=== Data Fetch Complete in {elapsed_time:.2f}s ===")
        
        # Print summary
        total_items = sum(len(items) if isinstance(items, list) else 0 for items in all_data.values())
        print(f"Total items fetched: {total_items}")
        
        for category, items in all_data.items():
            if isinstance(items, list):
                print(f"  {category}: {len(items)} items")
        
        return all_data

def main():
    """Test the WFCD client"""
    client = WFCDClient()
    
    # Fetch all data
    data = client.fetch_all_data()
    
    # Save summary to file
    summary = {category: len(items) if isinstance(items, list) else 0 
               for category, items in data.items()}
    
    with open('data/raw/fetch_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nSummary saved to data/raw/fetch_summary.json")

if __name__ == "__main__":
    main()