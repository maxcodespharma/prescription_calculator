# Prescription Calculator

A professional prescription calculation tool for pharmacy students and pharmacists. Handles multiple prescriptions in one session with comprehensive error handling.

## Features

- **Multi-prescription processing** in single session
- **Automatic calculations:**
  - Total quantity needed
  - Days supply verification
  - Cost estimation
  - Prescription sig generation
- **Input validation** with error handling
- **Summary reports** with grand total costs

## Technical Implementation

- **Language:** Python 3.13
- **Core Functions:**
  - `calculate_quantity_needed()` - Total tablets calculation
  - `calculate_days_supply()` - Days supply verification
  - `generate_sig()` - Formatted prescription directions
  - `calculate_cost()` - Cost with 2 decimal precision
- **Error Handling:** Try/except blocks with validation for negative values

## Usage
```bash
python prescription_calculator.py
```

Enter prescription details when prompted. Type 'done' to see summary.

## Sample Session
```
Drug: Metformin 500mg
Tablets per dose: 2
Doses per day: 2
Days supply: 30
Cost: $0.15

✅ Prescription added!

[Enter more prescriptions or type 'done']

SUMMARY:
Total Prescriptions: 3
Total Cost: $28.80
```

## Safety Features

- Validates positive values (no negative quantities)
- Type checking (prevents text in numeric fields)
- Empty input handling
- Controlled substance flagging

## Future Enhancements

- Export prescriptions to file
- Drug database integration
- Insurance coverage calculation
- Refill scheduling

## Tech + Learning Focus
This was my 2nd project and it helped me understand the differences between embedded code (my drug lookup database) vs using temporary memory via append(). While I didn't grasp this nuance at first, I had an AHA moment about it and wanted to share it here. I will continue to build upon my beginner-level programs, improving my overall fluency to bridge the gap between clinical pharmaceuticals and AI/coding knowledge.

## About

**Developer:** Max S. - Pre-PharmD Student  
**Start Date:** October 2025  
**Education:** Beginning PharmD program June 2026  
**Purpose:** Learning portfolio demonstrating AI + Pharmacy integration
**Disclaimer**: Self-taught; Built with guidance from AI assisted learning tools. My second Python project created during week 1 of the learning process.

**GitHub:** github.com/maxcodespharma

## Documentation Note

**Transparency about AI Assistance:**  
This README was structured with AI-assisted guidance as part of my learning process. While I wrote, tested, and understand all the code functionality, articulating professional technical documentation is a skill I'm actively developing.

**30-Day Documentation Challenge:**  
I'm committing to rewrite this README independently (without AI assistance) by **December 1, 2025** to demonstrate my growth in technical communication. The original version will remain visible in Git history for comparison.

**Last Updated:** October 31, 2025