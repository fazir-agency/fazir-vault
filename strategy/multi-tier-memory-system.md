# Multi-Tier Memory System — Agency Knowledge Architecture

**Date:** 2026-06-20
**Owner:** CEO (Fazir + AI)

## Overview

Sistem 3-tier untuk pastikan semua staff ada access kepada knowledge yang sama, terkini, dan boleh di-upgrade.

```
T1 (Hermes Memory) → T2 (Hindsight) → T3 (Obsidian Vault = sini)
```

## Tier 1 — Quick Memory (In-Session)

**Location:** Hermes built-in memory per profile
**Content:** Quick facts, active decisions, current context, API keys locations
**Lifetime:** Persistent across sessions
**Who reads:** Agent itu sendiri

## Tier 2 — Hindsight (Cross-Staff Summary)

**Location:** `~/.hermes/hindsight/latest.md`
**Content:** Cross-staff summaries, cron daily digest, active campaign intel
**Update:** Auto via cron daily 9AM
**Who reads:** CEO, staff leads

## Tier 3 — Obsidian Vault (Long-Term Knowledge Base)

**Location:** `~/vault/` (server) → GitHub `fazir-agency/fazir-vault` → MacBook Obsidian
**Content:** Strategy docs, playbooks, competitor analysis, product dossiers, setup guides
**Who reads:** ALL staff — ini shared knowledge base

### Folder Structure

```
vault/
├── _Shared/          # Active intel, shared across all staff
│   └── _active/      # Auto-pushed from Hindsight
├── _Staff/           # Per-staff notes
├── live-content/
│   ├── angles/       # Marketing angle breakdowns
│   ├── hooks/        # Hook library
│   ├── funnels/      # Funnel structures
│   └── competitors/  # Competitor intel
├── strategy/         # High-level strategy docs
└── playbooks/        # Step-by-step operational guides
```

## How Staff Use This Vault

1. **Before starting a task** → Check `_Shared/_active/` for latest intel
2. **Learning new tech** → Check `playbooks/` for setup guides
3. **Campaign work** → Check `live-content/` for angles & hooks
4. **After completing task** → Document lessons ke vault supaya staff lain boleh learn

## Sync Flow

```
CEO/Staff writes note → ~/vault/ → git push → GitHub → Obsidian Git pulls → Fazir's MacBook
```

Fazir buka Obsidian → nampak semua updates dari server terus.

## Why This Matters

Agency yang grow fast kena ada **institutional memory** — bukan bergantung pada satu orang je. Kalau ada staff baru join, dia boleh baca vault ni dan catch up dengan agency knowledge dalam masa singkat.
