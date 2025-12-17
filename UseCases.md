# Use Cases

## Use Case 1: First-Time Buyer Finding a Budget City Car

**Actor**: User (First-time car buyer, limited budget)  
**Trigger**: User wants to purchase a reliable car under 30 Lakhs for daily office commute in Karachi.  
**Preconditions**: 
- User has created an account and is logged in
- Car database contains at least one vehicle matching criteria

**Main Flow**:
1. User navigates to the main dashboard after login
2. User selects **"City"** from the Primary Usage dropdown
3. User adjusts budget slider to **3,000,000 PKR** (30 Lakhs)
4. User selects **"Any"** for Condition (open to both new and used)
5. User selects **"Petrol"** for Fuel Type (most common in Pakistan)
6. User clicks **"Find My Ride"** button
7. System filters `cars.json` for:
   - Price ≤ 3,000,000
   - Fuel = "Petrol"
8. System scores remaining cars using "City" usage score
9. System sorts by score (descending), then price (ascending)
10. System displays top 3 results with:
    - Car name, price, condition, fuel type
    - Match score progress bar
    - City/Family/Performance metric breakdown
11. User reviews recommendations and notes down preferred options

**Expected Output**: 
- Toyota Corolla (Used, Petrol) - Score: 9/10
- Suzuki Swift (New, Petrol) - Score: 8.5/10  
- Honda City (Used, Petrol) - Score: 8/10

**Alternate Flow**:
- **No Match Found**: If budget is too restrictive (e.g., 500,000 PKR), system displays "😕 No matches found" with suggestion to increase budget or relax filters.

---

## Use Case 2: Family Head Searching for a Spacious SUV

**Actor**: User (Parent with 2 children)  
**Trigger**: User needs a safe, spacious vehicle for family trips to northern areas.  
**Preconditions**: User is logged in.

**Main Flow**:
1. User selects **"Family"** as Primary Usage
2. User sets budget to **8,000,000 PKR** (80 Lakhs)
3. User selects **"New"** for Condition (prioritizing safety/warranty)
4. User selects **"Any"** for Fuel Type
5. User clicks **"Find My Ride"**
6. System applies filters:
   - Price ≤ 8,000,000
   - Condition = "New"
7. System scores cars based on "Family" usage score (prioritizes space, safety, comfort)
8. System returns top 3:
   - Kia Sportage (New, Petrol, SUV) - Family Score: 10/10
   - Toyota Fortuner (New, Diesel, SUV) - Family Score: 9.5/10
   - Honda BR-V (New, Petrol, SUV) - Family Score: 9/10
9. User compares the three options using the metrics displayed

**Alternate Flow**:
- **User Refines Search**: If user wants hybrid for better fuel economy, they select "Hybrid" and re-search. System refreshes with new results (e.g., Toyota RAV4 Hybrid appears).

---

## Use Case 3: Enthusiast Looking for Performance Within Budget

**Actor**: User (Car enthusiast, young professional)  
**Trigger**: User wants a fast, fun car for weekend drives under 50 Lakhs.  
**Preconditions**: User is logged in.

**Main Flow**:
1. User selects **"Performance"** as Primary Usage
2. User sets budget to **5,000,000 PKR** (50 Lakhs)
3. User selects **"Any"** for Condition
4. User selects **"Petrol"** for Fuel Type (performance cars typically petrol)
5. User clicks **"Find My Ride"**
6. System filters by budget and fuel
7. System scores using "Performance" metric (engine power, acceleration, handling)
8. System displays:
   - Ford Mustang (Used, Petrol, Coupe) - Performance: 10/10
   - Honda Civic Type R (Used, Petrol, Sedan) - Performance: 9/10
   - Mazda MX-5 (New, Petrol, Convertible) - Performance: 8.5/10
9. User identifies the Mustang as best value for performance needs

**Alternate Flow**:
- **Electric Performance**: User selects "Electric" to see if Tesla Model 3 or other EVs fit budget. System displays results if available.

---

## High-Level System Design

```text
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERACTION                        │
│  (Browser: Chrome/Firefox/Safari accessing Streamlit Web App)  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     STREAMLIT FRONTEND                          │
│  ┌──────────────────┐         ┌───────────────────────┐       │
│  │  Login Page      │────────▶│  Main Dashboard       │       │
│  │  Signup Page     │         │  - Sidebar Filters    │       │
│  └──────────────────┘         │  - Results Display    │       │
│                               │  - Metrics Dashboard  │       │
│                               └───────────────────────┘       │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    APPLICATION LOGIC (app.py)                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  recommend_cars(budget, condition, fuel, usage)          │  │
│  │    1. Filter by budget (hard constraint)                │  │
│  │    2. Filter by condition (if not "Any")                │  │
│  │    3. Filter by fuel type (if not "Any")                │  │
│  │    4. Score using usage_scores[usage]                   │  │
│  │    5. Sort by score DESC, price ASC                     │  │
│  │    6. Return top 3                                       │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
   ┌──────────────────┐          ┌──────────────────┐
   │   cars.json      │          │   users.json     │
   │  (100 vehicles)  │          │  (credentials)   │
   │  - id            │          │  - username      │
   │  - make/model    │          │  - hashed_pw     │
   │  - price         │          └──────────────────┘
   │  - condition     │
   │  - fuel          │
   │  - usage_scores  │
   └──────────────────┘
```

## Data Flow Example

**Input**: Budget=3,000,000, Usage="City", Condition="Any", Fuel="Petrol"

**Processing**:
1. Load cars from `cars.json` → 100 entries
2. Filter: `price <= 3,000,000` → 45 matches
3. Filter: `fuel == "Petrol"` → 30 matches
4. Score: Extract `usage_scores["City"]` for each → [9, 8, 8.5, 7, ...]
5. Sort: By score DESC, price ASC → [(Corolla, 9), (Swift, 8.5), (City, 8)]
6. Return: Top 3

**Output**: Display 3 car cards with details
