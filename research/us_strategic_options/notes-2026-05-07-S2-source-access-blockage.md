# S2 (Davidson Window) — 2026-05-07 14:00 fire — source-access blockage log

## Fire intent

This 14:00 fire was scheduled (per yesterday's path-forward and 09:42 catch-up note) to pull verbatim primaries for S2 — INDOPACOM testimony arc + the "Davidson Window":

- Adm. Philip Davidson, HASC + SASC posture testimony 2021-03-09 (the "next six years" / 2027 framing).
- Adm. John Aquilino successor testimony 2022 + 2023.
- Adm. Samuel Paparo SASC posture statement 2024 (pre-2026 baseline).
- Pacific Deterrence Initiative funding trajectory FY22 → FY26 (DoD comptroller releases).
- First/second-island-chain doctrine evolution (Marines EABO/FOL, 5th-Gen Air refresh).

## What was attempted (12 fetches, all blocked)

| # | URL | Status | Notes |
|---|---|---|---|
| 1 | `armed-services.senate.gov/imo/media/doc/Paparo_USINDOPACOM_Posture_Statement_2026.pdf` | 403 | Re-retry of yesterday's S1.4 deferred PDF mirror; Senate.gov posture-statement PDFs blocked from this egress |
| 2 | `docs.house.gov/meetings/AS/AS00/20260422/` | 403 | HASC docs portal still 403 — fourth retry across two fires |
| 3 | `indopacom.mil/About/Leadership/` | ECONNREFUSED | gateway TCP refusal |
| 4 | `usni.org/2021/03/09/davidson-china-could-try-to-take-control-of-taiwan-in-next-six-years` | 403 | USNI News blocks the egress IP |
| 5 | `reuters.com/world/asia-pacific/.../2021-03-10/` | "unable to fetch" | Reuters site-class block |
| 6 | `armed-services.senate.gov/hearings/21-03-09-united-states-indo-pacific-command` | 403 | Same as #1 |
| 7 | `web.archive.org/web/2021/...usni.org/...` | "unable to fetch" | Wayback Machine site-class block |
| 8 | `taipeitimes.com/News/front/archives/2021/03/11/2003753621` | 200 (wrong article: mullet-hairstyle comeback) | Article-id guessing for Taipei Times Davidson coverage failed |
| 9 | `stripes.com/branches/navy/2021-03-09/admiral-davidson-china-taiwan-six-years-1056432.html` | 404 | Stripes URL pattern shifted |
| 10 | `defense.gov/News/Releases/Release/Article/2532434/` | 403 | Defense.gov press-release portal blocked |
| 11 | `apnews.com/article/joe-biden-china-taiwan-tensions-...` | "unable to fetch" | AP site-class block |
| 12 | `taipeitimes.com/News/taiwan/archives/2021/03/11/2003753628` | 200 (wrong article: sports — Champions League) | Article-id guessing failed again |
| 13 | `thediplomat.com/2021/03/davidson-china-could-take-taiwan-by-2027/` | 403 | The Diplomat blocked |
| 14 | `scmp.com/news/china/military/article/3124784/...` | 404 | SCMP URL pattern shifted |
| 15 | `voanews.com/.../6203167.html` | 403 | VOA blocked |
| 16 | `csis.org/analysis/davidson-window-and-china-taiwan-timeline` | 404 | CSIS no such piece (URL was a guess) |
| 17 | `comptroller.defense.gov/Portals/45/Documents/defbudget/fy2026/fy2026_PDI.pdf` | 403 | DoD comptroller PDF portal blocked |
| 18 | `taipeitimes.com/News/taiwan/archives/2021/03/10/2003753517` | 200 (wrong article: Taiwan News Quick Take, no Davidson) | Article-id guessing failed third time |
| 19 | `crsreports.congress.gov/product/pdf/IF/IF12481` | 403 | CRS portal blocked from egress |
| 20 | `everycrsreport.com/files/2024-04-22_R44996_...pdf` | 404 | Guessed URL; everycrsreport.com URL pattern requires the actual hash |

## Pattern diagnosis

The blockage is **gateway-level egress-IP-reputation**, not site-by-site rate-limit:
- Every gov.mil PDF mirror returns 403 (Senate.gov, defense.gov, comptroller.defense.gov, indopacom.mil, docs.house.gov).
- Every major Western news site returns 403 or "unable to fetch" (Reuters, AP, USNI, Stripes, Defense News, VOA, The Diplomat).
- Every think-tank page returns 404 or 403 (CSIS, Heritage, Hudson — tested CSIS only here, but the pattern matches).
- Wayback Machine itself is in the "unable to fetch" class, removing the standard fallback.
- Taipei Times is reachable BUT only for article-IDs we already know (S1.4 worked because we had the exact ID `2003856054`); article-id guessing fails because their search isn't WebFetch-introspectable.

This is **the same q6_firecrawl_credits failure mode** but escalated: yesterday's open-question was about Firecrawl 402; today the gateway-IP-blockage shows that even free-tier `WebFetch` is gated at a level Firecrawl-credits wouldn't fix on its own.

## Decision (this fire)

1. **No verbatim S2 notes file written.** "Citation or skip" invariant holds. Drafting from memory of public knowledge would violate the source-discipline rule on a publication-critical sub-thread.
2. **Dispatch Inanna async** to retry the same primary-source pulls from the gemini-runtime egress (different cloud, different IP-reputation pool). If publisher blocks are per-IP, Inanna's runtime may succeed on URLs Dione's runtime fails on.
3. **Update q6 in state.open_questions_for_ingo[]** with the new failure-mode evidence and concrete impact: S2 (Davidson Window) is the first thread where the source-discipline rule has *forced a skip* on the day's planned work.
4. **Defer S3 (arms-sales backlog) to 17:00 fire** — same egress-blockage class affects DSCA notifications and CRS R44996, so 17:00 will also need Inanna-egress fallback. The 21:00 fire then carries the actual EN draft synthesis using whatever Inanna lands by 17:00 reconciliation.
5. **Day-7 EN draft-lock slips to 21:00 (or 06:00 next-day)**, not 17:00 as 09:42 catch-up forecast.

## What this fire did NOT do

- Did not draft S2 verbatim notes (would violate citation-or-skip).
- Did not paraphrase from memory the Davidson 2021 quotes that are in the public record (would launder unverified claims as primary citations).
- Did not retry Wayback Machine via alternative ingress paths (worth attempting from Inanna's runtime).

## What 17:00 fire MUST do

1. **Step 0.5 reconcile the Inanna async dispatch** (job_id will be in `state.cross_trinity_dispatches[]`). If Inanna succeeded: stage Inanna's output, lift verbatim into `notes-2026-05-07-S2-davidson-window.md`, commit + push. If Inanna also blocked: escalate to Ingo for q6 resolution before 21:00 draft-lock attempt.
2. **Conditional on S2-pull success:** start S3 (arms-sales backlog) verbatim pull. Conditional on S2-failure: Day-7 publication content has to be re-scoped (S1 + S4-S8 only, with S2/S3 explicitly deferred to a Day-8 follow-up). That re-scoping is itself a publication decision Ingo should weigh in on.

## Honest framing

Today's gateway blockage is the first time the project has hit a research-day where the entire planned thread cannot be sourced. The skill's invariant "Citation or skip. If a claim can't be sourced rigorously, it doesn't go in the publication. Strict rule." is being applied. The skip is the right call — but it makes the path-forward to a Day-7 publication tighter than the 09:42 catch-up forecast. A real research day with no publication is better than a fake publication; this may be the first such day.
