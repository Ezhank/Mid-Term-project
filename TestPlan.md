# Test Plan

## Test Case 1: Successful User Registration and Login

**Category**: Positive Test (Normal Flow)

**Description**: Verify that a new user can register and subsequently log in to access the system.

**Input**:
- Username: "testuser"
- Password: "securepass123"
- Confirm Password: "securepass123"

**Steps**:
1. Navigate to the application home page
2. Click "New here? Create Account" button
3. Enter username "testuser"
4. Enter password "securepass123"
5. Confirm password "securepass123"
6. Click "Sign Up" button
7. Navigate to login page
8. Enter credentials
9. Click "Log In" button

**Expected Output**:
- Account creation success message displayed
- Redirect to login page
- After login, user sees "Hi, testuser!" in sidebar
- Access to main dashboard granted

**Actual Output**: Will match after execution

---

## Test Case 2: Car Search with Standard Budget (Positive)

**Category**: Positive Test (Normal Flow)

**Description**: Verify that the recommendation system returns appropriate results for a typical budget.

**Input**:
- Budget: 5,000,000 PKR (50 Lakhs)
- Usage: "City"
- Condition: "Any"
- Fuel: "Petrol"

**Steps**:
1. Log in to the system
2. Set budget slider to 5,000,000
3. Select "City" from Primary Usage dropdown
4. Select "Any" for Condition
5. Select "Petrol" for Fuel Type
6. Click "Find My Ride" button

**Expected Output**:
- System displays top 3 cars
- All displayed cars have:
  - Price ≤ 5,000,000 PKR
  - Fuel type = "Petrol"
  - High "City" usage score (7+/10)
- Results sorted by City score (descending), then price (ascending)
- Each car shows: name, price, condition, fuel, match score, and metric breakdown

**Actual Output**: Will match after execution

---

## Test Case 3: Zero Results for Impossible Criteria (Negative)

**Category**: Negative Test (Edge Case)

**Description**: Verify graceful handling when no cars match the user's criteria.

**Input**:
- Budget: 500,000 PKR (5 Lakhs - extremely low)
- Usage: "Performance"
- Condition: "New"
- Fuel: "Electric"

**Steps**:
1. Log in to the system
2. Set budget slider to 500,000
3. Select "Performance" usage
4. Select "New" condition
5. Select "Electric" fuel
6. Click "Find My Ride"

**Expected Output**:
- System displays warning message: "😕 No matches found."
- No car cards displayed
- Suggestion to adjust filters (implicit in UI/future enhancement)
- System does NOT crash or show error traces

**Actual Output**: Will match after execution

---

## Test Case 4: Login with Invalid Credentials (Negative)

**Category**: Negative Test (Security)

**Description**: Verify that the system rejects incorrect credentials and provides appropriate feedback.

**Input**:
- Username: "admin"
- Password: "wrongpassword"

**Steps**:
1. Navigate to login page
2. Enter username "admin"
3. Enter incorrect password "wrongpassword"
4. Click "Log In" button

**Expected Output**:
- Login rejected
- Error message displayed: "Invalid username or password"
- User remains on login page
- No access to dashboard granted

**Actual Output**: Will match after execution

---

## Test Case 5: Filter Interaction - Fuel Type Hard Filter (Positive)

**Category**: Positive Test (Filter Validation)

**Description**: Verify that the fuel type filter works as a hard constraint (not soft scoring).

**Input**:
- Budget: 10,000,000 PKR (1 Crore)
- Usage: "Family"
- Condition: "Any"
- Fuel: "Hybrid"

**Steps**:
1. Log in to the system
2. Set budget slider to 10,000,000
3. Select "Family" usage
4. Select "Hybrid" fuel type
5. Click "Find My Ride"

**Expected Output**:
- All displayed cars have Fuel = "Hybrid"
- No Petrol, Diesel, or Electric cars shown (even if they have high Family scores)
- If no hybrid cars exist under budget, show "No matches found"
- Results sorted by Family score

**Actual Output**: Will match after execution

---

## Summary of Test Coverage

| Test ID | Category | Focus Area | Pass Criteria |
|---------|----------|------------|---------------|
| TC-1 | Positive | Authentication | User can register and login |
| TC-2 | Positive | Search Logic | Returns correct filtered results |
| TC-3 | Negative | Edge Case | Handles no results gracefully |
| TC-4 | Negative | Security | Rejects invalid credentials |
| TC-5 | Positive | Filtering | Fuel filter works as hard constraint |

**Coverage**: Authentication, Core Search Algorithm, Filter Logic, Error Handling, Edge Cases
