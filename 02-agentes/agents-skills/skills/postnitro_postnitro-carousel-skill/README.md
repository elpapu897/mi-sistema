# PostNitro Carousel Generator — Agent Skill

Generate professional social media carousel posts using the [PostNitro.ai](https://postnitro.ai) Embed API. Works with Claude Code, OpenClaw, and any agent that supports the [AgentSkills](https://github.com/vercel-labs/skills) open standard.

## What It Does

This skill lets AI agents create carousel posts for LinkedIn, Instagram, TikTok, and X (Twitter) through two workflows:

- **AI Generation** — provide a topic, article URL, or X post and let PostNitro's AI create the entire carousel
- **Content Import** — provide your own slide content with headings, descriptions, images, and infographic layouts

The agent handles the full async flow: initiate → poll status → download output (PNG images or PDF).

## Install

### Claude Code

```bash
# Project-level
cp -r postnitro-carousel/ .claude/skills/

# Global
cp -r postnitro-carousel/ ~/.claude/skills/
```

### OpenClaw / ClawHub

```bash
clawhub install postnitro-carousel
```

Or paste this repo URL directly into your agent's chat — it will handle setup automatically.

### Other Agents

Copy the `postnitro-carousel/` folder into your agent's skills directory. See the [skills CLI](https://github.com/vercel-labs/skills) for supported agents and paths.

## Setup

1. Sign up at [postnitro.ai](https://postnitro.ai) (free plan: 5 credits/month, no credit card required)
2. Go to account settings → **Embed** → generate an API key
3. Set up a template, brand, and AI preset in the PostNitro dashboard
4. Set your environment variables:

```bash
export POSTNITRO_API_KEY="your-api-key"
export POSTNITRO_TEMPLATE_ID="your-template-id"
export POSTNITRO_BRAND_ID="your-brand-id"
export POSTNITRO_PRESET_ID="your-ai-preset-id"  # only needed for AI generation
```

## Usage Examples

Once installed, just ask your agent naturally:

> "Create a LinkedIn carousel about 5 productivity tips for remote workers"

> "Turn this blog post into a carousel: https://myblog.com/posts/marketing-strategy"

> "Make a carousel from my slides: Title slide saying 'Growth Hacking 101', then 4 tips, then a CTA to follow me"

> "Convert this X thread into a carousel: https://x.com/username/status/123456789"

The agent will pick the right workflow (AI generation or content import), call the PostNitro API, poll for completion, and return download links for your carousel images or PDF.

## What's Inside

```
postnitro-carousel/
├── SKILL.md                           # Agent instructions (core skill file)
├── references/
│   └── api-reference.md               # Complete API docs with request/response schemas
└── examples/
    ├── EXAMPLES.md                    # Index of all examples
    ├── generate-from-text.json        # AI generation from text content
    ├── generate-from-article.json     # AI generation from article URL
    ├── generate-from-x-post.json      # AI generation from X (Twitter) post
    ├── import-default.json            # Basic multi-slide carousel import
    └── import-infographics.json       # Import with grid & cycle infographic layouts
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/post/initiate/generate` | POST | Create carousel with AI (2 credits/slide) |
| `/post/initiate/import` | POST | Create carousel from your content (1 credit/slide) |
| `/post/status/{id}` | GET | Check generation status |
| `/post/output/{id}` | GET | Download finished carousel |

Full endpoint documentation with schemas: [`references/api-reference.md`](postnitro-carousel/references/api-reference.md)

## Credits & Pricing

| Plan | Price | Credits/Month |
|------|-------|---------------|
| Free | $0 | 5 |
| Monthly | From $10 | 250+ (scalable) |

One credit = one slide. AI generation costs 2x.

## Links

- [PostNitro.ai](https://postnitro.ai) — Sign up and manage your account
- [API Documentation](https://postnitro.ai/docs/embed/api) — Official PostNitro API docs
- [Postman Collection](https://www.postman.com/postnitro/postnitro-embed-apis/overview) — Test endpoints in Postman
- [ClawHub Page](https://clawhub.ai/iAmMuneeb/postnitro-carousel) — Install via ClawHub

## Contributing

Found a bug or want to improve the skill? Open an issue or submit a PR. Please test changes against the PostNitro API before submitting.

## License

MIT
