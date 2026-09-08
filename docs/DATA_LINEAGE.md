# Data Lineage

This document records how every public metric in the Louisiana Congressional Representation & Participation Lab is produced.

## Required lineage fields

Every dataset used by the Lab should record:

- source and publisher;
- direct source URL;
- access date;
- reporting period;
- geographic vintage;
- variables used;
- race definition, when relevant;
- geography and CRS;
- whether the source is official, transformed, modeled, or supplemental;
- transformation method;
- validation and control totals;
- limitations;
- generating script or repository file;
- checksum for archived raw inputs when retained locally.

## Layer separation

### Census demographic layer
Use Census 2020 PL 94-171 and validated Louisiana redistricting geography for population and Black voting-age population analysis. Black VAP must be labeled as either Black alone or Black alone/in combination (Any Part Black). These definitions are not interchangeable.

### Congressional district geometry
Use the exact enacted/operative congressional boundary source only after verifying map version, statute or official source, and effective date. Do not describe a district file as current without current primary-source verification.

### VTD / precinct / block assignment
All geographic reconciliation must be reproducible. Record CRS, geometry validity/repairs, match rate, unmatched units, split-unit treatment, allocation method, and validation controls.

### Registration and election participation
Louisiana Secretary of State registration and election data must remain separate from Census VAP. Registration must not substitute for VAP, and turnout must use an election-appropriate denominator rather than Census VAP.

### Redistricting Data Hub and other transformed data
Derived or disaggregated datasets must retain source-specific attribution, methods, and terms. Official election results should remain the control source where available.

## Metric rules

**REI = District Black VAP percentage − statewide Black VAP percentage.**

REI is descriptive only. It is not evidence by itself of discriminatory intent, vote dilution, racial gerrymandering, or legal liability.

Turnout measures must identify numerator and denominator explicitly. A standard turnout rate should ordinarily be ballots cast divided by registered voters eligible for that election. Any CVAP-based participation measure must be labeled separately and not called standard turnout.

## Publication gate

No metric should appear in the public dashboard unless its source, geography, denominator, processing script, and QA status can be traced through this document and `data/manifest.csv`.

Analysis by Tia Fields / Provisional Consulting LLC. Licensed under CC BY 4.0 unless otherwise stated. Third-party data retains its own terms.
