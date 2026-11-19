# Profile visuals: source, maintenance, and optional additions

The live profile is [github.com/pirlapal](https://github.com/pirlapal).
The source is [README.md](../README.md). All active images are stored in
this repository. The profile needs no paid service, API key, or image
generation account to render.

The current palette uses deep navy and warm copper in dark mode, with
ivory, ink blue, and soft copper in light mode. Technology badges use navy.

## Included in this update

| Addition | Purpose | Source / exact place to edit |
| --- | --- | --- |
| Custom header | Establishes name and engineering focus at the top | `assets/header-light.svg`, `assets/header-dark.svg` |
| Project diagrams | Makes each project's architecture visible before reading the details | `assets/planai-*.svg`, `assets/dashboard-*.svg`, `assets/lumos-*.svg` |
| Technology badges | Makes the core stack easy to scan | `assets/badges/`, the Tools section in `README.md` |
| Contact navigation | Gives readers a direct next action | Top Email, LinkedIn, and project links in `README.md` |
| Expandable project details | Keeps the initial scan short while preserving technical scope | `<details>` blocks in `README.md` |
| Theme-aware artwork | Supports GitHub light and dark themes | `<picture>` blocks in `README.md` |
| Mobile diagrams | Uses larger labels and vertical flows on screens up to 600px wide | `assets/*-mobile-*.svg` |

The diagrams describe documented architecture. They are diagrams, not
application screenshots. Project roles and prototype limitations remain
in the README.

## Header and project diagrams

The art uses Manrope lettering converted to paths, so it renders without
requiring the visitor to have that font installed. The font and its OFL
license are in `assets/fonts/`. Artwork has accessible descriptions and
no scripts, animation, remote fonts, or live statistics.

To edit and regenerate:

```sh
git clone https://github.com/pirlapal/pirlapal.git
cd pirlapal
python3 -m venv .venv
.venv/bin/python -m pip install fonttools==4.68.0
# Edit labels, colors, or layout in scripts/build_assets.py.
.venv/bin/python scripts/build_assets.py
```

The committed assets make the last command work without network access.
Use `--download` only to refresh the source font and Shields badges.

To embed a themed image, use this exact pattern:

```html
<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/header-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/header-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg">
  <img alt="Pranav Kishor Irlapale — software engineering and applied AI" src="assets/header-light.svg" width="1200">
</picture>
```

GitHub documents this pattern in its
[writing quickstart](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github).
The font source is [Manrope in Google Fonts](https://github.com/google/fonts/tree/main/ofl/manrope).

## Technology badges

Six static, locally stored badges are already installed. They describe
technologies used in the projects. To add another badge, generate it with
[Shields](https://shields.io/badges/static-badge), save it in
`assets/badges/`, and add an image next to the current six.

For example, this is the direct Python badge source:

```markdown
![Python](https://img.shields.io/badge/Python-243a5c?style=flat-square&logo=python&logoColor=white)
```

The live profile uses the committed version:

```html
<img src="assets/badges/python.svg" alt="Python" height="28">
```

## Project showcases and real demo media

The README already links each diagram to a project through its heading.
Keep the problem, your role, the stack, and a runnable example or clear
setup instructions together.

A useful next addition is a real screenshot or a short recording of
PlanAI's local interface or the dashboard's fictional-data demo. Capture
your running application, save a screenshot as `assets/planai-demo.png`,
then add the following under PlanAI. Add the file before adding the image
reference:

```markdown
[![PlanAI local interface preview](assets/planai-demo.png)](https://github.com/pirlapal/AI-agent-Swarm-checker)
```

Use a wide image with readable text, descriptive alt text, and synthetic
example content. A linked recording can also be hosted as a GitHub
attachment or on an existing video account. Link it beside the source
repository; identify whether it shows a local preview or a complete run.

## Pinned repositories

The three showcase projects are the intended pins:

- [AI-agent-Swarm-checker](https://github.com/pirlapal/AI-agent-Swarm-checker)
- [Resume-Screening-Dashboard](https://github.com/pirlapal/Resume-Screening-Dashboard)
- [Lumos-Language](https://github.com/pirlapal/Lumos-Language)

To change them, open [your profile](https://github.com/pirlapal), click
**Customize your pins**, select the repositories, and click **Save pins**.
GitHub permits up to six pinned repositories and gists. See
[GitHub's pinning instructions](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/pinning-items-to-your-profile).

## Contribution graph

GitHub already displays a contribution calendar below the README and
pins. It updates through GitHub and requires no image endpoint or setup.
See [contributions on your profile](https://docs.github.com/en/account-and-profile/concepts/contributions-on-your-profile).

For an additional graph inside the README, paste the following near the
bottom. This optional service visualizes the last 31 days of activity:

```markdown
## Recent activity

[![Pranav's recent GitHub activity](https://github-readme-activity-graph.vercel.app/graph?username=pirlapal&bg_color=101d35&color=f5f0e8&line=e8a06a&point=f1bf97&area=true&hide_border=true)](https://github.com/pirlapal)
```

Source and configuration:
[GitHub Readme Activity Graph](https://github.com/Ashutosh00710/github-readme-activity-graph).
This optional image relies on its public service being available. It is
not enabled in the live README.

## Optional GitHub statistics

These are copy-ready additions, kept optional so the primary profile
renders entirely from this repository's own assets. Add at most one
stats section near the bottom if it contributes useful information.

### Public GitHub activity summary

```markdown
## GitHub activity

[![Pranav's public GitHub statistics](https://github-readme-stats.vercel.app/api?username=pirlapal&show_icons=true&hide_rank=true&hide_border=true&theme=transparent)](https://github.com/pirlapal)
```

### Repository language composition

```markdown
[![Languages used across Pranav's public repositories](https://github-readme-stats.vercel.app/api/top-langs/?username=pirlapal&layout=compact&hide_border=true&theme=transparent)](https://github.com/pirlapal?tab=repositories)
```

The language card summarizes repository language usage. The public stats
instance is best-effort; its maintainers document rate limits and
outages. For reliability, follow their GitHub Actions or self-hosting
instructions and use the resulting image paths. These optional snippets
are not enabled in the live profile.

Source, parameters, and setup:
[GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats).

### Optional contribution streak

```markdown
[![Pranav's GitHub contribution streak](https://streak-stats.demolab.com/?user=pirlapal&theme=transparent&hide_border=true)](https://github.com/pirlapal)
```

This public service also introduces an availability dependency. Use it
only if a streak is something you want to emphasize. Source and
configuration: [GitHub Readme Streak Stats](https://github.com/DenverCoder1/github-readme-streak-stats).

## Verification and maintenance

- Inspect the profile in both GitHub themes after changing assets.
- Check the layout on a narrow screen. Let images scale to their
  container and let technology badges wrap naturally.
- Keep `irlapalepranav@gmail.com` and the LinkedIn destination correct.
- Preserve collaborator credits and distinguish local previews from
  cloud-dependent execution.
- Use a CI-status badge only when the linked workflow actually exists
  and runs. The current technology badges make no test or coverage claim.
