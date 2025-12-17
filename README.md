# PakAutos - Smart Car Recommendation System 🚗🇵🇰

**Midterm Project - Software Engineering**  
**Option 5: Best-Fit Car Finder**

---

## Overview

**PakAutos** is an intelligent web application designed to simplify car purchasing decisions for Pakistani buyers. By leveraging a curated database of 100 popular vehicles and a sophisticated usage-based scoring algorithm, PakAutos matches users with their ideal car based on budget, usage patterns, and preferences.

### Key Features
✅ **Smart Filtering** - Filter by budget, condition (New/Used), and fuel type  
✅ **Usage-Based Scoring** - Vehicles rated for City, Family, or Performance use cases  
✅ **Top 3 Recommendations** - Ranked by suitability score and value  
✅ **User Authentication** - Secure login/signup with persistent sessions  
✅ **Database Insights** - Dashboard showing catalog statistics  
✅ **Clean Interface** - Text-focused design for fast loading and clarity

---

## Technology Stack

- **Frontend/Backend**: Streamlit (Python web framework)
- **Database**: JSON file-based storage (`cars.json`, `users.json`)
- **Authentication**: SHA-256 password hashing
- **Styling**: Custom CSS with light theme
- **Data Generation**: Python scripts for synthetic data

---

## Project Structure

```
Mid-Term/
├── app.py                      # Main Streamlit application
├── cars.json                   # 100-vehicle database
├── users.json                  # User credentials store
├── generate_cars.py            # Utility to expand car database
├── .env                        # Environment variables (API keys)
├── .streamlit/config.toml      # Streamlit configuration
│
├── ProblemStatement.md         # Project context and goals
├── UseCases.md                 # Detailed use cases with diagrams
├── README.md                   # This file
├── TestPlan.md                 # Test cases and validation
├── AI-log.md                   # AI tool usage documentation
├── UI-Sketch-and-Vision.md     # UI design decisions
└── ReleaseRoadmap.md           # Future development plan
```

---

## How to Run

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone or download the project**:
   ```bash
   cd Mid-Term
   ```

2. **Install dependencies**:
   ```bash
   pip install streamlit pandas python-dotenv
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

4. **Access the app**:
   - Open your browser at `http://localhost:8501`
   - Create an account or login
   - Set your preferences and click "Find My Ride"

---

## Example Usage

### Scenario 1: Budget City Car
**Input**:
- Budget: 30,00,000 PKR (30 Lakhs)
- Usage: City
- Condition: Any
- Fuel: Petrol

**Output**:
```
#1 Toyota Corolla (Used, Petrol, Sedan) - Rs. 2,200,000
   Match Score: 9/10
   City: 9/10 | Family: 7/10 | Performance: 4/10

#2 Suzuki Swift (New, Petrol, Hatchback) - Rs. 2,800,000
   Match Score: 8.5/10
   City: 10/10 | Family: 5/10 | Performance: 6/10

#3 Honda City (Used, Petrol, Sedan) - Rs. 2,400,000
   Match Score: 8/10
   City: 8/10 | Family: 7/10 | Performance: 6/10
```

### Scenario 2: Family SUV
**Input**:
- Budget: 80,00,000 PKR (80 Lakhs)
- Usage: Family
- Condition: New
- Fuel: Any

**Output**:
```
#1 Kia Sportage (New, Petrol, SUV) - Rs. 7,500,000
   Match Score: 10/10
   Family: 10/10

#2 Toyota Fortuner (New, Diesel, SUV) - Rs. 7,900,000
   Match Score: 9.5/10
   Family: 9/10
```

---

## Algorithm Logic

The core recommendation engine follows this workflow:

1. **Hard Filters**:
   - Exclude cars above budget
   - Filter by condition if specified
   - Filter by fuel type if specified

2. **Scoring**:
   - Extract the usage score for selected category (City/Family/Performance)
   - Each car has pre-assigned scores (0-10) for each category

3. **Ranking**:
   - Sort by score (descending)
   - Tie-break by price (ascending - cheaper is better)

4. **Return**:
   - Top 3 matches displayed with full details

---

## Database Schema

### cars.json
```json
{
  "id": 1,
  "make": "Toyota",
  "model": "Corolla",
  "price": 2200000,
  "condition": "Used",
  "fuel": "Petrol",
  "type": "Sedan",
  "usage_scores": {
    "City": 9,
    "Family": 7,
    "Performance": 4
  }
}
```

### users.json
```json
{
  "username": "sha256_hashed_password"
}
```

---

## Future Enhancements

See [ReleaseRoadmap.md](ReleaseRoadmap.md) for planned features:
- Real-time price integration from marketplaces
- Financing calculator
- Comparison tool for side-by-side analysis
- Mobile app (iOS/Android)

---

## Contributors

Built by **[Your Name]** for the Software Engineering Midterm Project, December 2025.

---

## License

This project is submitted for academic evaluation and is not licensed for commercial use.
