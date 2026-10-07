# InstaFlow — Architecture Overview

## System Design

```
                    ┌─────────────────┐
                    │  InstaFlow       │
                    │  Dashboard       │
                    │  (Next.js/Vercel)│
                    └────────┬────────┘
                             │ HTTPS
                    ┌────────▼────────┐
                    │  InstaFlow       │
                    │  Engine          │
                    │  (FastAPI/DO)    │
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
   ┌──────▼──────┐  ┌────────▼──────┐  ┌───────▼──────┐
   │  PostgreSQL  │  │  Cloudflare   │  │  Google       │
   │  (Railway)   │  │  R2 Storage   │  │  Gemini AI    │
   └─────────────┘  └───────────────┘  └──────────────┘
```

## Distribution Pipeline

1. **Ingest** — Brand uploads reel via dashboard → stored in Cloudflare R2
2. **Process** — Engine downloads once, creates N unique variants via FFmpeg
3. **Caption** — Gemini generates N unique Hinglish captions in parallel
4. **Distribute** — Batch posting with human-like timing per account
5. **Track** — Metrics captured at post time + daily refresh via analytics bot

## Account Identity

Each account has three unique identifiers:
- Dedicated Indian residential IP (Mumbai)
- Unique Android device fingerprint
- DNA-based behavior archetype (10 archetypes, deterministic per account)

## Warmup System

16 human-like activities run daily per account:
scroll feed, watch reels, view stories, like posts, follow accounts,
browse explore, search hashtags, save posts, read comments, and more.

Each account's daily session is unique — different activity count,
different order, different timing — seeded from account ID + date.
