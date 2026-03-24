# Dwarf Mini Smart Telescope — FAQ

*Last updated: 2026-03-24 1300 CST*

A community-maintained FAQ for the **Dwarf Mini Smart Telescope** by DWARFLAB.

> **Want to contribute or suggest a question?**
> Open an [Issue](../../issues) or submit a Pull Request. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## Table of Contents

1. [What Is the Dwarf Mini?](#1-what-is-the-dwarf-mini)
2. [Hardware & Specifications](#2-hardware--specifications)
3. [Tripod & Mounting](#3-tripod--mounting)
4. [Setup & First Use](#4-setup--first-use)
5. [The Dwarf Lab App](#5-the-dwarf-lab-app)
6. [Daytime Photography](#6-daytime-photography)
7. [Astrophotography](#7-astrophotography)
8. [GoTo & Tracking](#8-goto--tracking)
9. [Image Capture & Stacking](#9-image-capture--stacking)
10. [Stellar Studio](#10-stellar-studio)
11. [Calibration Frames](#11-calibration-frames)
12. [Storing & Transferring Images](#12-storing--transferring-images)
13. [Troubleshooting](#13-troubleshooting)
14. [Tips & Best Practices](#14-tips--best-practices)
15. [Resources & Community](#15-resources--community)

---

## 1. What Is the Dwarf Mini?

**Q: What is the Dwarf Mini Smart Telescope?**
The Dwarf Mini is a compact, automated smart telescope made by DWARFLAB. It combines a motorized alt-azimuth mount, a camera, and onboard Wi-Fi into a single portable unit. It is controlled entirely through the DWARFLAB smartphone app — there is no eyepiece. Images are captured, stacked, and displayed live on your phone.

**Q: How is the Dwarf Mini different from the Dwarf II or Dwarf 3?**
The Dwarf Mini is DWARFLAB's smallest and most affordable model. Compared to the Dwarf II and Dwarf 3, it has a shorter focal length, a smaller aperture, and a more compact form factor. It is well suited for wide-field astrophotography and daytime photography, but is less suited for small planetary detail or faint deep-sky objects that benefit from longer focal lengths.

**Q: Does the Dwarf Mini have an eyepiece?**
No. The Dwarf Mini is a camera-based smart telescope. All viewing is done through the DWARFLAB app on your smartphone or tablet. There is no optical eyepiece.

---

## 2. Hardware & Specifications

**Q: What are the key optical specifications?**

| Parameter | Value |
|---|---|
| Aperture | 24 mm |
| Focal Length | 100 mm |
| Focal Ratio | f/4.2 |
| Main Camera | Sony IMX462 (color) |
| Field of View | ~3.7° × 2.8° |
| Mount Type | Alt-azimuth, motorized |

> **Note:** Specifications are subject to change. Always verify against the official DWARFLAB product page.

**Q: What is the battery life?**
The Dwarf Mini has a built-in battery. Expected runtime varies by use case (motors running, Wi-Fi active, temperature) but is typically in the range of 3–4 hours of continuous operation. Cold weather reduces battery life noticeably.

**Q: What storage does the Dwarf Mini have?**
The Dwarf Mini has internal storage. Check the current firmware release notes for capacity. Images can be transferred to your phone via the app.

---

## 3. Tripod & Mounting

**Q: What tripod comes with the Dwarf Mini?**
The Dwarf Mini does not ship with a tripod, DwarfLab has a nice compact tabletop tripod that works well with the Mini. Its legs fold flat for storage and extend outward for use. The tripod is sized for placement on a table, wall, car roof, or any other flat surface at a comfortable height — not for freestanding use on the ground.

**Q: What is the mounting thread size on the Dwarf Mini?**
The Dwarf Mini uses a standard **1/4"-20 UNC** threaded socket on its base — the same thread used by most cameras and camera accessories. This makes it compatible with a wide range of tripods, adapters, and ball heads.

**Q: How do I attach the Dwarf Mini to the included tripod?**
Align the tripod's center stud with the 1/4"-20 socket on the bottom of the scope and turn clockwise until snug. Finger-tight is sufficient — do not overtighten.

**Q: Does the Dwarf Mini need to be level?**
Yes, and this matters more than it might seem. The Dwarf Mini calculates GoTo pointing positions using an alt-azimuth coordinate system that assumes a level base. A significantly tilted unit will cause GoTo slews to consistently miss targets. Set the tripod on a flat surface before powering on, and confirm the unit is approximately level before starting a session. A small bubble level placed on top of the scope is a handy accessory for this.

**Q: Can I use a full-size camera tripod instead of the included tabletop tripod?**
Yes. Any standard camera tripod with a 1/4"-20 stud or head is compatible. A taller, heavier tripod improves stability — especially in windy conditions — and lets you position the scope at eye level rather than bending over a table. Make sure the tripod head is level before powering on.

**Q: Can I use a ball head or pan-tilt head?**
Yes, but use it only to level the scope before powering on — not to reposition it during a session. Once the Dwarf Mini is powered on and aligned, its own motors handle all movement. Adjusting the tripod head mid-session will break tracking and GoTo alignment and require you to start over.

**Q: Can I use the Dwarf Mini without any tripod?**
You can set the Dwarf Mini directly on a flat, stable surface using its base as a rest. However, even the included tabletop tripod is preferable: it raises the scope slightly, helps level it, and isolates it from surface contact. Direct placement on a hard surface also transmits more vibration.

**Q: How do I adjust the height of the included tabletop tripod?**
The included tabletop tripod has fixed-length legs — it folds and unfolds but is not height-adjustable. If you need more height or adjustability, use a standard camera tripod.

**Q: What surface should I place the tripod on?**
Prioritize firmness and stability. Hard, flat surfaces (concrete, pavement, a solid table) transmit less vibration than soft ones (grass, carpet, a hollow wooden deck). Vibration from footsteps, wind, or a flexing surface shows up in stacked images as star trails or blurred frames.

**Q: The tripod feels wobbly or unstable. What should I do?**
- Make sure all leg locks (if present) are firmly tightened.
- Place the tripod on a firm, level surface.
- On soft ground, press the tripod feet into the surface to seat them before starting.
- If using a full-size tripod with an extendable center column, keep the column retracted — shorter is more stable.
- On a full-size tripod, hanging a weight (a camera bag or dedicated hook weight) from the center column lowers the center of gravity and damps vibration.

**Q: Can I mount the Dwarf Mini on an equatorial mount or tracking platform?**
The Dwarf Mini has its own built-in alt-azimuth tracking motors and is designed for use on a fixed, level tripod. Mounting it on a separate tracking platform is not a supported configuration — the onboard tracking and the platform's motion would conflict. This setup is not recommended.

**Q: Does the Dwarf Mini communicate with the DWARFLAB tabletop tripod?**
No. The DWARFLAB tabletop tripod (sold separately) is a purely mechanical accessory — it has no electronics, no Bluetooth, and no data connection of any kind. The Dwarf Mini has no awareness of what it is mounted on. The tripod's only job is to provide a stable, level platform.

---

## 4. Setup & First Use

**Q: What do I need to get started?**
- The Dwarf Mini telescope
- A smartphone (iOS or Android) with the DWARFLAB app installed
- A clear sky or a distant daytime target for initial alignment
- A charged battery (charge before first use)

**Q: How do I download the app?**
Search for **"DWARFLAB"** in the Apple App Store or Google Play Store. The app is free.

**Q: How does the Dwarf Mini connect to my phone?**
The Dwarf Mini creates its own Wi-Fi hotspot. You connect your phone to that hotspot from your phone's Wi-Fi settings, then open the DWARFLAB app. The app will detect and connect to the telescope automatically.

**Q: Do I need an internet connection to use the Dwarf Mini?**
No. The connection is direct phone-to-telescope over the Dwarf Mini's own Wi-Fi. However, some app features (star catalog lookups, firmware updates) may require internet access. You can enable internet pass-through or use a home Wi-Fi network if the app supports it.

**Q: What is AP mode?**
AP mode (Access Point mode) is the Dwarf Mini's default network mode. In AP mode the telescope acts as its own Wi-Fi hotspot — your phone connects directly to it, and all communication stays between the phone and the scope. There is no internet access in this mode unless your phone has a separate mobile data connection. AP mode is the simplest setup and works anywhere, even in the field with no router nearby. Compare with **STA mode** (see below), where the Dwarf Mini joins an existing Wi-Fi network instead.

**Q: Can I connect the Dwarf Mini to my home Wi-Fi network?**
Yes. The DWARFLAB app includes a **STA mode** (Station mode) option that allows the Dwarf Mini to join your home Wi-Fi network instead of acting as its own hotspot. This gives the telescope internet access (useful for firmware updates and star catalog lookups) while keeping your phone connected to your home network. To set this up, connect to the Dwarf Mini's hotspot first, then use the app's Wi-Fi or network settings to enter your home Wi-Fi credentials.

**Q: How do I turn the Dwarf Mini on and off?**
Press and hold the power button until the indicator light comes on (or off). Refer to the quick-start card included in the box for your specific unit, as button behavior may change with firmware updates.

**Q: What should I do the very first time I use it?**
1. Fully charge the Dwarf Mini before first use.
2. Install the DWARFLAB app on your phone.
3. Power on the Dwarf Mini and connect your phone to its Wi-Fi network.
4. Open the app and follow any first-time setup prompts.
5. Check for and install any available firmware updates before your first observing session.
6. Perform a daytime calibration to familiarize yourself with the controls before attempting astrophotography.

---

## 5. The Dwarf Lab App

**Q: What can the app do?**
The DWARFLAB app is the primary interface for the Dwarf Mini. It provides:
- Live camera preview
- Manual and automated GoTo target selection
- Exposure, gain, and white balance controls
- Automatic image stacking (live stacking)
- Photo and video capture
- Firmware update management
- Battery and storage status

**Q: What do the on-screen icons and controls mean?**
The app UI changes with firmware and app updates. General areas of the screen include:

- **Top bar:** Connection status, battery level, storage indicator
- **Main view:** Live image feed from the telescope
- **Bottom controls:** Shutter/record button, mode selector, settings access
- **Settings panel:** Exposure time, gain, white balance, stacking settings

> **Tip:** If a control is unclear, tap and hold it — some controls show a tooltip. Community-contributed UI descriptions are welcome via Issues.

**Q: Can I control the telescope from a tablet?**
Yes, the DWARFLAB app runs on both smartphones and tablets. A tablet's larger screen can make it easier to review live stacked images.

**Q: Can I use the Dwarf Mini without the app?**
No. The app is required to operate the Dwarf Mini.

**Q: Where can I find the DWARFLAB app and firmware version history?**
The official download and release history page is at [dwarflab.com/pages/dwarflab-app-firmware-download](https://dwarflab.com/pages/dwarflab-app-firmware-download). Recent releases as of early 2026:

| Platform | Version | Date | Notes |
|---|---|---|---|
| Android | V3.3.8 | 2026-02-10 | Sky Finder feature; Star Trail mode; location tag in JPEG metadata; 1×/2× crop for Sun/Moon |
| Android | V3.3.5 B564 | 2025-12-31 | Nearby Devices feature for quick switching between DWARF units; continuous autofocus toggle for DWARF 3 |
| Android | V3.3.1 B528 | 2025-11-12 | New user onboarding guide; improved joystick speed control; fixed comet GoTo coordinates |
| iOS | V3.3.9 B8 | 2026-02-24 | Bug fixes and stability improvements |
| iOS | V3.3.1 B8 | 2025-11-12 | New user onboarding guide; improved joystick speed control |
| Stellar Studio (Android) | V1.4.15.2 | 2026-02-10 | Star Trail mode; Sky Finder; panorama manual framing |
| Stellar Studio (iOS) | V1.0.25.2 | 2026-02-10 | Star Trail mode; Sky Finder; improved Sun & Moon tracking |
| Stellar Studio (Android) | V1.4.12.1 | 2026-01-22 | Nearby Devices feature; Sun & Moon data processing; interrupted session recovery |
| Stellar Studio (iOS) | V1.0.22.1 | 2026-01-22 | Sun & Moon data processing support |
| Stellar Studio | V1.4.7.5 | 2025-11-06 | New dark frame management; single device connection only; bug fixes |

> **Note:** Not all release notes distinguish Dwarf Mini-specific changes from Dwarf 2/3 changes. Always check the official page for the latest version and full release notes.

---

## 6. Daytime Photography

**Q: Can the Dwarf Mini be used during the day?**
Yes. The Dwarf Mini works well as a daytime spotting scope / telephoto camera. It can photograph distant landscapes, wildlife, or other subjects.

**Q: How do I switch to daytime (telephoto) mode?**
In the app, select the **Telephoto** or **Daytime** mode (exact label may vary by app version). In this mode the telescope is controlled like a manual camera — no GoTo or tracking is active.

**Q: What camera settings should I use during the day?**
During the day, use short exposures and lower gain to avoid overexposure. The app's Auto mode is a good starting point. Manually adjust if the image looks blown out (too bright) or noisy.

---

## 7. Astrophotography

**Q: What kinds of objects can the Dwarf Mini photograph?**
The Dwarf Mini's wide field of view makes it best suited for:
- The Moon
- Large nebulae (Orion Nebula, Lagoon Nebula, etc.)
- Star clusters (Pleiades, Beehive Cluster, etc.)
- Wide-field Milky Way shots
- Large galaxies (Andromeda Galaxy)

Smaller or fainter objects (small planetary nebulae, globular cluster detail, planets) are more challenging given the aperture and focal length.

**Q: Can I photograph planets?**
The Dwarf Mini can capture the Moon and bright planets, but the short focal length (100 mm) means planets will appear small. You can see Jupiter's disk and Saturn's rings at high gain, but detailed planetary imaging favors longer focal lengths.

**Q: What gain and exposure settings should I start with for deep-sky objects?**

| Target type | Exposure | Gain |
|---|---|---|
| Moon | 1/100 s – 1/10 s | Low (0–30) |
| Bright nebulae | 5–15 s | Medium (50–80) |
| Faint nebulae / galaxies | 10–30 s | Higher (80–120) |
| Star clusters | 2–10 s | Low–medium |

These are starting points. Adjust based on your sky brightness (light pollution) and the object's brightness.

**Q: How dark does my sky need to be?**
The Dwarf Mini can image from light-polluted skies. Bright targets like the Moon, Orion Nebula, and Andromeda Galaxy are accessible from suburban skies. Fainter objects benefit from darker skies, but the live stacking feature helps pull signal out of moderately light-polluted conditions.

**Q: Should I let the telescope cool down before imaging?**
Thermal equilibration is less critical for the Dwarf Mini than for large reflectors, but letting the unit sit outside for 10–15 minutes before imaging can reduce thermal noise in the camera.

**Q: Can the Dwarf Mini photograph comets?**
Yes. Comets are supported as GoTo targets in the DWARFLAB app. Because comets move relative to the background stars, their coordinates change over time — the app uses current ephemeris data to calculate the comet's position. A bug affecting incorrect comet GoTo coordinates was fixed in Android app V3.3.1 B528 (2025-11-12), so make sure your app is up to date if you plan to image comets. The Dwarf Mini's wide field of view is actually well suited for bright comets, which often have extended tails that benefit from a wider frame.

---

## 8. GoTo & Tracking

**Q: What is GoTo?**
GoTo is the automatic slew feature — you select a target in the app, and the telescope motors move the scope to point at that target.

**Q: How does the Dwarf Mini know where to point?**
The app uses your phone's GPS (or manually entered location) combined with the current date/time to calculate the position of objects in the sky. The Dwarf Mini's motors then move to the calculated coordinates.

**Q: What is star alignment / plate solving?**
Some smart telescope apps use **plate solving** — the camera takes an image, compares the star pattern against a known star catalog, and precisely determines where the telescope is pointing. This corrects for small pointing errors. Check the DWARFLAB app release notes to see if and how plate solving is supported for your firmware version.

**Q: Does the Dwarf Mini track objects?**
Yes. Once pointed at a target, the Dwarf Mini's motors compensate for Earth's rotation to keep the object in frame. This is essential for longer exposures.

**Q: How do I stop a current session to slew the telescope to a new target?**
Stop the current imaging session by pressing and holding the **Stop** button (or shutter button, depending on app version) in the app. The telescope will stop capturing and stacking. You can then use GoTo to select a new target — the scope will slew and begin a fresh stacking session on the new object. Any stacked image from the previous session should be saved to internal storage before you switch targets.

**Q: The GoTo pointed at the wrong part of the sky. What should I do?**
- Make sure your phone's location (GPS) is correct and that the date/time on your phone is accurate.
- Make sure the Dwarf Mini started from a reasonably level position.
- Try a star alignment or re-run the GoTo to a bright, easily identifiable star first to verify pointing.
- Perform a manual correction using the directional controls in the app, then re-center.

---

## 9. Image Capture & Stacking

**Q: What is live stacking?**
Live stacking is the automatic combination of multiple exposures taken back-to-back. Each new frame is aligned and added to the previous frames, progressively building up a brighter, smoother image. The result improves continuously while the telescope keeps shooting.

**Q: How many frames should I stack?**
More frames generally means a better final image. For a first look, even 20–30 frames will show improvement. For a polished result, 100–300+ frames (depending on exposure length and object brightness) is common.

**Q: Can I save the individual frames (RAW/FITS)?**
Check your current app and firmware version — options for saving individual frames or RAW data vary. The app generally saves a processed JPEG of the stacked result. Check the DWARFLAB release notes or community forums for the current capability.

**Q: What image formats does the Dwarf Mini save?**
The primary output is JPEG for processed/stacked images. Availability of RAW or FITS output depends on firmware version.

---

## 10. Stellar Studio

**Q: What is Stellar Studio?**
Stellar Studio is a companion app made by DWARFLAB for post-processing the images captured by your Dwarf Mini (and other DWARF telescopes). While the main DWARFLAB app handles live capture and in-the-field stacking, Stellar Studio lets you revisit your saved data later on your phone or tablet — reprocessing, adjusting, and exporting final images at your own pace.

**Q: Is Stellar Studio the same as the DWARFLAB app?**
No. They are two separate apps:
- **DWARFLAB app** — connects to the telescope, controls the hardware, runs live stacking sessions in the field
- **Stellar Studio** — a post-processing app you use after the session, on data already saved to your device or transferred from the scope

You don't need Stellar Studio to use the Dwarf Mini, but it gives you significantly more control over the final result.

**Q: Where do I get Stellar Studio?**
Stellar Studio is available as a separate download from the Apple App Store and Google Play Store. Search for **"Stellar Studio DWARFLAB"**.

**Q: What can Stellar Studio do that the DWARFLAB app cannot?**
Stellar Studio is focused on post-processing flexibility:
- Re-stack or re-process previously captured frames
- Adjust stretch, brightness, contrast, and color balance after the fact
- Process Sun and Moon data (added in V1.4.12.1 / V1.0.22.1, January 2026)
- Apply Star Trail processing to compatible data sets (added February 2026)
- Access detailed photo and video metadata in the album view

**Q: Do I need to be connected to the telescope to use Stellar Studio?**
No. Stellar Studio works entirely on data already stored on your device. You can use it at home, days after a session, with no connection to the scope required.

**Q: My Stellar Studio session was interrupted. Did I lose my data?**
Not necessarily. As of V1.4.12.1 (January 2026), if an astronomy capture is interrupted unexpectedly, the current partial results remain accessible in the App Album. Check there before assuming the data is lost.

**Q: Which version of Stellar Studio should I have?**
Keep Stellar Studio updated. See Section 5 for a recent version history. As of early 2026, V1.4.15.2 (Android) / V1.0.25.2 (iOS) is current.

**Q: Is Stellar Studio available on Windows, Mac, or Linux?**
No. Stellar Studio is a mobile-only app — iOS and Android. There is no desktop version. Users who prefer desktop post-processing typically export their stacked images from the DWARFLAB app and use third-party tools such as **PixInsight**, **Siril**, **Astro Pixel Processor**, or **Adobe Lightroom/Photoshop** for further processing on a computer.

---

## 11. Calibration Frames

**Q: What are calibration frames?**
Calibration frames are special images used to subtract noise and optical artifacts from your science (light) frames:

- **Dark frames:** Images taken with the lens covered, at the same exposure/gain as your light frames. They capture thermal noise and hot pixels.
- **Flat frames:** Images of a uniformly lit surface (e.g., a white card in daylight). They correct for vignetting and dust.
- **Bias frames:** Very short exposures that capture read noise.

**Q: Does the Dwarf Mini support calibration frames?**
Support varies by firmware and app version. Check current DWARFLAB release notes. Even if manual calibration frame workflows are not fully supported in-app, the dark frames the onboard processor uses may be applied automatically.

---

## 12. Storing & Transferring Images

**Q: Where are images saved?**
Images are saved to the Dwarf Mini's internal storage. They can be transferred to your phone via the app.

**Q: How do I transfer images to my phone?**
Use the gallery or image transfer section of the DWARFLAB app. You can browse stored images and download them to your phone's camera roll.

**Q: Can I access the Dwarf Mini's storage directly (as a USB drive)?**
This depends on firmware. Some versions support a USB mass storage or MTP mode when connected via USB cable. Check the DWARFLAB documentation or community forums for your firmware version.

---

## 13. Troubleshooting

**Q: The app won't connect to the Dwarf Mini. What should I try?**
1. Confirm the Dwarf Mini is powered on and the indicator light is showing a connected/ready state.
2. On your phone, go to Wi-Fi settings and connect to the Dwarf Mini's Wi-Fi network (named something like `DWARF_MINI_XXXXXX`).
3. Close and reopen the DWARFLAB app.
4. If still failing, power cycle the Dwarf Mini and try again.
5. Check that no other device is already connected to the Dwarf Mini (it may only allow one connection at a time).

**Q: The image looks very noisy. What can I do?**
- Increase the number of stacked frames — noise averages out with more frames.
- Reduce gain if the exposure is already long enough.
- Check that the lens cover is removed.
- Make sure the telescope has had time to thermally equilibrate.
- Move to a darker site if possible.

**Q: The motors make noise but the scope doesn't move. What should I do?**
- Make sure the tripod and the unit itself are on a stable surface.
- Check if there is a transport lock or obstruction.
- Restart the Dwarf Mini and try again.
- If the problem persists, contact DWARFLAB support.

**Q: GoTo targets are consistently off by the same amount. What's wrong?**
- Verify your phone's GPS coordinates and time/date are accurate.
- Make sure the Dwarf Mini is level at startup.
- After a GoTo slew, use the manual directional controls to center the target, then perform a sync/alignment if the app supports it.

**Q: Firmware update failed. What should I do?**
- Make sure your phone has internet access (for downloading the firmware).
- Keep the Dwarf Mini close to your phone during the update to maintain a strong Wi-Fi signal.
- Do not power off the Dwarf Mini during a firmware update.
- If an update fails, try restarting both the Dwarf Mini and the app, then attempt the update again.

---

## 14. Tips & Best Practices

- **Charge before every session.** Don't start a session with a partially charged battery.
- **Update firmware.** DWARFLAB releases updates that improve GoTo accuracy, stacking quality, and app features. Stay current.
- **Start with the Moon.** The Moon is an easy, bright target for learning controls, GoTo, and focusing.
- **Use a red flashlight** when working outside at night to preserve night vision.
- **Shield from wind.** Even small breezes can cause vibration that shows up in stacked images as star trails.
- **Note your settings.** Keep a simple log of gain, exposure, and stacking count for your best images so you can repeat them.
- **Join the community.** The DWARFLAB user communities (Facebook groups, Reddit r/telescopes, CloudyNights) have experienced users who share tips and settings.

---

## 15. Resources & Community

- **DWARFLAB Official Website:** [https://www.dwarflab.com](https://www.dwarflab.com)
- **DWARFLAB User Manual / Downloads:** Check the official site's support/download section
- **DWARFLAB App:** Available on Apple App Store and Google Play (search "DWARFLAB")
- **Reddit:** [r/telescopes](https://www.reddit.com/r/telescopes/) and search for "Dwarf Mini"
- **CloudyNights Forums:** [https://www.cloudynights.com](https://www.cloudynights.com) — search for "Dwarf Mini"
- **Facebook:** Search for "DWARFLAB" or "Dwarf Telescope" user groups

---

## Contributing

Have a question that should be in this FAQ? Found an error? Know a better answer?

- **Open an Issue** — describe the question or correction
- **Submit a Pull Request** — add or edit content directly

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

*This FAQ is community-maintained and is not affiliated with or endorsed by DWARFLAB. Information may become outdated as firmware and app updates are released. Always verify critical details against official DWARFLAB documentation.*

*Last updated: 2026-03-24 1300 CST*
