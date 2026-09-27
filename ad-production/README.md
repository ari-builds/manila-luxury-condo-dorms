# Manila Luxury Condo Dorms — ad production assets

Everything produced for the premium 9:16 social advertisement, plus the working
evidence used to build it. Source clips for the property remain in this repo's
`videos/` folder (the gallery that sits alongside these assets).

## Delivered advertisement

| File | What it is |
|---|---|
| `output/Manila_Luxury_Condo_Dorms.mp4` | Final ad, 9:16, 1080×1920, 24 fps, 26.209 s (no voiceover) |
| `output/Manila_Luxury_Condo_Dorms_Poster.jpg` | Poster frame from the opening |
| `output/titles.ass` | Brand and CTA title track burned into the final cut |

## Reference evidence used for the recreation

| Folder | Contents |
|---|---|
| `keyframes/` | Exact property frames pulled from the source clips (rooms, bathroom, pool, gate views) |
| `review/` | Labelled contact sheets and review reels covering the whole source library |
| `qc/` | Frame sheets and stills captured from generated footage during quality review |

## Generation inputs and outputs

| Folder | Contents |
|---|---|
| `generation_refs/` | Shortened reference excerpts submitted to the video model |
| `social_refs/` | Amenity references (gym, lobby, study hall) and short clips used for the extended cut |
| `generated/` | Generated sections: `part1` (pool → lobby → corridor → studio), `part2` (joinery → bathroom → window), `part3` (campus views and panorama), plus `music.wav` |

## Build scripts

| File | Purpose |
|---|---|
| `assemble.py` | Renders the final ad: trims exact frame ranges, removes the rejected lobby shot, mixes ambience and music, burns titles |
| `build_review.py` | Builds labelled review reels and contact sheets from the source library |
| `review_sources.py` | Downloads and inventories the source library (duration, dimensions, checksums) |
| `qc_frames.py` | Extracts frame sheets from generated sections for inspection |
| `prepare_generation_refs.py`, `prepare_social_refs.py` | Cut the reference excerpts used for generation |
| `production_state.json` | Record of the approved direction and generation ids |
| `source_inventory.json` | Full inventory of every source clip reviewed |

## Notes on the edit

- No people, human shadows, silhouettes or human reflections appear in any interior.
- Bare bunk platforms are the property's real, documented condition — not an omission.
- The lobby shot was excluded because a dark object behind reception could not be
  confirmed as furniture rather than a person, and the brief required completely
  empty interiors.
- Two campus entrance views are included and kept visually distinct.
- Reproduce the final render with `python assemble.py` from this folder.
