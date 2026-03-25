# Dwarf Mini Observer's Checklist

*A practical pre-session, in-the-field, and post-session checklist for getting the most out of your Dwarf Mini Smart Telescope.*

---

## Before You Go Out

### Days Before the Session
- [ ] Check the weather forecast and moon phase for your planned night
- [ ] Check sky conditions (seeing, transparency) — apps like Clear Outside, Clear Dark Sky, or Astrospheric are useful
- [ ] Identify your targets for the night — know what is in season and visible from your location
      - Milky Way core: best late April–September (northern hemisphere); aim for Sagittarius
      - Large nebulae, star clusters, Andromeda: check seasonal visibility
- [ ] Confirm Bortle class at your planned site (darker = better for faint targets; Bortle 4 or better for Milky Way)
- [ ] If planning EQ mode (exposures ≥15 s, Milky Way, Panorama): locate Polaris in the sky using a star chart app
- [ ] Check available storage space on the Dwarf Mini and your phone; clear space if needed

### Same Day
- [ ] **Fully charge the Dwarf Mini** — do not start a session with a partial charge
- [ ] Charge your power bank if bringing one (highly recommended for long sessions of 2+ hours)
- [ ] Charge your phone / tablet
- [ ] Check that the **DWARFLAB app** is up to date (App Store / Google Play)
- [ ] Check that **Stellar Studio** is up to date if you plan to post-process on your phone
- [ ] Confirm firmware is current (the app will notify you of available updates when connected)

---

## What to Bring

### Essential
- [ ] Dwarf Mini telescope
- [ ] Tripod (tabletop or full-size camera tripod with 1/4"-20 thread)
- [ ] Charged phone or tablet with DWARFLAB app installed
- [ ] USB power bank (capacity: 10,000 mAh or more for sessions over 2 hours)
- [ ] USB cable to connect power bank to Dwarf Mini

### Strongly Recommended
- [ ] Red flashlight or headlamp (preserves night vision; avoid white light)
- [ ] Small bubble level (to confirm the scope is level at setup — critical for GoTo accuracy)
- [ ] Lens cloth or cleaning tissue (for dew or dust on the lens)
- [ ] Extra phone battery or charging cable for your phone

### Situational
- [ ] Dew shield or anti-dew strap (warm, humid nights — the lens can fog during a long session)
- [ ] Wind shield / windbreak (even a light breeze causes vibration in stacked frames)
- [ ] Warm layers / hand warmers (cold weather drains battery life and makes long sessions uncomfortable)
- [ ] Mosquito repellent / bug protection (summer sessions in the field)
- [ ] Observing log or notes app (record gain, exposure, stacking count, and object name for your best sessions)

---

## Power & Battery Backup

The Dwarf Mini's built-in battery provides roughly **3–4 hours** of continuous operation under normal conditions. Cold weather shortens this noticeably. A quality imaging session — stacking hundreds of frames at 15–30 seconds each — can easily run 2–3 hours or longer, so external power is strongly recommended for any serious session.

### Choosing a Power Bank
- [ ] **Capacity:** 10,000 mAh minimum; 20,000 mAh+ recommended for sessions over 2 hours or cold-weather use
- [ ] **Output:** Confirm the power bank has a USB-A or USB-C output port that matches your cable; standard 5V/2A output is sufficient
- [ ] **Pass-through charging:** Confirm the power bank supports charging the Dwarf Mini while it is running (most do, but verify)
- [ ] Avoid very cheap or unknown-brand power banks — inconsistent output voltage can cause the Dwarf Mini to reset mid-session

### Before the Session
- [ ] Fully charge the power bank the day before
- [ ] Pack the USB cable that fits the Dwarf Mini's charging port
- [ ] In cold weather, keep the power bank in an inner pocket until needed — cold reduces lithium battery capacity significantly

### In the Field
- [ ] Connect the power bank **before** the Dwarf Mini's internal battery runs low — connecting it after a cutoff may interrupt a stacking session
- [ ] Route the USB cable so it cannot snag, pull on the scope, or be tripped over
- [ ] Keep the power bank off the cold ground in winter; a small bag or cloth underneath helps retain heat
- [ ] Monitor the power bank's own charge indicator during long sessions — a depleted bank is easy to overlook in the dark

### Phone Battery
- [ ] Keep your phone charged throughout the session — the DWARFLAB app must stay connected for imaging to continue
- [ ] Bring a second USB cable or a two-port power bank so you can charge both the scope and phone simultaneously
- [ ] Enable Low Power Mode on your phone only as a last resort — it can affect Wi-Fi performance and app behavior

---

## Site Setup

- [ ] Choose a surface that is **firm and flat** — concrete, pavement, or a solid table; avoid grass, carpet, or hollow decks
- [ ] If using a full-size tripod: keep the center column **retracted** (shorter = more stable); hang a weight from the center column hook if windy
- [ ] Orient the tripod to give yourself room to view the phone without bumping the scope or cables
- [ ] Do **not** set up under trees, overhangs, or near heat sources (chimneys, HVAC vents, parked cars) — thermals and obstructions degrade image quality
- [ ] Allow 10–15 minutes for the Dwarf Mini to thermally equilibrate after bringing it outside from a warm location

---

## Powering On and Connecting

- [ ] Place the Dwarf Mini on the tripod; hand-tighten the 1/4"-20 mount — finger-tight only, do not overtighten
- [ ] Confirm the scope is approximately **level** using a bubble level (critical for GoTo accuracy)
- [ ] Remove the lens cap / cover
- [ ] Power on the Dwarf Mini (press and hold the power button until the indicator light turns on)
- [ ] On your phone, open **Wi-Fi settings** and connect to the Dwarf Mini's hotspot (e.g., `DWARF_MINI_XXXXXX`)
- [ ] Open the DWARFLAB app — it should detect and connect to the scope automatically
- [ ] Verify **battery level** and **storage status** in the app's top bar
- [ ] If a firmware update is available: install it now (do not power off during the update; keep the phone close)

---

## Alignment and Focusing

### Alt-Az Mode (default; exposures up to ~15 s)
- [ ] Confirm the scope is level
- [ ] In the app, confirm your **GPS location** is correct and phone **date/time** is accurate
- [ ] Use **Sky Finder** (app V3.3.8+) to identify what is currently visible, or select a target directly from the GoTo catalog
- [ ] GoTo a bright star or the Moon first to verify pointing before targeting faint objects

### EQ Mode (exposures ≥15 s, Milky Way, Panorama)
- [ ] Physically tilt the Dwarf Mini so it points toward **Polaris** (the North Star)
- [ ] Follow the EQ alignment procedure in the app to confirm polar alignment
- [ ] The app switches to EQ tracking automatically once aligned

### Focus
- [ ] Tap the **Infinity (∞)** button in the app's focus panel to return to the stored astrophotography focus reference
- [ ] Tap **AF (Auto Focus)** to fine-tune — the button turns green while focusing and white when done
- [ ] If autofocus consistently produces soft stars, use **manual focus** (+/−) to sharpen, then go to **Parameters → Settings → Update Auto Focus Position** to save the new reference
- [ ] Note: autofocus is **disabled in Astro Mode** — use the Infinity button instead

---

## During the Session

### Starting a Target
- [ ] Select your target via GoTo or Sky Finder; let the scope slew to it
- [ ] Set your **exposure** and **gain** appropriate to the target:
  - Moon: 1/100 s – 1/10 s, gain 0–30
  - Bright nebulae: 5–15 s, gain 50–80
  - Faint nebulae / galaxies: 10–30 s, gain 80–120
  - Star clusters: 2–10 s, gain 0–60
  - Milky Way: 10–20 s, gain 80–120
- [ ] Begin stacking and watch the live preview improve with each frame

### While Imaging
- [ ] Do not bump the tripod, touch the scope, or adjust the tripod head mid-session — this breaks tracking
- [ ] Check the **live view periodically** for dew, lens fog, or clouds drifting through the frame
- [ ] Wipe the lens gently with a lens cloth if dew forms — then resume the session
- [ ] Monitor **battery level** — connect the power bank proactively before it runs low rather than letting it cut out
- [ ] Note your settings in an observing log: object name, exposure, gain, filter (if any), number of frames stacked

### Switching Targets
- [ ] **Save your current stacked image** before switching — the in-progress stack may be lost when you GoTo a new target
- [ ] Press and hold the Stop/Shutter button in the app to end the current session
- [ ] Select the new target; the scope will slew and begin a fresh stacking session

### If GoTo Is Off
- [ ] Confirm GPS location and phone date/time are accurate
- [ ] Confirm the scope was level when powered on
- [ ] Use the manual directional controls in the app to center the target, then sync/align if supported
- [ ] GoTo a bright star first to verify pointing before targeting faint objects

---

## Milky Way Session Notes

- [ ] Dark sky confirmed (Bortle 4 or darker strongly recommended)
- [ ] Session is in season (late April–September, northern hemisphere) and core is above 30° altitude
- [ ] EQ mode set up and confirmed before starting
- [ ] Exposure 10–20 s, gain 80–120
- [ ] Power bank connected (a full core session of 100–300 frames at 15–30 s each will exceed the built-in battery)
- [ ] Lens monitored for dew on warm, humid summer nights
- [ ] Panorama mode: use only in EQ mode; plan to stitch panels on desktop (Hugin, PTGui, or Microsoft ICE) — Pano Weave cloud stitching is not available on the Dwarf Mini

---

## Wrapping Up

- [ ] Stop the current session in the app and confirm the final stacked image is saved to internal storage
- [ ] Transfer images to your phone via the app's gallery/transfer section before powering down (or plan to do it via USB/MTP later)
- [ ] Power off the Dwarf Mini (press and hold the power button until the light goes off)
- [ ] Replace the lens cap
- [ ] Disconnect the power bank cable
- [ ] Fold the tripod and pack all gear

---

## Post-Session Processing

### On Your Phone (Stellar Studio)
- [ ] Open **Stellar Studio** and review your saved session data in the album
- [ ] Re-stack or re-process if needed; adjust stretch, brightness, contrast, and color balance
- [ ] For multi-session objects: use **Mega Stack** in Infinity Lab to combine data from separate nights
- [ ] Export your final processed image to your phone's camera roll

### On Desktop (optional — Siril, PixInsight, Astro Pixel Processor, etc.)
- [ ] Transfer raw light frames (`DWARF_RAW` folder) to your computer via USB (MTP mode) or microSD card
- [ ] If using factory calibration frames: locate `Astronomy/CALI_FRAME/` on the device; copy matching `bias`, `flat`, and `dark` folders to your working directory
      - Match gain and binning of factory files to your session settings
      - Use session darks (`DWARF_DARK`) in preference to factory darks (darks are temperature-dependent)
- [ ] Organize working directory: `biases/`, `flats/`, `darks/`, `lights/`
- [ ] Run calibration and stacking script (e.g., a Dwarf-to-Siril script from DeepSkyLab, or the `OSC_Preprocessing` script in Siril)
- [ ] If factory flats cause bright corners (over-correction): run `OSC_Preprocessing_WithoutFlat` and use Background Extraction instead

---

*This checklist is based on the community-maintained Dwarf Mini FAQ. Cross-reference with the FAQ for detailed explanations of any item.*
