---
type: decision-record
date: 2026-10-03
status: menunggu-keputusan
tags: [senibina, vps, office, risiko, keputusan]
---

# ⚖️ Keputusan: Pindah Hermes Office ke VPS?

**Cadangan asal:** Bawa Hermes office masuk VPS sebagai profil baru → dapat knowledge + runtime 24/7 + bot Telegram sendiri + cron report + approvals.

**Status:** Analisis siap. **Menunggu keputusan Fazir.**

---

## Ringkasan penemuan

| Aspek | Keadaan sebenar (diukur 2026-10-03) |
|---|---|
| RAM VPS | 1967 MB total, **431 MB available** |
| Swap | 2047 MB (ditambah hari ini) |
| CPU | 1 core, load 0.01 (lapang) |
| Proses terbesar | `hermes-webui` = **499 MB**, up 46 hari |
| iPhone Tailscale | **offline 34 hari** |
| Vault | 4.3 MB |
| Profil `ceo` | 361 MB |
| Hermes VPS | **v0.19.0** (lama — takde `peer`/`sync`) |

---

## 🔴 Tiga risiko besar

### 1. Vault bercampur (tersembunyi)

Profil Hermes atas mesin sama **bukan pengasingan keselamatan** — cuma folder. Agent office boleh baca folder agent personal (satu filesystem).

Kalau dua-dua tulis ke `/home/agent-runner/vault`:
- knowledge office + personal **bercampur**
- vault sync ke repo `fazir-vault`
- agent office boleh **baca semuanya**
- 💥 **PECAH RULE:** office tak boleh tahu kerja personal

**Fix:** vault berasingan + repo berasingan + (lebih baik) Unix user berasingan.

### 2. RAM

- Profil baru ≈ **+90–110 MB** → muat, tapi tipis
- ⚠️ Kalau perlu **browser** → **+300–800 MB** → box mati
- ⚠️ **18 staff dah diprune Okt 2026 SEBAB RAM** — ni langkah ke belakang
- 🎁 **499 MB percuma** kalau `hermes-webui` dimatikan (iPhone offline 34 hari)

### 3. Credential company atas server peribadi

| Soalan | Jawapan |
|---|---|
| Guna laptop office? | ✅ Boleh — takde restriction |
| Pindah token akaun iklan company ke VPS peribadi? | ⚠️ **Soalan LAIN** |

VPS **bukan milik company**. Kalau ada audit / DPA / polisi data → boleh jadi masalah. Kena jadi **keputusan sedar**.

### 4. Blast radius

Satu box pegang: token iklan office (**boleh belanja duit**) + credential personal + vault + 2 bot.
- Kena breach → dua-dua dunia terdedah
- VPS down → dua-dua agent mati

### 5. Versi lama & kerja UI

- VPS v0.19 → upgrade perlu restart gateway 24/7 (downtime)
- Kerja UI (skrin office, browser session, fail tempatan) **tak boleh pindah** — tetap kena Mac

---

## ✅ Jalan keluar: pindah KERJA, bukan AGEN

| Keperluan | Perlu pindah agent? |
|---|---|
| Monitor ads 24/7 | ❌ VPS panggil API terus |
| Uptime + payment watchdog | ❌ Script biasa |
| Cron report Telegram | ❌ CEO bot dah ada |
| Approvals | ❌ |
| Knowledge | ❌ Git repo |
| Kerja UI office | 🚫 Tak boleh pun |

**Hasil:** VPS dapat **3 cron job + 1 bot**. Takde profil baru.

---

## Dua keputusan berasingan

| # | Keputusan | Saiz | Perlu? |
|---|---|---|---|
| 1 | Pindah **token** (read-only) ke VPS | Kecil | ✅ Ini yang bagi 24/7 |
| 2 | Pindah **agent** (profil baru) | Besar | 🟡 Selalunya tak perlu |

---

## Syarat kalau nak buat juga

1. **Vault berasingan** — `office-vault` ≠ `vault`, repo berasingan
2. **Matikan `hermes-webui`** — bebas 499 MB (kalau tak guna Hermex)
3. **Upgrade VPS** v0.19 → v0.20
4. Fikir serius pasal **credential company atas server peribadi**

---

## Cadangan

> Pindah **KERJA** sahaja. VPS dapat 24/7 tanpa pindah agent, tanpa risiko vault bercampur.
> Token **read-only** sahaja dulu — mata, bukan tangan.
