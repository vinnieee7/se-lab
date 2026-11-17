# Lab 4: Vibe Coding — Pygame Frogger Game Fixes & Enhancements

## Student Details
- **Name:** A S Vincent
- **SRN:** PES2UG24CS002
- **Course:** Software Engineering Lab (5th Semester)
- **Source Repository:** [vinnieee7/frogger](https://github.com/vinnieee7/frogger)

---

## Lab Overview
The objective of this lab is to experience "Vibe Coding" — pair-programming and debugging with an LLM assistant to analyze, debug, and expand an existing Pygame-based implementation of the classic game **Frogger**.

---

## Completed Tasks

### Task 1 — Fix Vehicle Collision Detection
- **Issue:** Collisions between frog and vehicles were either failing to register or registering at incorrect bounding intervals.
- **Solution:** Replaced broken collision checks with precise `pygame.Rect.colliderect` bounding-box collision detection in `game/collisions.py`.

### Task 2 — Implement Lives and Respawn System
- **Feature:** Introduced a 3-life system (`self.lives = 3`).
- **Behavior:** On collision with a vehicle or when the timer expires, the frog loses one life and respawns at the starting zone (`(GRID_WIDTH // 2, GRID_HEIGHT - 1)`). When lives reach 0, game over is triggered.

### Task 3 — Implement Goal and Score Tracking
- **Feature:** Reaching the top row (`y == 0`) successfully counts as reaching the goal.
- **Behavior:** Increments score, resets position to the starting row for another round, and triggers a win state upon successfully completing all goal requirements.

### Task 4 — Add a 30-Second Countdown Timer
- **Feature:** Added a per-attempt 30-second countdown timer.
- **Behavior:** The remaining time is rendered dynamically on HUD. If the timer reaches 0, the attempt fails, a life is deducted, and the frog respawns.

---

## Deliverables & Evidence
- [`main.py`](./main.py): Game entry point.
- [`game/`](./game/): Core game engine, renderer, frog, vehicle, and collision modules.
- [`before_changes.avi`](./before_changes.avi): Screen recording demonstrating the buggy baseline game.
- [`after_changes.avi`](./after_changes.avi): Screen recording demonstrating the fully fixed and enhanced gameplay with collision detection, lives, timer, and score.
- [`chat_history.pdf`](./chat_history.pdf): Complete prompt engineering and chat interaction transcript with the AI assistant.
- [`Lab_4_VibeCoding_Student_handout.pdf`](./Lab_4_VibeCoding_Student_handout.pdf): Official lab specification handout.

---

## How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the game
python main.py

# Controls:
# - Arrow keys: Move Frog
# - R: Restart game
