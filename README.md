# Generative AI Adoption Assessment: Repairs Email Triage

> **Practice case study.** Brookvale Homes is a fictional housing association, all figures are illustrative, and the emails in the prototype are synthetic (written for this exercise, with no real tenant data). This repo shows how I would assess an AI tool for a business process. It is not based on client work.

An assessment of whether Brookvale Homes should use AI to sort and prioritise the repair requests that tenants send by email. It covers the current process, the options, feasibility, risks and UK GDPR, how success would be measured, and a pilot plan. A small prototype tests whether the idea works on sample data.

## The business problem

Brookvale Homes manages about 12,000 homes. Tenants report around 2,600 repairs a month by email. Two contact centre staff read each email, decide what kind of repair it is and how urgent it is, and log it in the housing management system.

- Emails wait an average of **1.5 working days** before anyone reads them.
- About **1 in 8** are logged with the wrong trade or priority and have to be redone.
- Urgent issues (gas smells, no heating for vulnerable tenants, electrical hazards, serious damp and mould) sit in the same queue as routine requests. Since Awaab's Law came into force for social landlords in October 2025, missing an emergency hazard is a legal risk as well as a safety one.

## The question

> Can AI read incoming repair emails, suggest the repair category and urgency, and flag emergencies, so that staff confirm rather than start from scratch? And can it do that safely, lawfully and at a cost that makes sense?

## Recommendation (summary)

**Go ahead with a 12-week pilot of option C: AI suggests, a person decides.** The AI suggests a category and urgency for each email, a rules layer catches safety keywords so emergencies are never left to the model, and staff confirm every suggestion before it reaches the repairs system. Full automation (option D) is not recommended: the cost of a missed emergency is too high and the time saved over option C is small.

Proceed only once the DPIA is signed off and the go/no-go measures in the [pilot plan](05-success-measures-and-pilot.md) are agreed.

## What's in the assessment

| # | Document | Status |
|---|---|---|
| 01 | [Current state and problem](01-current-state.md) | Done |
| 02 | Options appraisal | Next |
| 03 | Requirements and feasibility | Next |
| 04 | Risks, UK GDPR and DPIA screening | Next |
| 05 | Success measures and pilot plan | Next |
| – | Prototype notebook | Next |

## Tools

Markdown and Mermaid for the documents; Python and Hugging Face (sentence-transformers) for the prototype.
