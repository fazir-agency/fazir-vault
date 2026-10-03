---
type: ops-index
date: 2026-10-03
tags: [ads-ops, media-buying, meta-ads, index]
---

# 🎯 Ads Ops — Otak Media Buyer

`knowledge/` (folder lain) = **ilmu** — swipe file, hook, angle dari IG/FB.
**Folder ni** = **operasi** — macam mana Fazir sebenarnya jalankan iklan, apa yang jadi, apa counter dia.

## Sumber ilmu

| Sumber | Jenis | Cara masuk |
|---|---|---|
| 📊 Google Sheet **"Ads Log"** | Data berstruktur (campaign, spend, CPA, keputusan) | Hub baca terus via Sheets API |
| 📓 Obsidian **office** | Nota pengalaman, apa jadi, counter-measure | Repo berasingan (`office-brain`) |
| 💬 **Mesej ke CEO bot** | Ilmu lisan / ad-hoc | Bot fail ke fail yang betul di sini |

## ⚠️ Aliran SATU HALA

```
OFFICE  ──►  HUB (VPS)  ──►  iklan personal
```

- Office **tidak pernah** baca vault personal
- Repo office = repo **berasingan** (`office-brain`), read-only untuk hub
- Yang mengalir keluar dari office: **pola & pengajaran**, bukan credential

## Fail dalam folder ni

| Fail | Isi |
|---|---|
| `00-sop-harian.md` | Checklist harian, rule escalate |
| `01-ads-log.md` | Cara hub baca Google Sheet Ads Log |
| `02-budget-scaling.md` | Rule naik/turun budget, learning phase |
| `03-metrics-benchmark.md` | Sasaran CPA/ROAS/CTR/CPM pasaran MY |
| `04-tracking.md` | Pixel, CAPI, UTM, attribution window |
| `05-account-health.md` | Rejection, appeal, akaun kena restrict |
| `06-seasonality-my.md` | Kalendar belanja MY (gaji, Raya, 11.11) |
| `07-post-mortem.md` | Template "apa jadi → kenapa → counter" |

## Status

> 🚧 **Scaffold.** Setiap fail ada struktur kosong. Ilmu masuk **sikit demi sikit** — bila Fazir report, bila office push, bila sheet dikemas kini.
