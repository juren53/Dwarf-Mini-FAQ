# Changelog - Dwarf Mini Smart Telescope FAQ

All notable changes to this FAQ will be documented in this file.

> **Note for maintainers:** Every entry header **must** include a date, a 4-digit 24-hour time, and the `CST` timezone label.
> Correct format: `## YYYY-MM-DD HHMM CST`
> Example: `## 2026-03-23 1430 CST`

---

## 2026-03-24 1600 CST

### Added
- **Q: What is Alt-Az mode?** — explains altitude-azimuth mount, field rotation limitation, and when to use it vs EQ mode (Section 2)
- **Q: What is EQ mode?** — covers polar alignment setup, when EQ mode is recommended vs required, 180s max exposure, and Panorama mode requirement (Section 2)

### Changed
- **Milky Way section** — added EQ mode recommendation, noting it is required for exposures 30s+, and that Panorama mode requires EQ mode (Section 7)

---

## 2026-03-24 1500 CST

### Added
- **Q: How do I image the Milky Way?** — covers best season, where to point, recommended gain/exposure settings, dark sky requirements, tracking, dew, and Panorama mode tip (Section 7)

---

## 2026-03-24 1400 CST

### Added
- **Q: What is Sky Finder?** — explains the wide-angle target discovery feature, step-by-step usage, and notes it was added in V3.3.8 / V1.4.15.2 (February 2026) (Section 8)

---

## 2026-03-24 1300 CST

### Added
- **Q: Is Stellar Studio available on Windows, Mac, or Linux?** — clarifies mobile-only availability; suggests desktop alternatives (PixInsight, Siril, APP, Lightroom/Photoshop) for users who prefer desktop post-processing (Section 10)

---

## 2026-03-24 1200 CST

### Added
- **Section 10: Stellar Studio** — new dedicated section (7 Q&A entries) covering what Stellar Studio is, how it differs from the DWARFLAB app, where to get it, key features, offline use, interrupted session recovery, and current version

### Changed
- Renumbered sections 10–14 to 11–15 to accommodate new Stellar Studio section

---

## 2026-03-24 1100 CST

### Added
- **Q: Can the Dwarf Mini photograph comets?** — covers comet GoTo support, ephemeris-based positioning, the V3.3.1 comet coordinate bug fix, and suitability of wide FOV for comet tails (Section 7)

---

## 2026-03-24 0900 CST

### Added
- **Q: Where can I find the DWARFLAB app and firmware version history?** — lists recent Android, iOS, and Stellar Studio versions with dates; links to official download page (Section 5)

---

## 2026-03-24 0000 CST

### Added
- **Q: Does the Dwarf Mini communicate with the DWARFLAB tabletop tripod?** — clarifies the tripod is a passive mechanical accessory with no electronics (Section 3)

### Fixed
- **Tabletop tripod is not included** — corrected FAQ to note the DWARFLAB tabletop tripod is sold separately, not bundled with the Dwarf Mini

---

## 2026-03-23 1600 CST

### Added
- **Section 3: Tripod & Mounting** — new dedicated section (10 Q&A entries) covering:
  - What tripod ships with the Dwarf Mini
  - Mounting thread size (1/4"-20 UNC)
  - How to attach the scope to the tripod
  - Why leveling matters for GoTo accuracy
  - Using a full-size camera tripod
  - Ball heads and pan-tilt heads (level before powering on only)
  - Using the scope without a tripod
  - Adjusting tabletop tripod height (fixed legs — not adjustable)
  - Best surfaces for tripod placement
  - Troubleshooting a wobbly tripod
  - Equatorial mounts / tracking platforms (not supported)

### Changed
- Renumbered sections 3–13 to 4–14 to accommodate the new Tripod & Mounting section
- Removed brief tripod Q ("Does the Dwarf Mini have a tripod?") from Section 2 — content now covered in detail in Section 3

---

## 2026-03-23 1430 CST

### Added
- **Q: What is AP mode?** — explains Access Point mode (default hotspot mode) and contrasts it with STA mode (Section 4)

---

## 2026-03-23 1200 CST

### Added
- **Q: Can I connect the Dwarf Mini to my home Wi-Fi network?** — covers STA mode, benefits, and setup steps (Section 4)
- **Q: How do I stop a current session to slew the telescope to a new target?** — covers press-and-hold Stop button, GoTo to new target, and saving prior stacked image (Section 8)

### Fixed
- **Stop button action corrected** — changed "tapping" to "pressing and holding" the Stop button to end a session

---

## 2026-03-22 0000 CST

### Added
- **README.md** — Initial FAQ with 13 sections and 50+ Q&A entries covering:
  - What Is the Dwarf Mini
  - Hardware & Specifications (spec table)
  - Setup & First Use
  - The Dwarf Lab App
  - Daytime Photography
  - Astrophotography (target types, gain/exposure starting points)
  - GoTo & Tracking
  - Image Capture & Stacking
  - Calibration Frames
  - Storing & Transferring Images
  - Troubleshooting
  - Tips & Best Practices
  - Resources & Community
- **CONTRIBUTING.md** — Contribution guidelines, style guide, and scope definition
- **GitHub Issue Templates** — Three templates for community contributions:
  - New Question
  - Correction
  - General Feedback

---
