# Raw Data Policy

Raw source datasets are generally **not committed** to this public repository when they are large, duplicative, license-restricted, or reproducibly downloadable from an authoritative source.

For each raw input used by the Lab:

1. Preserve the original file locally without modifying or renaming it until it has been inventoried.
2. Add one row to `data/manifest.csv` with source, URL, access date, geography/vintage, format, terms, checksum, and planned use.
3. Prefer primary-source downloads from the U.S. Census Bureau, Louisiana Legislature, and Louisiana Secretary of State when equivalent official data is available.
4. Treat Redistricting Data Hub, L2, and other transformed datasets as separately sourced layers with their own terms and methodological notes.
5. Commit compact processed derivatives only after their generating script, QA status, and publication rights are documented.

Shapefiles must be treated as complete bundles (`.shp`, `.dbf`, `.shx`, `.prj`, and `.cpg` where provided); a standalone `.shp` file is not a complete dataset.

Analysis by Tia Fields / Provisional Consulting LLC. Licensed under CC BY 4.0 unless otherwise stated. Third-party datasets retain their own terms.
