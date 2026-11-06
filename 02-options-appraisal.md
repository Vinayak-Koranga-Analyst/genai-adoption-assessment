# 02. Options Appraisal

> **Practice case study.** Brookvale Homes is fictional; costs and scores are illustrative.

## 1. Options considered

| Option | What it means |
|---|---|
| **A. Improve the current process (no AI)** | Replace free-text email with a structured web form (address, room, type of problem, photos). Advisers still read and sort everything. |
| **B. Rules-based routing** | The structured form plus keyword rules (e.g. "gas", "sparking", "no heating") that move likely emergencies to the top of the queue. No AI. |
| **C. AI suggests, a person decides** | An AI model reads each email and suggests a trade, a priority and missing details. A separate rules layer flags safety keywords. An adviser confirms or changes every suggestion before it goes into the HMS. |
| **D. Full automation** | AI classifies the email and creates the repair order in the HMS with no human check, except for low-confidence cases. |

## 2. Evaluation criteria

Weights were agreed with the sponsor and the head of the contact centre. Safety carries the most weight because a missed emergency is the most serious outcome.

| Criterion | Weight | What a high score means |
|---|---|---|
| Safety | 30% | Emergencies are found quickly and reliably; failures are caught by a person |
| Time saved | 20% | Less adviser time per email and less waiting |
| Accuracy and consistency | 15% | Fewer wrong trades or priorities |
| Cost | 15% | Low set-up and running cost |
| Data protection risk | 10% | Less personal data processed, fewer new processors |
| Deliverability | 10% | Can be delivered with current systems, skills and suppliers |

## 3. Scoring (1 = poor, 5 = strong)

| Criterion | Weight | A | B | C | D |
|---|---|---|---|---|---|
| Safety | 30% | 1 | 3 | 5 | 2 |
| Time saved | 20% | 1 | 2 | 4 | 5 |
| Accuracy and consistency | 15% | 1 | 2 | 4 | 3 |
| Cost | 15% | 5 | 4 | 3 | 3 |
| Data protection risk | 10% | 5 | 5 | 3 | 2 |
| Deliverability | 10% | 5 | 4 | 3 | 2 |
| **Weighted score** | | **2.40** | **3.10** | **3.95** | **2.90** |

**Why D scores low on safety:** without a person checking, a misread emergency (e.g. "there's a funny smell near the boiler") could be logged as routine. Even a 1% miss rate on ~80 emergency emails a month means about nine missed emergencies a year. A rules layer reduces this risk but doesn't remove it.

**Why C beats B:** keyword rules alone catch obvious emergencies but can't suggest the trade or spot missing details, so advisers still do most of the work. Rules also miss emergencies described in plain words ("water coming through the light fitting").

## 4. Costs and benefits (option C, first year, illustrative)

| Item | Estimate |
|---|---|
| Set-up: integration with inbox and HMS, configuration, testing | £20,000 |
| Running: AI service, hosting, support | £18,000 a year |
| DPIA, training, change management | £6,000 |
| **Year 1 cost** | **£44,000** |
| Adviser time saved: 6 → about 2 minutes per email, 2,600 emails a month | ~170 hours a month, about £37,000 a year at £18 an hour |
| Fewer re-worked repair orders (12% → target 5%) | Not costed; reduces contractor call-outs |
| Faster handling of emergencies | Not costed; the main benefit (safety and compliance) |

On adviser time alone, option C pays back in about 14 months. The main reason to do it is safety, not cost.

## 5. Recommendation

**Option C: AI suggests, a person decides**, piloted for 12 weeks before any wider rollout. Option B's structured web form should be delivered alongside it: it improves data quality for both people and the AI, and it doesn't depend on the AI succeeding.
