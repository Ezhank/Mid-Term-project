# UI Sketch and Vision

## Current State (MVP)

The current implementation prioritizes **functionality over aesthetics** with a clean, text-focused interface:
- Light theme with Pakistan-inspired green accents
- Sidebar-based filters for easy access
- Card layout for results
- No images (text-only for performance)

---

## Future Vision: Premium Visual Experience

The next iteration should transform PakAutos into a **visually immersive platform** that builds trust and excitement.

### Design Principles

1. **Visual First**: High-quality car photography as the primary attraction
2. **Data Transparency**: Clear pricing breakdowns, dealer locations, and history
3. **Guided Journey**: Progressive disclosure - don't overwhelm, guide users step-by-step
4. **Mobile Responsive**: 60% of Pakistani users access web on mobile
5. **Fast Loading**: Optimize images/assets for slow 3G connections

---

## Wireframe: Future Desktop Layout

```text
+-------------------------------------------------------------------------+
|  [🇵🇰 PakAutos]    [Home] [Compare] [Marketplace] [Financing]  [Ahmad ▾]|
+-------------------------------------------------------------------------+
|                                                                         |
|  +-------------------+  +-------------------------------------------+   |
|  | 💡 FILTERS       |  |  🔍 Search Results                        |   |
|  |                  |  +-------------------------------------------+   |
|  | Budget           |  |                                           |   |
|  | [====O=========] |  |  ┌─────────────────────────────────────┐ |   |
|  | 500k - 5Cr       |  |  │ [IMG]  Toyota Corolla 2023          │ |   |
|  |                  |  |  │        Rs. 2,200,000                │ |   |
|  | Usage            |  |  │        Petrol • Sedan • Used        │ |   |
|  | ○ City           |  |  │        ★★★★★ City: 9/10            │ |   |
|  | ● Family         |  |  │        [❤️ Save] [📊 Compare]       │ |   |
|  | ○ Performance    |  |  └─────────────────────────────────────┘ |   |
|  |                  |  |                                           |   |
|  | Fuel Type        |  |  ┌─────────────────────────────────────┐ |   |
|  | ☑ Petrol         |  |  │ [IMG]  Honda Civic 2022             │ |   |
|  | ☐ Diesel         |  |  │        Rs. 2,400,000                │ |   |
|  | ☐ Hybrid         |  |  │        Petrol • Sedan • New         │ |   |
|  | ☐ Electric       |  |  │        ★★★★☆ City: 8/10            │ |   |
|  |                  |  |  │        [❤️ Save] [📊 Compare]       │ |   |
|  | Condition        |  |  └─────────────────────────────────────┘ |   |
|  | ☑ New            |  |                                           |   |
|  | ☑ Used           |  |  ┌─────────────────────────────────────┐ |   |
|  |                  |  |  │ [IMG]  Suzuki Swift 2024            │ |   |
|  | [🔍 SEARCH]      |  |  │        Rs. 2,800,000                │ |   |
|  +-------------------+  |  │        Petrol • Hatchback • New     │ |   |
|                         |  │        ★★★★★ City: 10/10           │ |   |
|                         |  │        [❤️ Save] [📊 Compare]       │ |   |
|                         |  └─────────────────────────────────────┘ |   |
|                         +-------------------------------------------+   |
|                                                                         |
| [<< Previous]  [1] [2] [3] ... [10]  [Next >>]                        |
+-------------------------------------------------------------------------+
|  FOOTER: About | Privacy | Terms | Contact: support@pakautos.pk        |
+-------------------------------------------------------------------------+
```

---

## Wireframe: Car Detail Page (Future)

```text
+-------------------------------------------------------------------------+
|  🇵🇰 PakAutos    [← Back to Results]                      [Ahmad ▾]     |
+-------------------------------------------------------------------------+
|                                                                         |
|  +-----------------------------------+  +---------------------------+  |
|  |                                   |  | Toyota Corolla GLi 2023   |  |
|  |   [MAIN IMAGE - 800x600px]       |  |                           |  |
|  |   (Click to enlarge)              |  | Rs. 2,200,000             |  |
|  |                                   |  | 📍 Lahore, Punjab         |  |
|  +-----------------------------------+  |                           |  |
|  [Thumbnail1][Thumbnail2][Thumbnail3]  | [💬 Contact Seller]       |  |
|                                        | [📅 Schedule Test Drive]  |  |
|  Specifications                        | [💾 Save for Later]       |  |
|  ────────────────                      +---------------------------+  |
|  • Engine: 1.8L 4-Cylinder                                            |
|  • Transmission: Automatic                                            |
|  • Mileage: 25,000 km                                                 |
|  • Fuel Economy: 14 km/L                                              |
|                                                                        |
|  Ratings                                                               |
|  ────────                                                              |
|  City:        ████████░░ 8/10                                         |
|  Family:      ███████░░░ 7/10                                         |
|  Performance: ████░░░░░░ 4/10                                         |
|                                                                        |
|  Seller Notes                                                          |
|  ────────────                                                          |
|  "Well-maintained, single owner, full service history available."     |
+-------------------------------------------------------------------------+
```

---

## Key UI Decisions (Current MVP)

### Decision 1: Sidebar for Filters
**Rationale**: Keeps controls always visible without scrolling. Users can adjust preferences and see results update in real-time.

**Trade-off**: Reduces horizontal space for results, but acceptable on wide screens.

---

### Decision 2: Card Layout for Results
**Rationale**: 
- Each car is a self-contained unit (card metaphor)
- Easier to scan than table rows
- Allows for future expansion (add images, badges, ratings)

**Trade-off**: Less dense than a table, but more user-friendly for non-technical users.

---

### Decision 3: Progress Bar for Match Score
**Rationale**: Visual indicator is faster to interpret than raw numbers. A 9/10 score shows as 90% filled green bar.

**Trade-off**: Requires more vertical space per card.

---

### Decision 4: Light Theme (Not Dark)
**Rationale**: 
- Daylight usability (many users browse during work hours)
- Green/white colors evoke Pakistan flag for brand identity
- Better accessibility for older users (higher contrast)

**Trade-off**: Dark mode is trendy and reduces eye strain at night. Future version should offer toggle.

---

### Decision 5: Text-Only (No Images)
**Rationale**: 
- Faster page load, especially on 3G connections common in Pakistan
- Reduces hosting costs (no image CDN needed for MVP)
- Focuses attention on data rather than aesthetics

**Trade-off**: Less engaging. Users may feel less confident without visual confirmation of the car's appearance.

---

## Future Enhancements

1. **Image Gallery**: High-res photos with 360° interior view
2. **Comparison Tool**: Side-by-side comparison of 2-3 selected cars
3. **Dark Mode Toggle**: Preference-based theme switching
4. **Interactive Map**: Show dealer locations for test drives
5. **Video Reviews**: Embedded YouTube reviews from Pakistani automotive channels
6. **Financing Calculator**: Real-time EMI calculation with bank partner APIs

---

## Accessibility Considerations

- **Color Contrast**: Ensure WCAG AA compliance (4.5:1 ratio for text)
- **Keyboard Navigation**: All filters and buttons accessible via Tab key
- **Screen Reader Support**: Semantic HTML with proper ARIA labels
- **Mobile Touch Targets**: Minimum 44x44px for buttons (iOS HIG standard)
