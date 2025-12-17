# AI Utilization Log

## AI Tools Used

| Tool | Provider | Purpose |
|------|----------|---------|
| **Google Gemini-based** | Google DeepMind | Primary AI assistant for code generation, debugging, and documentation |
| **Streamlit** | Streamlit Inc. | Web framework (not AI, but enables rapid prototyping) |
| **Python Code Generation** | AI-assisted | Synthetic data generation scripts |

---

## Prompt Log

### Development Phase

* **Phase 1: Data & UI Foundation**
- Prompt Summary (P-1): "Create a Python script to generate 100 synthetic car data entries..."
- Purpose: Data Generation
- Outcome: Created generate_cars.py which populates cars.json with diverse vehicle data.

- Prompt Summary (P-2): "Build a Streamlit app with sidebar filters (budget slider, usage dropdown, condition radio, fuel dropdown) and main results area."
- Purpose: UI Scaffolding
- Outcome: Generated initial app.py structure with Streamlit components.

* **Phase 2: Core Logic & Security**
- Prompt Summary (P-3): "Implement a scoring algorithm that filters cars by budget/condition/fuel, then ranks by usage_scores[selected_usage]."
- Purpose: Core Logic
- Outcome: Created recommend_cars() function with multi-stage filtering and scoring.

- Prompt Summary (P-4): "Add user authentication with login/signup pages using hashed passwords stored in users.json."
- Purpose: Security Feature
- Outcome: Implemented SHA-256 password hashing and session management.

* **Phase 3: Aesthetics & Refinement**
- Prompt Summary (P-5): "Design light-theme CSS with Pakistan flag colors (green/white) using modern glassmorphism and smooth animations."
- Purpose: UI/UX Design
- Outcome: Generated custom CSS with gradient hero titles, card hover effects, and green accent colors.

- Prompt Summary (P-6): "Fix API quota exceeded error - add graceful degradation."
- Purpose: Error Handling
- Outcome: Initially attempted to add AI chatbot fallback, later removed chatbot entirely for simplicity.

- Prompt Summary (P-7): "Remove image display logic and delete images folder."
- Purpose: Optimization
- Outcome: Streamlined UI to text-only for faster loading and simpler codebase.

---

## Detailed Prompt Examples

### Prompt 1: Data Generation
**Full Prompt**:
```
"Generate a Python script that creates a JSON array of 100 car objects. 
Each car should have: id, make (choose from Toyota, Honda, BMW, etc.), 
model (realistic model names), price (in USD, range 15000-100000), 
condition (New or Used), fuel (Petrol/Diesel/Hybrid/Electric), 
type (Sedan/SUV/Truck/Hatchback), and usage_scores (dict with City, 
Family, Performance keys, values 0-10). Ensure diversity in makes and 
logical score assignments (e.g., sedans score high in City, SUVs in Family)."
```
**What it was used for**: Bootstrapping the car database without manual entry

**Result**: `generate_cars.py` script that intelligently assigns scores based on vehicle type heuristics

---

### Prompt 2: Authentication Implementation
**Full Prompt**:
```
"Add login/signup functionality to my Streamlit app. Store credentials in 
users.json with username as key and SHA-256 hashed password as value. 
Implement session state to persist login across page interactions. 
Show login and signup forms in a 3-column layout with the form centered."
```
**What it was used for**: Securing the application to demonstrate user management

**Result**: Complete authentication flow with persistent sessions via `st.query_params`

---

### Prompt 3: Debugging Chatbot (Later Removed)
**Full Prompt**:
```
"The chatbot is giving the same answer repeatedly. The AI isn't using 
conversation history and has low temperature (0.4). Fix by: adding 
chat_history parameter, increasing temperature to 0.7, limiting car 
context to top 10, and passing conversation history from Streamlit."
```
**What it was used for**: Attempted to improve chatbot responses

**Result**: Initially fixed, but later removed chatbot entirely when user found it unnecessary

---

## Reflection on AI Usage

### Usefulness

1. **Rapid Prototyping**: AI reduced development time from estimated 8-10 hours to 2-3 hours by generating boilerplate code instantly.

2. **Algorithmic Precision**: The scoring algorithm was complex (nested filters + sorting). AI correctly implemented the multi-stage logic on first attempt.

3. **Documentation Quality**: Generated markdown files maintained consistent professional tone and structure without manual formatting effort.

4. **Debugging Efficiency**: When encountering issues (e.g., repetitive chatbot responses), AI quickly diagnosed root causes (missing chat history, low temperature) and proposed solutions.

5. **Data Diversity**: Generated 100 realistic car entries with logical score assignments (e.g., Honda Civic scores high for City, Toyota Fortuner for Family) that would have been tedious to create manually.

### Risks and Limitations

1. **Over-Engineering**: AI initially suggested adding chatbot functionality, which added unnecessary complexity. Human judgment was needed to decide it wasn't essential for MVP.

2. **Dependency Risk**: Heavy reliance on AI-generated code meant less understanding of edge cases. For production systems, human review is critical.

3. **API Quota Limits**: The chatbot feature hit Gemini API rate limits quickly, demonstrating that "free tier" AI services aren't viable for high-traffic applications.

4. **Context Window Limits**: When sending all 100 cars to the AI for chatbot context, we hit token limits. Had to optimize to top 10 cars only.

5. **Hallucination in Documentation**: AI sometimes invented features that didn't exist (e.g., mentioning "comparison tool" in early README drafts). Required human verification.

### Best Practices Learned

- **Iterative Prompting**: Start with simple prompts, then refine based on results
- **Human-in-the-Loop**: Always review AI-generated code, especially security-critical sections (authentication)
- **Simplicity Over Features**: AI tends to suggest feature-rich solutions; humans must decide on scope
- **Fallback Mechanisms**: For AI features (like chatbot), always have a non-AI fallback to avoid complete failures

### Conclusion

AI was **highly beneficial** for this project, enabling rapid development of a functional MVP. However, critical decisions (removing chatbot, simplifying UI) required human judgment. The ideal workflow is **AI for acceleration + Human for direction**.
