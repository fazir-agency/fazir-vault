---
source: LinkedIn (@matthew-feng-615806162) + Instagram (@matthew.feng_)
platform: linkedin + instagram
date: 2026-08-19
tags: [funnels, paid-ads, meta-ads, google-ads, attribution, incrementality, new-customer, segmentation]
link: https://www.linkedin.com/posts/matthew-feng-615806162_increasing-budget-is-where-most-new-meta-activity-7469087813016334336-PJf-
---

# Full Breakdown: Cara Baca Data New vs Existing Customer (Matthew Feng)

## 1. Konsep asas — apa "new vs existing customer" ni

Dalam Meta Ads (dan Google), setiap conversion boleh datang dari 3 jenis orang:

| Jenis | Maksud | Nilai untuk growth |
|-------|--------|--------------------|
| **New customer** | Tak pernah beli/beli pertama kali (cold/prospecting) | 🔴 Growth SEBENAR — inilah yang buat brand membesar |
| **Engaged (warm)** | Dah kenal brand (visit, view, engage), belum beli | 🟡 Mid-funnel |
| **Existing customer** | Dah beli sebelum ni (retargeting/brand search) | 🟢 Senang convert, tapi BUKAN growth |

**Inti masalah:** Data yang Fazir tengok dalam Ads Manager (ROAS, CPA) biasanya **blended** — campur 3 jenis ni jadi satu. Angka nampak bagus, tapi tak bagitahu mana satu yang bawa growth.

## 2. Kenapa ini metrik PALING penting (Matthew rank #1)

Dari reel metrics tier-list: "New vs Engaged vs Existing customer breakdown" = **✅✅ sangat penting** — lebih penting dari ROAS, CPC, semua sekali.

Sebab: ROAS/CPA yang tinggi boleh datang 100% dari existing customer (orang yang dah memang nak beli). Nampak profit, tapi brand tak berkembang.

## 3. Framework penuh Matthew (5 prinsip)

### Prinsip 1 — Jangan percaya blended ROAS/CPA
> "An ad that gets credit isn't always the one bringing NEW customers in — it's often just the last touch before conversion."

Contoh Google (reel DWir30aFLs1): "6x return — orang tu **dah memang nak beli**." Brand search = existing, bukan new acquisition. Orang "lump everything together" dan tak nampak yang 6x tu bukan growth.

### Prinsip 2 — Kenal pasti "winner" palsu
> "At low spend, a lot of things LOOK like they're working... the ads that looked like winners weren't actually driving growth. They were just sitting at the bottom of the funnel."

Ad yang "menang" pada spend rendah selalunya cuma capture existing demand (bottom funnel). Bila scale, sistem kena cari NEW customer → account pecah.

### Prinsip 3 — Scale yang terbukti bawa NEW customer
> "The difference at the top tier is simple: they scale what's proven to bring in new customers. They read the full funnel, understand which creatives are driving intent."

Cara baca betul = tengok creative mana yang drive **new customer** acquisition, bukan yang dapat CPA terendah (sebab CPA rendah = selalunya retargeting).

### Prinsip 4 — Watch out attribution distortion
> "Meta doesn't care about your business. It optimises for what it can measure."

Meta auto-shift spend ke iklan yang "nampak" bagus dalam attribution model dia — iaitu last-touch / bottom-funnel / retargeting. Kesannya: prospecting (new customer) hilang coverage, spend concentrate pada retargeting. "Performance looks strong short-term, but you're slowly cutting off the flow of new customers."

### Prinsip 5 — Fix teknikal (control sendiri)
Matthew bagi 3 fix yang dia sendiri sebut:
1. **Set exclusions** — pastikan retargeting/cost-cap campaign target NEW customer, bukan existing.
2. **Matikan 1-day view** attribution — elak double-count (conversion dikira pada retargeting padahal datang dari prospecting).
3. **Pisahkan campaign** — jangan lump prospecting + retargeting dalam satu campaign (kalau lump, Meta auto-redistribute spend tanpa kawalan Fazir).

## 4. Cara apply (step-by-step — derived dari framework dia)

1. **Buka breakdown** — dalam Ads Manager, jangan tengok ROAS total. Tengok performance breakdown ikut **new vs returning customer** (Meta ada segmentation ni). Kalau Meta tak bagi terus, guna custom conversion / segment server-side.
2. **Kira incrementality** — berapa % revenue datang dari NEW customer? Kalau semua dari existing, brand tak berkembang walaupun ROAS tinggi.
3. **Audit creative** — creative mana yang drive NEW customer (bukan CPA terendah). Ini yang patut dapat budget scale.
4. **Setup exclusions** — pada retargeting/cost-cap campaign, exclude existing customer & purchaser list, supaya duit tak bazir pada orang yang dah beli.
5. **Matikan 1-day view** — guna attribution yang lebih kredible (7-day click / view yang betul).
6. **Pisah struktur** — prospecting campaign (new, broad, exclusion) berasingan dari retargeting campaign (existing, low budget).
7. **Monitor bila scale** — setiap kali naik budget, check sama ada NEW customer % maintain atau jatuh (kalau jatuh = Meta dah shift spend ke retargeting).

## 5. Tanda data menipu (red flags)

- ROAS naik tapi revenue total flat → spend beralih ke retargeting
- CPA rendah tapi takde new customer → semua conversion existing
- "Winner" pada low spend tapi pecah bila scale → ia cuma bottom-funnel capture
- Prospecting coverage mengecut bila budget naik → attribution distortion

## Content asal (verbatim — LinkedIn)
**"Scaling Ad Budget for New Customers"** — "Increasing budget is where most new Meta advertisers get exposed. At lower spend, a lot of things can look like they're working. As soon as you push spend, the system has to find new customers, not just capture existing demand, and that's where most accounts break... The difference at the top tier is simple: they scale what's proven to bring in new customers. They read the full funnel, understand which creatives are driving intent."

**"Meta's attribution model distorts ad spend"** — "Meta doesn't care about your business. It's optimising for what it can measure... An ad that gets credit isn't always the one bringing new customers in. It's often just the last touch before conversion... Spend shifts toward bottom-of-funnel ads, retargeting gets overweighted, and prospecting starts to lose coverage. Performance can look strong for a short period, but you're slowly cutting off the flow of new customers."
