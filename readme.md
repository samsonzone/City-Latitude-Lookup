
# City Latitude Lookup

This Python script allows users to find **major cities (population > 500,000)** around the world that share the same **latitude** as a given city and state in the United States.

## Features
- Fetches latitude of a U.S. city and state using **Nominatim (OpenStreetMap)**.
- Filters cities with a **population > 500,000**.
- Lists matching cities **grouped by country**.
- No API keys required—completely **free** to use.

---

## Requirements
- **Python 3.8+**
- **pandas** and **requests** libraries.

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com/samsonzone/City-Latitude-Lookup/city-latitude-lookup.git
   cd city-latitude-lookup
   ```

2. **Run the script:**
   ```bash
   python3 citylookup.py <city> <state>
   ```

   Example:
   ```bash
   python3 citylookup.py syracuse ny
   ```

3. **Output Example:**
   ```
   Latitude of Syracuse, NY: 43.0481

   Major cities at the same latitude (grouped by country):
   Canada: Calgary
   China: Harbin
   Italy: Bologna, Florence
   Japan: Sapporo
   ```

---

## Dataset Information
- The script dynamically downloads the **SimpleMaps World Cities dataset** (https://simplemaps.com/data/world-cities).
- Filters cities with **population > 500,000**.

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contribution
Contributions are welcome!  
1. Fork the repository.  
2. Create a feature branch:
   ```bash
   git checkout -b feature-new-feature
   ```
3. Commit changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-new-feature
   ```
5. Open a Pull Request.

---

## Issues
If you encounter any problems, feel free to open an issue on the repository.

---

## Author
Created by Brian Samson
