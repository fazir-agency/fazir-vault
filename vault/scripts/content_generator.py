#!/usr/bin/env python3
"""
Content Generator — Flexible Cron Script
Reads content strategy from vault, generates assets via staff profiles.

Usage: python3 content_generator.py [--type copy|script|social] [--campaign NAME]
"""

import json, os, sys, subprocess, glob
from datetime import datetime

CONTENT_DIR = os.path.expanduser("~/notes/vault/content")
CAMPAIGNS_DIR = os.path.join(CONTENT_DIR, "campaigns")
TEMPLATES_DIR = os.path.join(CONTENT_DIR, "templates")

def get_active_campaigns():
    """Read campaign files from vault"""
    campaigns = []
    for f in glob.glob(f"{CAMPAIGNS_DIR}/*.md"):
        name = os.path.splitext(os.path.basename(f))[0]
        campaigns.append({"name": name, "file": f})
    return campaigns

def generate_copy(amount, campaign=None):
    """Use copywriter staff profile to generate ad copy"""
    if not campaign:
        campaign = get_active_campaigns()
        if not campaign:
            print("No active campaigns found. Create one in ~/notes/vault/content/campaigns/")
            return
        campaign = campaign[0]["name"]
    
    prompt = f"""Generate {amount} ad copies for campaign '{campaign}'.
Use templates from {TEMPLATES_DIR}/copy-template.md
Follow brand voice from ~/notes/vault/content/guides/brand-voice.md
Target: Weight loss / supplement, Malaysian market, COD focus
Output format: JSON array of {{headline, body, cta, platform}}"""
    
    result = subprocess.run(
        ["hermes", "--profile", "copywriter", "chat", "-q", prompt, "-Q"],
        capture_output=True, text=True, timeout=120
    )
    return result.stdout

def generate_scripts(amount, campaign=None):
    """Use scriptwriter staff profile to generate video scripts"""
    prompt = f"""Generate {amount} TikTok/Reels scripts.
Platform: TikTok, duration 30-60s
Hook style: problem → solution → CTA
BM+English mix, Malaysia market
Output JSON: [{{hook, problem, solution, cta, duration}}]"""
    
    result = subprocess.run(
        ["hermes", "--profile", "scriptwriter", "chat", "-q", prompt, "-Q"],
        capture_output=True, text=True, timeout=120
    )
    return result.stdout

def generate_social_posts(amount, platform="all"):
    """Use social staff profile to generate social posts"""
    prompt = f"""Generate {amount} social media posts for {platform}.
Brand voice: confident, direct, relatable
Mix BM+English, COD signals, testimonial mentions
Output JSON array"""
    
    result = subprocess.run(
        ["hermes", "--profile", "social", "chat", "-q", prompt, "-Q"],
        capture_output=True, text=True, timeout=120
    )
    return result.stdout

if __name__ == "__main__":
    content_type = sys.argv[1] if len(sys.argv) > 1 else "all"
    amount = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    campaign = sys.argv[3] if len(sys.argv) > 3 else None
    
    output = {"generated_at": datetime.now().isoformat(), "type": content_type, "items": []}
    
    if content_type in ("copy", "all"):
        output["copy"] = generate_copy(amount, campaign)
    if content_type in ("script", "all"):
        output["scripts"] = generate_scripts(amount, campaign)
    if content_type in ("social", "all"):
        output["social_posts"] = generate_social_posts(amount)
    
    print(json.dumps(output, indent=2))
