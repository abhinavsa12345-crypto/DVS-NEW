# How to publish this on GitHub Pages

Two routes. **Route A needs no command line at all** — use it if you're unsure.

---

## Route A — Web upload (easiest, ~5 minutes)

### 1. Create the repository

1. Go to **https://github.com/new**
2. **Repository name:** `dvs-manager`
3. Set it to **Public** *(GitHub Pages is free only for public repos)*
4. **Do not** tick "Add a README" — this folder already has one
5. Click **Create repository**

### 2. Upload the files

1. On the new empty repo page, click **uploading an existing file**
2. Drag in **every file from this folder**, including:
   - `index.html`, `app.html`, `qrlib.js`
   - the three `.pdf` files
   - `README.md`, `PUBLISH.md`, `make_qr.py`
   - **`.nojekyll`** ← easy to miss, it's a hidden file
3. Click **Commit changes**

> **Can't see `.nojekyll`?** Hidden files don't show in some file pickers.
> On Windows: in the file dialog, type `.nojekyll` in the filename box.
> On Mac: press `Cmd + Shift + .` in Finder to reveal hidden files.
> If you truly can't upload it, create it on GitHub instead:
> **Add file → Create new file**, name it `.nojekyll`, leave it empty, commit.

### 3. Turn on Pages

1. **Settings** tab → **Pages** in the left sidebar
2. **Source:** Deploy from a branch
3. **Branch:** `main`, folder: `/ (root)`
4. **Save**

Wait 1–2 minutes, refresh the page, and your URL appears at the top:

```
https://YOUR-USERNAME.github.io/dvs-manager/
```

---

## Route B — Command line

Replace `YOUR-USERNAME` throughout.

```bash
cd dvs-manager-repo

git init
git add -A
git commit -m "DVS Manager — doctor targeting model and site"
git branch -M main

# Create the repo first at https://github.com/new (public, no README), then:
git remote add origin https://github.com/YOUR-USERNAME/dvs-manager.git
git push -u origin main
```

Then enable Pages exactly as in **Route A, step 3**.

### If it asks for a password

GitHub no longer accepts account passwords over HTTPS. Create a token:

1. **https://github.com/settings/tokens** → *Generate new token (classic)*
2. Tick the **`repo`** scope, generate, and copy it
3. When git prompts for a password, paste the **token**

Or install the GitHub CLI and let it handle auth:

```bash
gh auth login
gh repo create dvs-manager --public --source=. --push
```

---

## After it's live

### Generate the QR code

1. Open `https://YOUR-USERNAME.github.io/dvs-manager/`
2. Scroll to the **QR Code** section
3. Paste your live URL and press **Update**
4. **Download SVG** for your poster (stays sharp at any size) or **PNG** for slides

> **Tip:** point the QR at the landing page (`/`) rather than `/app.html`.
> Visitors then get the context, the downloads *and* the tool.

### Updating later

**Web:** open the file on GitHub → pencil icon → edit → commit.
**Command line:**

```bash
git add -A
git commit -m "Update"
git push
```

Changes go live in about a minute.

---

## Troubleshooting

| Problem | Cause and fix |
|---|---|
| **404 page not found** | Pages takes 1–2 min on first deploy. Also confirm the repo is **Public** and that a file named exactly `index.html` sits in the repo root. |
| **Page loads but QR area is blank** | `qrlib.js` didn't upload, or `.nojekyll` is missing. Check both are in the repo root. |
| **PDF links 404** | The three `.pdf` files weren't uploaded. GitHub's web uploader can be slow with the 1 MB report — re-upload and wait for it to finish. |
| **Site shows an old version** | Browser cache. Hard-refresh with `Ctrl+Shift+R` (`Cmd+Shift+R` on Mac). |
| **Changes not appearing** | Check the **Actions** tab for a failed deployment. |

---

## Why `.nojekyll` matters

GitHub Pages runs every site through Jekyll by default, and **Jekyll ignores any file
or folder whose name begins with an underscore**. The QR library was originally named
`_qrlib.js`, which Jekyll would have silently dropped — the page would load but the QR
generator would fail with no error message.

Two safeguards are in place: the file has been renamed to `qrlib.js`, and `.nojekyll`
switches Jekyll off entirely so every file is served exactly as it is.
