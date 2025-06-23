# Warframe Progress Tracker

A comprehensive progress tracking application for Warframe items including weapons, warframes, companions, and equipment.

## Project Overview

This project tracks your progress across all major Warframe item categories:
- Primary Weapons
- Secondary Weapons  
- Melee Weapons
- Warframes
- Kitguns
- Zaws
- Companions
- Necramechs (Voidrigs)
- Archwings
- Archguns
- Archmelees
- Mods
- Robotics
- Amps
- Incarnon Weapons
- Vehicles

## Project Structure

```
warframe-tracker/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── scraper/
│   │   ├── __init__.py
│   │   ├── wfcd_scraper.py
│   │   └── data_processor.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── schema.sql
│   ├── tracker/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   └── templates/
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── data/
│   ├── raw/
│   └── processed/
└── tests/
    ├── __init__.py
    └── test_scraper.py
```

## Setup Instructions

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the scraper: `python src/scraper/wfcd_scraper.py`
4. Process the data: `python src/scraper/data_processor.py`
5. Start the tracker: `python src/tracker/app.py`

## Data Source

This project uses the WFCD (Warframe Community Developers) API and data sources for accurate, up-to-date Warframe item information.

## License

MIT License