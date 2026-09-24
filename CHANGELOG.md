# Changelog - Dwarf Mini Smart Telescope FAQ

All notable changes to this FAQ will be documented in this file.

> **Note for maintainers:** Every entry header **must** include a date, a 4-digit 24-hour time, and the `CST` timezone label.
> Correct format: `## YYYY-MM-DD HHMM CST`
> Example: `## 2026-03-23 1430 CST`

---

## 2026-09-24 0938 CST

### Added
- **High Point Scientific review link** — hands-on Dwarf Mini review added to Resources & Community (Section 16)

### Changed
- **DWARFLAB User Manual / Downloads entry** — replaced "check the official site" with direct links to the DWARF mini User Manual and the App & Firmware Download page (Section 16)

---

## 2026-09-24 0933 CST

### Added
- **Star Trail mode Q&As** — what it is (wide-angle lens, real-time stacking, Classic and Comet MP4 videos at 30 fps), step-by-step setup (mode switch, composition, 30–360 min or infinite duration, Automatic/Quick/Manual settings, on-screen timers), tips (point north for circumpolar trails, power, Mega Stack restacking), wide-angle dark frame requirements, and the 30-frame album minimum; per the DWARF mini user manual §3.2.7 and High Point Scientific's review (Section 8)

### Changed
- **Q: Do I need to shoot my own dark frames?** — added an exception: automatic darks cover the telephoto camera only, and wide-angle modes such as Star Trail need user-captured darks (Section 12)

### Fixed
- **Milky Way Q&A used outdated optics figures** — "~3.7° × 2.8°" field of view and "f/4.2" replaced with the spec-table values (~2.13° × 1.20°, f/5) corrected in #5; reworded to note that a single frame covers only part of the galactic core (Section 8)

---

## 2026-09-24 0929 CST

### Added
- **Q: How does autofocus work?** — explains the internal motorized focuser and contrast-detection routine (sweeps the focus range, scores preview frames for sharpness, settles on the best position), per High Point Scientific (Section 6)

### Fixed
- **Autofocus wrongly described as disabled in Astro Mode** — per the DWARF mini user manual, only the *double-tap* autofocus shortcut is disabled in Astro Mode; the AF button still works. Corrected the trigger and troubleshooting answers and added DWARFLAB's recommended Infinity → AF workflow (Section 6)
- **Observer's Checklist focus steps** — restored the "tap AF to fine-tune" step that was incorrectly removed in the previous focus fix, and corrected the Astro Mode note to refer only to double-tap

---

## 2026-09-24 0924 CST

### Changed
- **Q: What is Sky Finder?** — verified against DWARFLAB's V3.3.8 release notes and the DWARF mini user manual (wide-angle lens and GoTo-from-view confirmed); added where to open it (Select Target window in Astro/Deep Sky mode), Refresh/joystick re-identification, the camera icon for one-tap GoTo, and a wide-angle exposure/gain tip (Section 9)

---

## 2026-09-24 0919 CST

### Fixed
- **Wide-angle lens focus answer conflated "fixed focal length" with "fixed focus"** — every prime lens has a fixed focal length; the reason the wide-angle lens can't be focused is that it is fixed-focus with no focus motor (Section 6)
- **Observer's Checklist focus steps contradicted themselves** — the checklist said to tap AF to fine-tune after pressing Infinity, while also noting AF is disabled in Astro Mode; removed the AF step so the night-session steps match the FAQ (Infinity → manual +/− if needed → Update Auto Focus Position)
- **Observer's Checklist EQ setup still overstated the Polaris requirement** — brought the checklist in line with the 2026-09-23 1912 FAQ fix: tilt to latitude and point roughly north/south; seeing Polaris is not required

---

## 2026-09-23 1926 CST

### Added
- **Weight, battery capacity, rotation range, and charging specs** — added to the spec table (840 g, 7000 mAh, 225° lens barrel tilt + 360° base rotation) and a new charging Q&A (USB-C, USB-PD 12V/2A fast charge vs. 5V slow charge, ~100 min full charge, usable while charging), verified against DWARFLAB's official spec sheet and user manual (Section 2)

### Changed
- **Spec table question renamed** from "What are the key optical specifications?" to "What are the key specifications?" since the table now includes non-optical fields

---

## 2026-09-23 1912 CST

### Fixed
- **EQ mode setup instructions overstated the Polaris requirement** — "physically tilt the Dwarf Mini so it points toward Polaris" wrongly implied a direct line of sight to the star is needed; corrected per DWARFLAB's official user manual, which states the Dwarf Mini does not require you to "see" Polaris (or Sigma Octantis) — only the rotation axis needs to align, achieved by tilting to latitude and pointing roughly north/south (Section 2)

---

## 2026-09-23 1908 CST

### Changed
- **Storage capacity filled in** — replaced the "check the current firmware release notes for capacity" hedge with the confirmed spec: 64 GB built-in eMMC storage, no microSD card slot (Section 2)

---

## 2026-09-23 1906 CST

### Fixed
- **Hardware/specs table was substantially wrong** (GitHub issue #5) — corrected Aperture (24mm → 30mm), Focal Length (100mm → 150mm), Focal Ratio (f/4.2 → f/5), Main Camera (Sony IMX462 → Sony IMX662), and Field of View (~3.7°×2.8° → ~2.13°×1.20°, diagonal ~2.45°); all values verified against DWARFLAB's official product page spec data and corroborated by multiple independent retailer/review sources (Section 2)
- **Dwarf II/3 comparison text was inaccurate** — corrected the claim that the Dwarf Mini has a shorter focal length and smaller aperture than both other models; it actually matches the Dwarf 3's 150mm focal length and has a larger aperture than the Dwarf II's 24mm (Section 1)
- **Pano Weave explanation incorrectly claimed the Dwarf Mini is a single-camera system** — the Dwarf Mini has a dual-camera system (telephoto + wide-angle) just like the Dwarf 3, contradicting the original 2026-03-24 1830 CST changelog entry; replaced the false hardware explanation with an honestly-hedged one pointing to sensor resolution (~2MP vs ~8MP) as the likely factor (Section 11)
- **`build-html.py` / `make-html.sh` HTML build pipeline was broken** — both scripts still read from `README.md`, which had been replaced by `FAQ_Dwarf-Mini-Telescope.md` as the FAQ source in an earlier rename; repointed both scripts at the current source file. Also loosened the "Last updated" timestamp regex to accept the date with or without an `HHMM` time component, since a prior edit had dropped the time and silently broken the old regex. Regenerating `docs/index.html` with the fix also caught up content (the "ephemeris question") that had been added to the FAQ but never propagated to the HTML while the pipeline was broken

---

## 2026-03-28 0853 CST

### Fixed
- **All TOC anchor links containing `&` were dead on GitHub** — GitHub's markdown renderer collapses spaces around `&` to a single hyphen; updated 9 TOC anchors from double-hyphen (`--`) to single-hyphen (`-`)
- **`build-html.py` anchor generation updated** to match GitHub's algorithm (remove special chars first, then collapse `\s+` to single hyphen); HTML page TOC links now consistent with GitHub rendered README

---

## 2026-03-28 0841 CST

### Fixed
- **Section 3: Tripod & Mounting** — removed all references to "included tabletop tripod"; DWARFLAB tabletop tripod is sold separately, not bundled with the Dwarf Mini. Updated four Q&A entries accordingly.

---

## 2026-03-26 1804 CST

### Changed
- **Q: What is the Dwarf Mini Smart Telescope?** — expanded to emphasize the three-part system (hardware + smartphone + app), and that the phone is an active essential component, not just a remote control (Section 1)

---

## 2026-03-26 1236 CST

### Added
- **Q: How does the telescope know where it is pointing and how to move to the next target?** — explains the full navigation stack: GPS/time, IMU, motor tracking, GoTo calculation, and plate solving (Section 9)

---

## 2026-03-24 1230 CST

### Added
- **Q: What is Panorama mode?** — covers EQ mode requirement, manual framing, how panels are captured, and stitching options on desktop (Hugin, PTGui, ICE) since Pano Weave is DWARF 3 only (Section 10)

---

## 2026-03-24 0721 CST

### Changed
- **Section 12: Calibration Frames** — fully rewritten with accurate Dwarf Mini-specific detail:
  - Dark frames: automatic via built-in filter wheel dark filter
  - Flat/Bias frames: factory pre-loaded per device; user capture in development
  - Added summary table (Dark/Flat/Bias support status)
  - Added Q&A on accessing `CALI_FRAME` files for use in Siril, PixInsight, etc.

---

## 2026-03-24 1900 CST

### Added
- **Section 6: Focusing** — new section (6 Q&A entries) covering autofocus, manual focus +/− controls, the Infinity (∞) button, updating the Auto Focus Position reference, autofocus troubleshooting, and the fixed-focus wide-angle lens

### Changed
- Renumbered former sections 6–15 to 7–16 to accommodate new Focusing section

---

## 2026-03-24 1830 CST

### Fixed
- **Pano Weave clarified as definitively unavailable on Dwarf Mini** — updated Infinity Lab table from "not confirmed" to "No — DWARF 3 only"; added hardware explanation (single-camera vs dual-camera system) per official app v3.3.5 release notes

---

## 2026-03-24 1800 CST

### Added
- **Q: What is Infinity Lab?** — explains the three-tool suite (Mega Stack, Stellar Studio, Pano Weave) with a support table noting Pano Weave is DWARF 3 only (Section 10)

### Changed
- **Section 10 renamed** from "Stellar Studio" to "Stellar Studio & Infinity Lab" to reflect broader scope

---

## 2026-03-24 1700 CST

### Fixed
- **Milky Way key tips list not rendering in HTML** — added missing blank line between `**Key tips:**` heading and bullet list; pandoc requires a blank line to recognize the list

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
