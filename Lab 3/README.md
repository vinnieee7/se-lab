# Lab 3: Component Modelling & Architectural Pattern Selection

## Student Details
- **Name:** A S Vincent
- **SRN:** PES2UG24CS002
- **Course:** Software Engineering Lab (5th Semester)
- **Project:** Smart Lab Equipment & Slot Reservation Portal

---

## Architectural Pattern Analysis & Selection
We evaluated three major candidate architectural patterns for the Smart Lab Reservation Portal:

1. **Client-Server Architecture (Chosen — Best Fit):**
   - Centralized server with web/mobile clients.
   - Clean horizontal separation between Presentation (Client), Business Logic (Server), and Data Integration (Server).
   - Designed for concurrent multi-user campus access (Students and Lab Technicians).
   - Authoritative single source of truth for equipment inventory and slot bookings.
   - Centralized RBAC enforcement behind server interfaces (`IAuthService`, `ISlotBooking`).

2. **Layered Architecture:**
   - Single process monolithic unit; poor fit for distributed multi-user campus access.

3. **Microservices Architecture:**
   - Highly scalable with independent deployment, but over-engineered with significant RPC/network overhead for a campus-scale reservation portal.

---

## Component Identification & Layers

| # | Component | Architectural Layer | Responsibility |
|---|---|---|---|
| 1 | **Portal UI** | Presentation (Client) | Responsive web interface for students to browse and reserve slots, and technicians to manage calibration. |
| 2 | **Reservation Manager** | Business Logic (Server) | Core reservation engine; validates availability, enforces 2-hr booking limit, manages DB concurrency locks. |
| 3 | **Authentication Service** | Business Logic (Server) | Validates university credentials, handles session tokens, and enforces Role-Based Access Control (RBAC). |
| 4 | **Equipment Catalog** | Data / Integration (Server) | Stores inventory, specifications, maintenance logs, and real-time calibration states. |
| 5 | **Notification Service** | Data / Integration (Server) | Asynchronously dispatches email/SMS booking confirmations, 15-minute reminders, and penalty alerts. |

---

## UML Component Diagram
The UML component diagram models:
- Client-side `Portal UI` invoking server-side interfaces: `IUserInteraction`, `ISlotBooking`, `IAuthService`, `IEquipmentQuery`.
- Server-side component dependencies and ports between `Reservation Manager`, `Authentication Service`, `Equipment Catalog`, and `Notification Service`.

---

## File Deliverable
- [`Lab-3_PES2UG24CS002.pdf`](./Lab-3_PES2UG24CS002.pdf): Complete submission document featuring architectural trade-off analysis, component specification, UML component diagram, and full justifications.
