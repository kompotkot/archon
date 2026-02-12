# Description

**Title:** Archon

## Overview

Archon is an LLM-based agent system that automates the C4 software architecture modeling workflow. It relies on role-specific expert agents that analyze a defined project brief and generate the System Context, Container, and Component views of the C4 model.

The system supports the generation and continuous tracking of human-readable architecture diagrams throughout the project lifecycle, addressing the common challenge of context loss in large software projects, especially when LLM-driven code generation is involved.

## Diagrams

If top-level C4 overview diagrams are defined, they can be found at:

- `context` - Level 1 System Context;
- `containers` - Level 2 Containers;
- `components` - Level 3 Components.

## Design

Workflow orchestration is implemented via LangGraph, which coordinates steps such as context ingestion, model proposal, refinement, validation, and artifact emission. The tool maintains persistent project state using a local files, allowing architectural sessions, and state history to survive across executions.

### Definitions

Project brief and requirements **provided by a human** as the starting point for the system defined in project repository.

Stores project-defined baseline information required to establish and maintain a shared architectural context, including system description, constraints, and requirements that guide design, analysis, and validation across all C4 levels.

### Expert Agent

The Expert Agent produces architectural decisions based on the provided project descriptions.

It iterates through all relevant entities, grouped by their zones of responsibility, and performs focused analysis for each scope. The outcome is a clearly structured architectural representation, while the agent’s reasoning and decision logic are captured in a transcript.

### Synthetic Agent

The Synthetic Agent transforms the expert’s free-form analysis into a strict text.

It validates relationships against existing diagrams that describe higher-level or adjacent C4 views to prevent isolated or inconsistent components. The agent generates a text-based C4 VIEW, creates visualization queues for containers or components when multiple views are required, and records its reasoning in a transcript.

### Diagram Agent

The Diagram Agent consumes visualization tasks from the queue, marks them as in progress, and converts the associated text-based VIEW into concrete diagrams according to the rules and documentation of the target visualization format (e.g., Mermaid). It then saves the generated diagrams to the diagrams directory and marks the tasks as completed.

### User stories

Short, numbered narratives that describe desired system behavior/outcomes.
