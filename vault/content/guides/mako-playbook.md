# Mako Playbook — What They Do, How We Replicate

## Core Features Breakdown

| Mako Feature | How It Works | Our Replication |
|-------------|--------------|-----------------|
| **Paste Link → Brand DNA** | Extract product, voice, brand visuals from URL | Manual: paste URL → aku analyse → simpan dalam vault |
| **10K+ Signals Research** | Scan Reddit, TikTok, Amazon, Trustpilot, YouTube, X | Trend cron + web_search + web_extract |
| **Mako Swipe** | Clone competitor top ads, remix 60/40 | Competitor research cron → vault → staff generate variants |
| **AI UGC Generation** | Script, film, edit UGC-style videos | Scriptwriter staff → ComfyUI video gen (Wan) |
| **Static Ads** | Image ads for Meta, TikTok | Designer profile + image_gen tool |
| **Wall-of-Text Reels** | Text-heavy viral content | Scriptwriter staff generate hooks |
| **Distribution Engine** | Post organic → pick winners → boost as ads | Manual: cron report suggest winners → kau decide |
| **Ask Mako (AI CMO)** | Trained on your buyer, product, winners | Aku (Hermes) + vault + memory |
| **Multi-brand** | Unlimited brand workspaces | ~/notes/vault/content/campaigns/ per brand |

## Key Insights to Steal

1. **60% remix / 40% original** — clone competitor, twist with your angle
2. **Only boost organic winners** — let algorithm pick, then scale
3. **Wall-of-text reels** — apparently algorithm loves "weird" text-first content
4. **Signal sources** — Reddit + Trustpilot + TikTok comments = goldmine
5. **Time-to-live under 10 min** — speed over perfection

## Our Advantage Over Mako

- Full funnel analysis (not just creative)
- Malaysia market (BM/English, COD, local triggers)
- Deep strategy partner (Claude Console + aku)
- Custom automation (not limited by their platform)
