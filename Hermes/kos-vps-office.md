---
type: cost-breakdown
date: 2026-10-03
status: menunggu-keputusan
tags: [kos, vps, office, bajet, deployment]
rate: "1 USD ≈ RM4.07 (Okt 2026)"
---

# 💰 Kos VPS Ke-2 (Agent Office)

**Keputusan:** VPS berasingan untuk agent office (pengasingan mesin sebenar, 24/7, RAM sendiri).
**Sebab dicadangkan:** kekalkan Hermex (499MB) → VPS sedia ada hanya ada 431MB available.

---

## Beban sebenar agent office (TANPA webui)

```
Hermes gateway        ~110–270 MB
OS + Python deps      ~400 MB
Cron spike            ~100–200 MB
─────────────────────────────────
Total                 ~700 MB – 1 GB
```

Jauh lebih ringan dari VPS sedia ada sebab **takde webui** (jimat 499MB) dan **takde `hermes serve`** (81MB).

---

## Pilihan VPS (harga Okt 2026)

| Provider | Spec | USD/bln | **RM/bln** | SG DC? |
|---|---|---|---|---|
| **Hetzner CX23** | 2 vCPU / 4GB / 40GB | €5.99 | **≈ RM28** | ❌ EU |
| **DigitalOcean** | 1 vCPU / 2GB / 50GB | $12 | **≈ RM49** | ✅ sgp1 |
| Vultr | 1 vCPU / 2GB NVMe | $12 | ≈ RM49 | ✅ |
| **DigitalOcean** | 2 vCPU / 4GB / 80GB | $24 | **≈ RM98** | ✅ sgp1 |
| Contabo | 4 vCPU / 8GB | €5.24* | ≈ RM25 | ✅ Asia |

*Kontrak 24 bulan · support lambat (24–48 jam)

---

## Kos penuh

| Item | Kos | Nota |
|---|---|---|
| VPS (DO SG 2GB) | **RM49/bln** | |
| Backup opsyenal | +RM10 | 20% — boleh skip |
| Meta Marketing API | **RM0** | Percuma, takde kos per-call |
| Bot Telegram | **RM0** | Percuma |
| Tailscale | **RM0** | Plan Personal |
| GitHub repo | **RM0** | Percuma |
| Domain | **RM0** | Tak perlu |
| Setup | **RM0** | Hermes buat |

**Jumlah: RM28 (Hetzner) – RM98 (DO 4GB) sebulan.**

---

## 🎁 Sebelum bayar — minta kredit DO

> DigitalOcean landing page cakap "$200 free trial" tapi daftar biasa cuma dapat **$5**.
> **TAPI:** buka tiket support, minta kredit trial $200 — dia bagi. Berjaya setakat Jun 2026.
> **$200 ≈ 8 bulan VPS 2GB percuma.**

---

## ⚖️ Kenapa VPS ke-2 vs profil atas VPS sedia ada

| | Profil atas VPS sedia ada | VPS ke-2 |
|---|---|---|
| Kos | RM0 | RM28–49/bln |
| Pengasingan | Folder + user | **Mesin berasingan** |
| RAM | Guna 431MB sedia ada ⚠️ | RAM sendiri |
| Kalau VPS mati | Dua-dua agent mati | Office tetap hidup |
| Hermex | Kekal | Kekal (tak bersaing RAM) |

Keputusan: **VPS ke-2** — sebab Hermex dikekalkan, jadi RAM sedia ada ketat.

---

## Apa agent office ni akan buat

| Kerja | Bila |
|---|---|
| Ads monitoring (Meta API, read-only) | Cron 24/7 |
| Uptime website | Cron |
| Payment/stock watchdog | Cron |
| Laporan harian → Telegram | Cron |
| Knowledge base office | Sentiasa |
| Kerja berat (creative, analisis) | Bila diminta |

Bot: **@FazirOffice_bot** (token SENDIRI)
Vault: `office-vault` → repo `office-brain` (BERASINGAN dari `fazir-vault`)

---

## Belum selesai

- [ ] Pilih provider
- [ ] Minta kredit $200 DO (kalau pilih DO)
- [ ] Provision VPS
- [ ] Install Hermes + swap + hardening
- [ ] Bot Telegram sendiri
- [ ] Sambung Meta token (read-only)
- [ ] Cron monitoring
- [ ] Tailscale (untuk hub pull)
