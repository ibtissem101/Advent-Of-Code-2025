## Day 1 - Safe Dial Puzzle 

### Overview
You're trying to crack a safe with a circular dial that has numbers 0-99. The dial starts at position **50**, and you're given a series of rotation instructions in the format:
- `L##` - Turn left (counterclockwise) by ## positions
- `R##` - Turn right (clockwise) by ## positions

### Part 1: Count Final Position Hits
**Question:** How many times does the dial land on **0** after completing each rotation?

**Algorithm:**
1. Start at position 50
2. For each instruction:
   - Perform the entire rotation at once
   - Check if the final position is 0
   - If yes, increment counter
3. Use modulo 100 to wrap around the circular dial

**Example:**
```
Start: position = 50
L68: 50 - 68 = -18 → -18 % 100 = 82
L30: 82 - 30 = 52
R48: 52 + 48 = 100 → 100 % 100 = 0 (count = 1)
```

**Key Insight:** We only check the position **after each complete rotation**, not during it.

---

### Part 2: Count All Zero Crossings
**Question:** How many times does the dial **pass through or land on** 0 during all the rotations?

**Algorithm:**
1. Start at position 50
2. For each instruction:
   - Move **one position at a time**
   - Check if position == 0 after each single step
   - If yes, increment counter
3. This counts every time we touch 0, not just final positions

**Example:**
```
L68 from position 50:
50 → 49 → 48 → ... → 1 → 0 ★ (count +1) → 99 → 98 → ... → 82
This single L68 command passes through 0 once!
```

**Key Insight:** A large rotation like `L68` or `R80` can pass through 0 even if it doesn't end there. We count **every crossing**.

---


---

### Example Test Case
Given: `L68, L30, R48, L5, R60, L55, L1, L99, R14, L82`

**Part 1 Answer:** 3 (dial lands on 0 exactly 3 times)  
**Part 2 Answer:** Higher number (counts all times passing through 0)

---

### Files
- `day1-part1.py` - Solution for Part 1 (endpoint checking)
- `day1-part2.py` - Solution for Part 2 (step-by-step checking)
- `input.txt` - Puzzle input with 4485 rotation instructions