# AI-Driven Precision Targeting for Pharmaceutical Sales
### A Predictive Model for Doctor Prioritization and Resource Optimization

**Author:** Abhinav Kumar

A seven-page project website presenting a five-pillar predictive scoring model that
replaces uniform pharmaceutical sales coverage with a quantified, auditable allocation
of field effort and promotional budget.

## Pages

| File | Contents |
|---|---|
| `index.html` | Home — overview, headline results, QR generator |
| `problem.html` | The business problem, stated quantitatively |
| `model.html` | The Doctor Value Score, rubrics, worked example, tiers |
| `methods.html` | All four techniques derived from first principles |
| `results.html` | Feasibility, concentration, territories, engagement |
| `validation.html` | The 123-assertion audit and honest limitations |
| `resources.html` | Downloads and full reference list |
| `app.html` | **The live interactive model** |

## Viewing locally

Double-click `index.html`, or serve the folder:

```bash
python3 -m http.server 8000
```

## Publishing

**GitHub Pages** — push this folder, then Settings → Pages → Deploy from branch →
`main` → `/ (root)`.

**Netlify Drop** — drag the folder onto https://app.netlify.com/drop

`.nojekyll` is included so GitHub Pages serves every file as-is.

## Generating the QR code

Once published, open the home page, scroll to the QR section, paste your live URL and
press Update. Download SVG for print or PNG for slides.

## Key figures

- 600 doctors modelled · 4.15× spend concentration · 63% field utilisation
- 123 assertions independently audited (85 exact, 6 material errors found)
- 10 formulas derived from first principles
