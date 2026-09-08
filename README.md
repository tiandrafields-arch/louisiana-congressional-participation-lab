# Louisiana Congressional Representation & Participation Lab

**Independent civic-data and spatial analysis by Tia Fields / Provisional Consulting LLC**

The **Louisiana Congressional Representation & Participation Lab** is a reproducible public-interest research project designed to study how congressional geography, demographic representation, voter registration, and historical election participation interact across Louisiana.

This repository is a standalone project. It builds on geographic and methodological lessons from the [Louisiana Redistricting Equity Dashboard](https://github.com/tiandrafields-arch/redistricting-dashboard---LA) but does not automatically inherit that dashboard's findings, outputs, legal framing, or data assumptions. Any imported result must be reproduced and documented in this repository before it is presented as a Lab finding.

## Research Questions

The Lab is being designed to answer questions such as:

- How did congressional boundary changes redistribute population, voting-age population, and historically participating electorates?
- How has voter participation changed across Louisiana congressional districts, parishes, precincts, and VTDs over time?
- How do registration and actual turnout differ across comparable elections?
- What was the historical participation profile of territory removed from, retained in, or added to a congressional district?
- How uncertain are turnout estimates when geography, precinct vintages, and election environments change?
- Which analytical results are exact, reconciled, allocated, modeled, or unresolved?

## Core Analytical Layers

The project keeps these layers separate and explicitly labeled:

1. **Census 2020 PL 94-171 + validated geography** — population and voting-age population analysis.
2. **Congressional district geometry** — legal district boundaries, with map version, statute/source, and effective date documented before being described as current.
3. **VTD / precinct / block crosswalks** — reproducible geographic reconciliation across vintages.
4. **Louisiana Secretary of State election and registration data** — official election-participation and registration context when available at compatible geography.
5. **Redistricting Data Hub and other transformed datasets** — secondary or derived research layers, with source-specific terms, methods, and limitations documented.
6. **Turnout modeling** — future phase only; forecasts will not be published until the model is back-tested and uncertainty is reported.

## Metric Separation

The Lab does **not** combine Census VAP, voter registration, turnout, partisan preference, or election outcomes into a single denominator or composite score.

Where REI is used:

> **REI = District Black VAP percentage − statewide Black VAP percentage**

REI is a descriptive demographic equity metric. It is not proof of discrimination, vote dilution, racial gerrymandering, discriminatory intent, or legal liability.

Standard turnout will be defined from election records using an election-appropriate denominator, ordinarily ballots cast divided by registered voters for that election. Census VAP and CVAP will remain separately labeled demographic context.

## Initial Development Phases

### Phase 1 — Foundation & Geography

- establish repository structure and data-source manifest;
- document licensing, lineage, and source restrictions;
- define one canonical 2020 Census block geography;
- reconcile Census blocks, validated VTDs, historical precincts, 2026 precinct geography, and congressional districts;
- report match rates, split units, geometry repairs, CRS, and unresolved units.

### Phase 2 — Historical Participation

- standardize historical Louisiana election results;
- preserve official control totals;
- aggregate comparable elections to common geography;
- publish turnout and participation-history tables with explicit denominators.

### Phase 3 — Boundary × Participation

- analyze removed / retained / added territory;
- compare historical participation characteristics without inferring race-based voting behavior;
- publish data-confidence classifications for every geography assignment.

### Phase 4 — Turnout Forecasting

- build transparent turnout models;
- back-test on elections withheld from model training;
- publish error metrics and prediction intervals;
- do not publish candidate- or party-winner predictions as part of the initial Lab scope.

## Data Governance

Large raw public datasets will not automatically be committed to this repository. The project will prefer:

- direct primary-source links;
- source manifests with access date, vintage, checksum, and license/terms status;
- compact machine-readable derivatives;
- reproducible scripts that generate processed outputs;
- source-specific attribution rather than relicensing third-party data under this repository's license.

Underlying third-party datasets retain their own licensing and terms. Redistricting Data Hub-derived data will be documented separately and will not be represented as CC BY 4.0 source data unless its terms expressly allow that treatment.

## Data Status

**Current status: foundation stage.** No turnout forecast or new substantive Lab finding has been published yet.

## Attribution

Copyright © 2026 Tia Fields, Provisional Consulting LLC.

Unless otherwise stated: **Analysis by Tia Fields / Provisional Consulting LLC. Licensed under CC BY 4.0.**

Third-party source data is not automatically relicensed under CC BY 4.0.

## Public-Interest Disclaimer

This dashboard provides independent descriptive spatial analysis using public data. It is not legal advice, an official government product, expert testimony, or a legal determination. Litigation, election administration, statutes, and district boundaries may change; users should verify current primary sources before relying on time-sensitive information.
