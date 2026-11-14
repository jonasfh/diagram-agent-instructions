# Vendor & Provider Icon Workflow

Professional architecture diagrams use recognizable vendor and cloud icons rather than generic rectangles.

## 1. Priority Order for Icons

1. **Check local icon cache first**: `docs/diagrams/assets/icons/<vendor>.svg`.
2. **Azure & Cloud Infrastructure**:
   - Prefer **Python `diagrams`** (`diagrams.azure.*`) for pure cloud landing-zone / infrastructure topologies.
   - For D2 software architectures that include Azure services, download official Azure / Terrastruct SVGs (e.g. `https://icons.terrastruct.com/azure/...`) into `docs/diagrams/assets/icons/` so compiled SVGs remain self-contained.
3. **Third-Party & Regional Vendors** (e.g. Vipps, MobilePay, WordPress, Stripe, Slack, MySQL):
   - Download verified SVG icons on demand into `docs/diagrams/assets/icons/<vendor>.svg`.
   - Good sources:
     - **Simple Icons CDN**: `https://cdn.simpleicons.org/<slug>` (e.g. `wordpress`, `mysql`, `stripe`, `php`, `docker`)
     - **Vendor Brand / Press Kits**: e.g. Vipps MobilePay brand assets or Wikimedia Commons / official GitHub brand repos when not in Simple Icons.

## 2. Download & Validation Command

Always verify that a downloaded file is actually an SVG (not an HTML 404/redirect page):

```bash
mkdir -p docs/diagrams/assets/icons
curl -fsSL "https://cdn.simpleicons.org/wordpress/21759B" -o docs/diagrams/assets/icons/wordpress.svg
grep -q "<svg" docs/diagrams/assets/icons/wordpress.svg || { rm -f docs/diagrams/assets/icons/wordpress.svg; exit 1; }
```

## 3. Referencing Icons in `.d2`

Use relative paths from `docs/diagrams/src/<name>.d2`:

```d2
vipps: "Vipps ePayment API" {
  icon: ../assets/icons/vipps.svg
  style.border-radius: 6
}
```

D2 inlines local SVG icons into the compiled output `.svg`, making the final diagram portable and offline-safe.
