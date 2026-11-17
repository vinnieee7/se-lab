# Software Engineering Laboratory (SE Lab)

Welcome to the comprehensive repository for the **Software Engineering Laboratory** course at **PES University**, Department of Computer Science & Engineering.

## Student Information
- **Student Name:** A S Vincent
- **SRN:** PES2UG24CS002
- **Semester:** 5th Semester B.Tech CSE
- **GitHub:** [@vinnieee7](https://github.com/vinnieee7)

---

## Repository Structure & Labs Overview

| Lab | Title / Topic | Domain / Tools | Key Deliverables |
|---|---|---|---|
| **[Lab 1](./Lab%201/)** | **Requirements Engineering & UML Use-Case Modelling** | IEEE 830, PlantUML | Requirements Table (FR-001 to FR-005, NFR-001 to NFR-002), UML Use-Case Diagram, Use-Case Flow Specification (UC-01 with Main & Alternate Flows). Report: [`PES2UG24CS002_Lab-1.pdf`](./Lab%201/PES2UG24CS002_Lab-1.pdf). |
| **[Lab 2](./Lab%202/)** | **Agile Backlog Creation & Sprint Simulation** | Atlassian Jira, Scrum | 5 Epics, 10 User Stories (38 Story Points), 2-sprint simulation, sprint carry-over analysis, and Burndown Chart verification. Report: [`PES2UG24CS002_SE_Lab2_Final_Report.pdf`](./Lab%202/PES2UG24CS002_SE_Lab2_Final_Report.pdf). |
| **[Lab 3](./Lab%203/)** | **Component Modelling & Architecture Selection** | Software Architecture, UML | Architectural style comparison (Client-Server vs. Layered vs. Microservices), component responsibility matrix, and UML Component Diagram. Report: [`Lab-3_PES2UG24CS002.pdf`](./Lab%203/Lab-3_PES2UG24CS002.pdf). |
| **[Lab 4](./Lab%204/)** | **Vibe Coding — Pygame Frogger Game Fixes** | Python, Pygame, AI-Assisted Dev | Bug fixes for vehicle collision detection, 3-life system with respawn, goal scoring & win state, 30s countdown timer. Source code, gameplay recordings ([`before_changes.avi`](./Lab%204/before_changes.avi), [`after_changes.avi`](./Lab%204/after_changes.avi)), and AI chat log [`chat_history.pdf`](./Lab%204/chat_history.pdf). |
| **[Lab 5](./Lab%205/)** | **Static Code Analysis & Linting** | Pylint, Flake8, Bandit | Audited and refactored `library_system.py`, resolved code smells, PEP 8 violations, and security vulnerabilities. Before/after reports, [`issues.md`](./Lab%205/issues.md), and [`reflection.md`](./Lab%205/reflection.md). |
| **[Lab 6](./Lab%206/)** | **Statement & Branch Coverage Analysis** | Pytest, Coverage.py | Achieved **100% Statement Coverage** and **100% Branch Coverage** on `water_utility_billing.py`. Full test suites (`CodeCoverageTest`, `BranchCoverageTest`), execution terminal screenshots, and detailed [`REPORT.md`](./Lab%206/REPORT.md). |
| **[Lab 7](./Lab%207/)** | **Property-Based Fuzz Testing** | Hypothesis, Pytest | Hardened `processor.py` against edge cases, discovered edge-case bugs with property-based fuzz tests in `test_processor.py`, and verified 100 passing test runs. Screenshots (SS1–SS4) and [`PES2UG24CS002_VINCENT_LAB7.pdf`](./Lab%207/PES2UG24CS002_VINCENT_LAB7.pdf). |

---

## Detailed Lab Summaries

### [Lab 1: Requirements Engineering & UML Use-Case Modelling](./Lab%201/)
- **Project:** *Smart Lab Equipment & Slot Reservation Portal*
- Formalized requirements engineering following IEEE Std 830-1998 for engineering lab equipment reservations.
- Developed a complete UML Use-Case model capturing primary student and technician interactions, along with `«include»` (authentication) and `«extend»` (late-return disciplinary penalty) relationships.

### [Lab 2: Agile Backlog Creation & Sprint Simulation in Jira](./Lab%202/)
- **Jira Project:** `SLESRP`
- Created 5 core epics covering equipment discovery, calibration, penalties, notifications, and analytics.
- Estimated 10 user stories using Fibonacci story points (38 total points) and simulated Sprint 1 & Sprint 2 execution on a Scrum board with burndown tracking.

### [Lab 3: Component Modelling & Architectural Pattern Selection](./Lab%203/)
- Evaluated architectural patterns for the campus reservation portal, selecting **Client-Server Architecture** for its multi-user concurrency, authoritative single source of truth, and robust server-side RBAC enforcement.
- Modeled subsystem boundaries and communication interfaces (`IUserInteraction`, `ISlotBooking`, `IAuthService`, `IEquipmentQuery`) in a UML Component Diagram.

### [Lab 4: Vibe Coding — Pygame Frogger](./Lab%204/)
- Pair-programmed with LLM assistance to debug and enhance a Pygame Frogger arcade game.
- Implemented pixel-accurate bounding box collisions, a 3-life respawn engine, goal tracking with win condition, and a 30-second per-attempt timer.

### [Lab 5: Static Code Analysis & Security Auditing](./Lab%205/)
- Analyzed a campus library loan and fine tracker (`library_system.py`) using **Flake8**, **Pylint**, and **Bandit**.
- Remediated high/medium severity security issues, resolved coding standard violations, and documented root-cause fixes in `issues.md` and `reflection.md`.

### [Lab 6: Code & Branch Coverage Analysis](./Lab%206/)
- Engineered unit test suites targeting a tiered water utility billing engine with leak deductions and tampering sensors (`water_utility_billing.py`).
- Attained **100% Statement Coverage** and **100% Branch Coverage** using `coverage run` and `pytest`.

### [Lab 7: Property-Based Fuzz Testing](./Lab%207/)
- Applied property-based testing using the **Hypothesis** framework to stress-test complex input invariants on a data processing pipeline (`processor.py`).
- Identified silent edge-case vulnerabilities, fortified input validations, and verified stability across hundreds of auto-generated pseudo-random test inputs.

---

## Getting Started

To explore or run the code in this repository:

```bash
# Clone the repository
git clone https://github.com/vinnieee7/se-lab.git
cd se-lab

# For Lab 4 (Frogger game)
cd "Lab 4"
pip install -r requirements.txt
python main.py

# For Lab 5 (Static Analysis)
cd ../"Lab 5"
pip install pylint bandit flake8
pylint library_system.py

# For Lab 6 (Coverage Testing)
cd ../"Lab 6"
pip install pytest coverage
pytest -v
coverage run --branch -m pytest BranchCoverageTest_water_utility_billing.py
coverage report -m

# For Lab 7 (Hypothesis Fuzz Testing)
cd ../"Lab 7"
pip install pytest hypothesis
pytest -v test_processor.py
```
