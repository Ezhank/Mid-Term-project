# Problem Statement: Finding the Perfect Car in Pakistan's Complex Market

## 1. The User
The primary user is a **Pakistani car buyer** navigating a challenging automotive market with limited transparent information and volatile pricing. They include:
- **First-time buyers** seeking reliable, affordable transportation
- **Family heads** requiring safe, spacious vehicles
- **Professionals** prioritizing fuel efficiency for daily commutes
- **Enthusiasts** seeking performance within budget constraints

## 2. The Pain Point
Buying a car in Pakistan presents unique challenges:
- **Information Overload**: Thousands of listings across multiple platforms with inconsistent data
- **No Objective Guidance**: Buyers rely on word-of-mouth rather than data-driven recommendations
- **Price Volatility**: Rapid currency fluctuations and import duty changes make pricing unpredictable
- **Decision Paralysis**: Choosing between new locally-assembled vs. used imported vehicles requires expert knowledge
- **Limited Comparison Tools**: No centralized platform to compare vehicles based on specific use cases

## 3. Why It Matters
A car is typically the second-largest household investment after property. Poor decisions result in:
- **Financial loss** through depreciation and unexpected maintenance costs
- **Lifestyle mismatch** (e.g., city sedan on rural roads, or SUV for solo commuting)
- **Safety risks** from purchasing vehicles with inadequate safety features
- **Opportunity cost** of capital tied up in unsuitable assets

## 4. MVP Goal
Build **PakAutos**, a web-based car recommendation system that:
1. Accepts simple user inputs (Budget, Primary Usage, Condition, Fuel Type)
2. Filters a curated database of 100 popular vehicles
3. Uses a **usage-based scoring algorithm** to rank matches
4. Presents the top 3 recommendations with clear justifications
5. Provides transparent pricing in PKR

## 5. Scope
**Included in MVP:**
- Interactive web interface built with Streamlit
- JSON-based car database with ~100 entries
- Multi-factor scoring system (City, Family, Performance ratings)
- Hard filters for budget, condition, and fuel type
- User authentication (login/signup)
- Persistent session management
- Database insights dashboard

**Core Algorithm:**
- Score cars based on usage intention (City/Family/Performance)
- Apply strict filters for budget, condition, and fuel preferences
- Return top 3 matches sorted by score, then price

## 6. Out of Scope (for MVP)
- Real-time price updates from marketplaces (OLX, PakWheels)
- Direct buying/selling transactions
- Vehicle history reports or mechanical inspections
- Loan/financing calculators
- Mobile native applications (iOS/Android)
- AI chatbot recommendations (removed for simplicity)
- Image galleries (text-only interface for performance)

## 7. Assumptions
- Car prices are representative averages in PKR (may vary by region/dealer)
- Usage scores are assigned based on industry expert consensus
- Users have basic internet literacy and access to a web browser
- The scoring system's weights (City: compact+economy, Family: space+safety, Performance: power+handling) align with Pakistani buyer priorities
- Data is refreshed periodically but not in real-time
