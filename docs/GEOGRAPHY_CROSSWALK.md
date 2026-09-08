# Geography Crosswalk Methodology

The Lab will use a common geographic spine so that demographic, registration, and election-participation data can be compared without silently mixing incompatible precinct or district vintages.

## Target geography spine

1. 2020 Census blocks as the canonical base geography.
2. Louisiana Legislature-validated 2020 VTD/block equivalency as the documented redistricting geography layer.
3. Historical election precinct boundaries, each preserved with its election-specific vintage.
4. 2026 precinct geography used by the enacted congressional plan, after primary-source verification.
5. Congressional district assignments generated from exact or documented block/precinct relationships.

## Required QA for every crosswalk

Report:

- source geography and target geography;
- source and target vintage;
- CRS for every geospatial input;
- feature counts before and after processing;
- geometry validity and any repairs;
- exact matches;
- split units;
- unmatched units;
- allocation method, if any;
- population or registration represented by unmatched/split units;
- control-total comparison;
- generating script and output path.

## Confidence status

Each reconciled record should receive one of these statuses:

- `exact` — deterministic identifier or exact containment relationship;
- `reconciled` — documented spatial or equivalency-based match with validation;
- `split` — source unit crosses target boundaries;
- `allocated` — values distributed across targets by a documented weighting method;
- `geometry_repaired` — source geometry required repair before assignment;
- `unresolved` — cannot be assigned without unsupported assumptions.

No unresolved record should be silently assigned to a district.

## Split-unit policy

Where a historical precinct or VTD crosses a target congressional boundary, the Lab will not assign the entire unit by majority area or centroid unless that treatment is explicitly appropriate for the research question and disclosed. Prefer block-level allocation or an official block-equivalency relationship when available.

## Current publication status

No canonical crosswalk has yet been declared complete in this repository. Historical election results, turnout, registration, and demographic measures should not be aggregated to current congressional districts until the geography QA pipeline passes.

Analysis by Tia Fields / Provisional Consulting LLC. Licensed under CC BY 4.0 unless otherwise stated.
