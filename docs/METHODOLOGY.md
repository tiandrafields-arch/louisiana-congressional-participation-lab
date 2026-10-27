# Research methodology and source register

## Unit of analysis

Maintain distinct layers for registration, voting age population, voting eligible population, VTD or precinct boundaries, early ballots and certified turnout. Do not divide early voting totals by voting age population and call that an official turnout rate.

## October 1, 2026 baseline

Source: Louisiana Secretary of State registration workbooks `2026_1001_sta_comb.xls` and `2026_1001_par_comb.xls`, status Both. Statewide registration 2,978,143. Black registration 933,052. The six district rows sum to the statewide control.

See the companion [public dashboard](https://tiandrafields-arch.github.io/redistricting-dashboard---LA/) and its processed data and source notes.

## Congressional geography

Use the legislature's [Congress Act 2](https://redist.legis.la.gov/2026_Files/2026CONGRESSACT2) plan. Store plan name, enacted date, source file checksum, CRS, crosswalk build steps, and effective election date for every geography derived from it. Never transfer old district values without documented geographic harmonization.

## Future voting datasets

Store raw public aggregate source, retrieval date, publication timestamp, reporting coverage period, unit of geography, stage (preliminary or certified), explanatory footnotes and SHA256. Statewide and parish numbers must reconcile before publication. Do not treat cumulative report differences as daily votes if reports differ in inclusion rules.

## Polling and scenarios

Survey polling data requires pollster, field dates, sampling frame, sample size, weighting, question wording and methodological limitations. Registration and early voting data are administrative observations, not public opinion polls. The illustrative slider is arithmetic scenario analysis, not candidate or party forecasting.

## Privacy

Only publish aggregate public records. Do not place voter files, walk lists, phone lists, names, individual addresses or other constituent identifiers into this public repository. Restrict any person level voter data to a separate access controlled storage location.

## Reproducibility

Run `python scripts/validate_registration.py` before publishing modified registration data. Historical crosswalks and performance metrics will be added once verified inputs exist.

## Litigation timeline verification

The litigation interface loads `data/congressional_map_litigation.json`. Events represent selected documentary milestones, not all pleadings or ongoing proceedings. Each entry includes an event date, case, map version, event type, explanatory effect, and source identifiers. Each source includes a verification date. The global `last_verified` value describes this compiled dataset and does not establish a current docket status.

**Map version rule:** 2024 Act 2 (SB8) and 2026 Act 2 (SB121) are separate plans and must never be collapsed by act number alone. The April 29, 2026 Supreme Court opinion concerns the 2024 plan. Do not apply its holding to the later enacted 2026 plan without a distinct court order.

**Legal interpretation:** Distinguish litigant allegations, preliminary orders, stays, appellate decisions, enactments, and operative election administration instructions. A new map does not by itself invalidate prior election results or automatically terminate sitting members' terms. Document any remedy using the actual court order and effective election cycle.

**Validation:** Run `python scripts/validate_litigation.py` to check referential integrity, date formatting, and source links. The data file is a curated static record and requires fresh docket checks before any assertion of current litigation status.
