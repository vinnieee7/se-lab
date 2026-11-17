# Lab 1: Requirements Engineering & UML Use-Case Modelling

## Student Details
- **Name:** A S Vincent
- **SRN:** PES2UG24CS002
- **Course:** Software Engineering Lab (5th Semester)

---

## Problem Statement
**Campus & Academic Operations: Smart Lab Equipment & Slot Reservation Portal**

### Project Overview
Engineering lab facilities require a specialized scheduling mechanism to prevent double-booking of high-value hardware instruments (oscilloscopes, logic analyzers, and FPGA development boards). The system must handle slot reservations, verify equipment calibration status, and enforce late-return disciplinary rules.

**Target Stakeholders / Actors:** Student, Lab Technician

---

## Deliverables Summary

1. **Requirements Table:**
   - **5 Functional Requirements (FR-001 to FR-005):**
     - `FR-001` [High]: Slot Reservation (up to 2 hours, 7 days in advance)
     - `FR-002` [High]: Equipment Calibration Status Updates (Calibrated / Under Maintenance / Retired)
     - `FR-003` [Medium]: Automatic Late-Return Penalty (48-hour booking suspension for >30 min delay)
     - `FR-004` [Medium]: Email/SMS Notifications (15 min prior reminder & cancellation alerts)
     - `FR-005` [Low]: Daily Lab Usage & Utilization Reports
   - **2 Non-Functional Requirements (NFR-001 & NFR-002):**
     - `NFR-001` [High]: Performance & Security (concurrent reservation requests ≤ 200 ms with DB-level lock isolation)
     - `NFR-002` [High]: Availability & Reliability (≥ 99.5% uptime during academic hours, automated failover < 10 mins)

2. **UML Use-Case Diagram:**
   - Actors: `Student`, `Lab Technician`, `System (Reservation Engine)`
   - Primary Use Cases:
     - `UC-01: Reserve Equipment Slot`
     - `UC-02: Cancel Reservation`
     - `UC-03: View Equipment Availability`
     - `UC-04: Update Calibration Status`
     - `UC-05: Generate Usage Report`
     - `UC-06: Authenticate User`
     - `UC-07: Apply Late-Return Penalty`
   - Key UML Relationships:
     - `UC-01` —`«include»`→ `UC-06` (Authentication is always required before reservation)
     - `UC-01` —`«extend»`→ `UC-07` (Late-return penalty is applied conditionally)

3. **Use-Case Flow Specification (UC-01: Reserve Equipment Slot):**
   - Detailed Preconditions, Postconditions, and 12-step Main Success Scenario.
   - Alternate Flow `AF-01`: Equipment Slot Becomes Unavailable (Race Condition handling).
   - Alternate Flow `AF-02`: Student Has Active Booking Suspension.

---

## File Deliverable
- [`PES2UG24CS002_Lab-1.pdf`](./PES2UG24CS002_Lab-1.pdf): Complete submission report containing the Requirements Table, PlantUML Use-Case Diagram, Use-Case Flow Specification, and references (IEEE Std 830-1998, PlantUML, Lucidchart).
