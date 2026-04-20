# Project Structure

```
.
├── .kiro/
│   ├── specs/
│   │   └── semantic-network-agent/   # Feature spec for the main project
│   │       ├── .config.kiro          # Spec config (requirements-first workflow)
│   │       └── requirements.md       # Detailed requirements document (Spanish)
│   └── steering/                     # Steering rules for AI assistant guidance
├── context/                          # Reference materials (PDFs)
│   ├── capitulo_2.pdf                # Textbook Ch.2 — Intelligent Agents
│   ├── capitulo_10.pdf               # Textbook Ch.10 — Knowledge Representation
│   └── trabajo_final.pdf             # Final project guidelines / rules
```

## Conventions

- **Spec files** live under `.kiro/specs/{feature-name}/` and follow the requirements-first workflow
- **Reference PDFs** are stored in `context/` — these are read-only source materials, not generated outputs
- **Documentation language**: Spanish for all academic and requirements documents
- As the prototype develops, source code should be organized in a dedicated directory (e.g., `src/` or `agent/`)

## Key Files

| File | Purpose |
|------|---------|
| `requirements.md` | 7 formal requirements covering problem statement, justification, research questions, objectives, state of the art, scope, and document structure |
| `trabajo_final.pdf` | Project rules and evaluation criteria — consult before making structural decisions about the research document |
| `capitulo_2.pdf` | Theoretical foundation for intelligent agent design (PEAS, agent types, task environments) |
| `capitulo_10.pdf` | Theoretical foundation for semantic networks and knowledge representation |
