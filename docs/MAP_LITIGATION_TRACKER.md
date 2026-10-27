# Congressional map litigation and representation tracker

Last research framework update: October 27, 2026.

## Purpose
Track legal status and map versions separately from election results. A new map does not automatically invalidate the term of a representative previously elected under an earlier map. Do not treat pending litigation as a court ruling.

## Verified baseline
* Louisiana Legislature lists Congress Act 2 (SB121) as the 2026 enacted congressional plan: https://redist.legis.la.gov/2026_Files/2026CONGRESSACT2
* Official SB121 status is signed by governor as Act 2: https://legis.state.la.us/Legis/BillInfo.aspx?i=250004
* The Supreme Court's April 29, 2026 Callais ruling concerned the earlier 2024 plan, not an automatic invalidation of 2026 Act 2.
* A litigation tracker reports remedial proceedings scheduled March 2 and 3, 2027 in the Callais matter: https://www.democracydocket.com/cases/louisiana-congressional-redistricting-challenge-callais/
* Further challenges to the new map are reported by https://redistricting.lls.edu/state/louisiana/ . Verify each case's current docket and disposition before adding a definitive status.

## Required case fields
case_name, docket_number, court, filing_date, challenged_action, map_version, claims, latest_order_date, latest_order_url, procedural_status, relief_requested, effective_election_cycle, next_hearing, last_verified, verification_source.

## Dashboard states
1. Enacted plan currently used for election administration.
2. Challenge pending (only if a live docket confirms).
3. Order entered but stayed or appealed.
4. Order effective changing boundaries or election administration.
5. Superseded plan retained for historical comparison.

## Research design
Keep immutable map version identifiers, shapefile checksums and dates. Link each election to the map actually used. Build a future side by side geographic comparison and population transfer table using verified geographic crosswalks. Never retroactively assign votes from one district map to another without a validated geographic conversion method.

## Editorial standard
Separate court holdings, litigant allegations, legislative actions, commentary and rumors. Every material legal status change needs a dated primary docket or signed order. Explain effects on voters and representation only to the extent established by that order.
