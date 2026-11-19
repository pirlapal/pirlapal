<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/header-mobile-dark.svg?v=matte-ash-gray">
  <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/header-mobile-light.svg?v=matte-ash-gray">
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/header-dark.svg?v=matte-ash-gray">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/header-light.svg?v=matte-ash-gray">
  <img alt="Pranav Kishor Irlapale — software engineering and applied AI. Connecting data and documents through APIs and tools to AI workflows." src="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/header-light.svg?v=matte-ash-gray" width="1200">
</picture>

# Hi, I'm Pranav Kishor Irlapale

**Software engineer focused on GenAI applications, backend systems,
and workflow automation.**

[Email](mailto:irlapalepranav@gmail.com) · [LinkedIn](https://www.linkedin.com/in/pranav-irlapale) · [Selected projects](#selected-projects)

I'm pursuing an MS in Software Engineering at Arizona State University,
with an expected graduation in May 2027.

I build applications that connect AI models, backend services, and
interfaces people can use. My projects include document-review agents,
a recruiter dashboard, and a programming-language interpreter.

My experience also includes reporting dashboards and content-workflow
automation at ASU's AI CIC.

## Selected projects

### [PlanAI — AI Agent Swarm Checker](https://github.com/pirlapal/AI-agent-Swarm-checker)

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/planai-mobile-dark.svg?v=matte-ash-gray">
  <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/planai-mobile-light.svg?v=matte-ash-gray">
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/planai-dark.svg?v=matte-ash-gray">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/planai-light.svg?v=matte-ash-gray">
  <img alt="PlanAI architecture: case documents and review rules feed a Python orchestrator with category agents, producing structured findings." src="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/planai-light.svg?v=matte-ash-gray" width="1200">
</picture>

A document-review prototype that lets users define review rules,
attach documents, and follow agent progress and structured findings.

**My role:** Co-creator in a two-person Kiro Spark Challenge team.

**Stack:** Python, TypeScript, Next.js, AWS CDK, Lambda, API Gateway,
DynamoDB, S3, and Bedrock AgentCore.

<details>
<summary>Architecture and running locally</summary>

The project combines a Python agent orchestrator, a Next.js interface,
WebSocket progress updates, and AWS infrastructure for workflow records,
document storage, and model-backed execution.

The interface can be previewed locally. Running document reviews
requires a configured AWS deployment. The README documents the
architecture, setup, and prototype limitations.

</details>

### [Resume Screening Dashboard](https://github.com/pirlapal/Resume-Screening-Dashboard)

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/dashboard-mobile-dark.svg?v=matte-ash-gray">
  <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/dashboard-mobile-light.svg?v=matte-ash-gray">
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/dashboard-dark.svg?v=matte-ash-gray">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/dashboard-light.svg?v=matte-ash-gray">
  <img alt="Dashboard architecture: fictional demo records or optional Google Sheets records pass through FastAPI validation into a Next.js review interface." src="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/dashboard-light.svg?v=matte-ash-gray" width="1200">
</picture>

A recruiter-facing application for browsing candidate evaluations,
filtering applications, inspecting records, and managing review status.

**My role:** Backend Lead on the original team project.

**Stack:** Python, FastAPI, Next.js, TypeScript, and Google Sheets.

<details>
<summary>Public demo and implemented scope</summary>

The public edition includes a FastAPI data adapter, score validation,
reviewer authentication, automated checks, and a local demo with
fictional candidates.

This repository handles the review interface and data integration.
Resume parsing and model-based scoring belong to the broader original
system.

</details>

### [Lumos Language](https://github.com/pirlapal/Lumos-Language)

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/lumos-mobile-dark.svg?v=matte-ash-gray">
  <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/lumos-mobile-light.svg?v=matte-ash-gray">
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/lumos-dark.svg?v=matte-ash-gray">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/lumos-light.svg?v=matte-ash-gray">
  <img alt="Lumos pipeline: source code passes through a lexer, parser, abstract syntax tree, and interpreter." src="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/lumos-light.svg?v=matte-ash-gray" width="1200">
</picture>

An educational programming language implemented in Python, with a
handwritten lexer, parser, abstract syntax tree, and interpreter.

**My contributions:** Loop parsing, parser integration, runtime tests,
documentation, and project coordination.

Lumos supports variables, expressions, conditionals, loops, and block
scopes. The included examples run without external packages.

Developed as a team course project, with individual contributions
documented in the repository.

## Tools I work with

<p>
  <img src="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/badges/python.svg?v=matte-ash-gray" alt="Python" height="28">
  <img src="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/badges/typescript.svg?v=matte-ash-gray" alt="TypeScript" height="28">
  <img src="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/badges/java.svg?v=matte-ash-gray" alt="Java" height="28">
  <img src="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/badges/fastapi.svg?v=matte-ash-gray" alt="FastAPI" height="28">
  <img src="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/badges/nextjs.svg?v=matte-ash-gray" alt="Next.js" height="28">
  <img src="https://raw.githubusercontent.com/pirlapal/pirlapal/main/assets/badges/aws.svg?v=matte-ash-gray" alt="AWS" height="28">
</p>

- **Languages:** Python, TypeScript, Java
- **Backend:** FastAPI, REST APIs, WebSockets
- **Web:** React, Next.js
- **AI and cloud:** AWS Bedrock AgentCore, Lambda, API Gateway,
  DynamoDB, S3, and CDK
- **Engineering:** Automated testing, API data contracts,
  technical documentation

## Current focus

My focus is backend and GenAI application engineering: connecting
models to data and tools, orchestrating workflows, and making results
clear to the people using them.

My recent public work includes preparing standalone project editions
with runnable examples, tests, clearer setup instructions, and
documented team contributions.

## Opportunities

I'm interested in software engineering and applied AI roles, including
**GenAI Engineer** and **Forward Deployed Engineer** positions.

I'm especially interested in work that combines hands-on development,
working closely with users, and integrating AI into existing workflows.

## Let's connect

- [Email](mailto:irlapalepranav@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/pranav-irlapale)

If you're hiring, I'd be happy to walk through a project, explain my
contribution, and discuss the engineering decisions behind it.
