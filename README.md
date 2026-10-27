# Louisiana Congressional Representation and Participation Lab

Independent civic data research by Tia Fields / Provisional Consulting LLC.

This is the research companion to the [Louisiana Congressional Voter & Participation Dashboard](https://tiandrafields-arch.github.io/redistricting-dashboard---LA/). The lab provides a reproducible analytical workspace for October 2026 voter registration, enacted congressional geography, and future historical participation studies.

## Current implementation (October 27, 2026)

* `index.html`: accessible static research interface with district registration explorer and mathematical participation scenario slider.
* `data/registration_2026-10-01.json`: official statewide and district registration controls.
* `scripts/validate_registration.py`: validation of statewide and six district subtotals.
* `docs/METHODOLOGY.md`: geography, sources, comparability, modeling and privacy standards.

The participation slider is illustrative, not a forecast, poll or estimate of candidate support. Final October 27 early voting figures are pending verification and are not included as final data.

## Next research stages

1. Obtain official reporting snapshots, publication dates and documented statewide and parish early voting data.
2. Inventory historical elections with consistent measures, geographic definitions and voting windows.
3. Ingest official Act 2 shapefiles and VTD or precinct geography, tracking boundary changes and geographic crosswalk quality.
4. Publish reproducible aggregate district participation measures only where crosswalks and source geography support them.
5. Validate historical descriptive comparisons and add uncertainty or missingness explanations.

## Local checks

```bash
python scripts/validate_registration.py
python -m http.server 8000
```

Visit `http://localhost:8000` to view the static interface locally.

## Primary sources

* [Louisiana Secretary of State](https://www.sos.la.gov/elections-voting/)
* [Louisiana congressional Act 2 data](https://redist.legis.la.gov/2026_Files/2026CONGRESSACT2)
* [Public voter dashboard](https://tiandrafields-arch.github.io/redistricting-dashboard---LA/)

## Data governance

This is a public repository for aggregate and nonidentifying information only. Do not commit individual voter files, walk lists, phone lists, names, addresses, or contact details. Retain raw source metadata, track reporting status, and distinguish registered voters from votes cast and Census population.

Copyright 2026 Tia Fields / Provisional Consulting LLC. Analysis under CC BY 4.0 unless specified. Third party source terms remain with their original providers.
