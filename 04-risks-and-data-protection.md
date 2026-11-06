# 04. Risks, UK GDPR and DPIA Screening

> **Practice case study.** Brookvale Homes is fictional. This is a BA's assessment to brief the Data Protection Officer, not legal advice.

## 1. Risk register

Likelihood and impact: H / M / L. Risks are scored before and after mitigation.

| ID | Risk | Before | Mitigation | After | Owner |
|---|---|---|---|---|---|
| R-01 | **An emergency is missed or marked routine** (e.g. described in unusual words) | L / H | Safety keyword rules run before and independently of the AI; emergencies flagged by **either** go to the top; adviser reviews every email; weekly sample audit of emails marked routine | L / H (monitored) | Head of Building Safety |
| R-02 | **Advisers accept suggestions without checking** (automation bias) | H / M | Training; low-confidence suggestions clearly marked; monthly audit of override rates (a near-zero override rate is a warning sign, not a success) | M / M | Head of Contact Centre |
| R-03 | **The AI invents details** that aren't in the email (e.g. a room or appliance) | M / M | AI suggests only a category, priority and missing-information list from fixed options; no free-text summaries go into the HMS without adviser edit | L / M | Product owner |
| R-04 | **Worse accuracy for some tenants**, e.g. emails written in other languages, very short emails or non-standard English | M / M | Test accuracy by email length and language in the pilot; route low-confidence emails to advisers without a suggestion; Equality Impact Assessment | L / M | Product owner |
| R-05 | **Personal data leaves the UK/EEA or is used to train the supplier's model** | M / H | Contract terms (UK GDPR Article 28 processor agreement); UK/EEA hosting; no training on Brookvale data; supplier due diligence | L / H | DPO |
| R-06 | **Health or vulnerability details** in emails are processed by a new system | H / M | Treat as special category data in the DPIA; data minimisation (NFR-02); access controls; retention limits | M / M | DPO |
| R-07 | **AI service outage** | M / M | Fall back to the current process automatically; safety rules run locally (BR-09) | L / L | IT lead |
| R-08 | **Accuracy falls over time** as tenants' wording or repair types change | M / M | Monthly accuracy report; retest every quarter on a fresh sample; agreed retraining or reconfiguration trigger | L / M | Product owner |
| R-09 | **Staff worry the AI will replace them** | M / M | Clear message that the adviser makes the decision; time saved goes to calling back vulnerable tenants and chasing overdue repairs | L / L | Director of Property Services |
| R-10 | **Locked in to one supplier** | M / L | Keep the keyword rules and logs in Brookvale's own systems; contract exit terms; prototype shows an open-model alternative | L / L | Procurement |

## 2. UK GDPR assessment

| Topic | Assessment |
|---|---|
| **Personal data involved** | Tenant name, address, contact details, description of the repair, photos. Emails often include health information (e.g. "my son has asthma and the mould is getting worse") and other vulnerability information. |
| **Special category data** | Yes, sometimes (health). Needs an Article 9 condition, to be confirmed by the DPO; likely a substantial public interest condition under the Data Protection Act 2018, Schedule 1. |
| **Lawful basis (Article 6)** | Processing is needed to meet the landlord's legal repair obligations and the tenancy agreement. The DPO to confirm the basis: legal obligation or contract. |
| **Automated decision-making (Article 22)** | Not engaged: no decision with legal or similarly significant effect is made solely by automated means. An adviser makes every decision (BR-05). This must stay true if the design changes. |
| **Transparency** | Update the tenant privacy notice to explain that AI helps sort repair emails and that a person always decides. |
| **Data minimisation** | Only the email content is sent to the AI service; HMS tenant records are not (NFR-02). |
| **Processors and transfers** | The AI supplier is a processor: Article 28 contract, UK/EEA processing, no use of data for model training, sub-processor list reviewed. |
| **Retention** | AI inputs and outputs kept no longer than the related repair record (NFR-03). |
| **Rights requests** | AI suggestions and adviser decisions are logged against the repair, so they can be found for subject access requests. |

## 3. DPIA screening

The ICO's guidance says a DPIA is needed for processing likely to result in a high risk. Screening questions:

| Screening question | Answer |
|---|---|
| Uses new or innovative technology (including AI)? | **Yes** |
| Processes special category data? | **Yes**, sometimes (health) |
| Processes data about vulnerable people? | **Yes**, some tenants |
| Makes solely automated decisions with significant effects? | No (adviser decides) |
| Large-scale processing? | Moderate (~31,000 emails a year) |
| Data matching or combining datasets? | No |

**Outcome: a full DPIA is required before the pilot starts.** The risk register above and the requirements in [03](03-requirements-and-feasibility.md) are inputs to it. The DPO is accountable for the DPIA (see the RACI in the [pilot plan](05-success-measures-and-pilot.md)).

## 4. Other assessments

- **Equality Impact Assessment:** to check that accuracy doesn't differ unfairly between groups of tenants (R-04).
- **Information security review:** of the supplier and of the integration with the inbox and HMS.
