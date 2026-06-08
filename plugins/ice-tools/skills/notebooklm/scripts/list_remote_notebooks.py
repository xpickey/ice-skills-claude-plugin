#!/usr/bin/env python3
"""List notebooks shown on the NotebookLM home page using the saved auth state."""

import sys
import time
from pathlib import Path

from patchright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).parent))

from browser_utils import BrowserFactory


def main():
    playwright = sync_playwright().start()
    context = None
    try:
        context = BrowserFactory.launch_persistent_context(playwright, headless=True)
        page = context.new_page()
        page.goto("https://notebooklm.google.com", wait_until="domcontentloaded", timeout=45000)

        if "accounts.google.com" in page.url:
            print("❌ Not authenticated — run: auth_manager.py setup")
            return 1

        # Allow client-side render
        try:
            page.wait_for_selector("project-button, a[href*='/notebook/']", timeout=20000)
        except Exception:
            pass
        time.sleep(2.5)

        notebooks = page.evaluate(
            """
            () => {
                const out = [];
                const seen = new Set();
                // Each notebook tile is a project-button containing an anchor to /notebook/<id>
                document.querySelectorAll("a[href*='/notebook/']").forEach(a => {
                    const href = a.href;
                    if (seen.has(href)) return;
                    seen.add(href);
                    // Try to extract a readable title from the surrounding tile
                    let title = '';
                    const tile = a.closest('project-button') || a;
                    const titleEl = tile.querySelector('.project-button-title, .title, [class*="title"]');
                    if (titleEl) title = titleEl.innerText.trim();
                    if (!title) title = (a.innerText || '').trim();
                    out.push({ url: href, title });
                });
                return out;
            }
            """
        )

        if not notebooks:
            print("⚠️  Found 0 notebooks. Page may not have loaded — title was:",
                  page.title(), "url:", page.url)
            return 2

        print(f"\n📚 Found {len(notebooks)} notebook(s) on notebooklm.google.com:\n")
        for i, nb in enumerate(notebooks, 1):
            title = nb["title"] or "(untitled)"
            print(f"  {i:>2}. {title}")
            print(f"      {nb['url']}")
        return 0

    finally:
        if context:
            try:
                context.close()
            except Exception:
                pass
        try:
            playwright.stop()
        except Exception:
            pass


if __name__ == "__main__":
    sys.exit(main())
