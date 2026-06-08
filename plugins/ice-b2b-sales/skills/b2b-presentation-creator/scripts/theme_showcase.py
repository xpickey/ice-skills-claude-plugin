#!/usr/bin/env python3

"""
theme_showcase.py
Generate an HTML showcase of all available themes from the assets/themes/ directory.
Displays theme swatches, font samples (EN+TH), and JSON preview in modals.
"""

import argparse
import json
import logging
from pathlib import Path
from typing import Dict, List, Tuple

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def discover_themes(themes_dir: Path) -> List[Tuple[str, Path]]:
    """Recursively discover theme JSON files and return (name, path) tuples."""
    themes = []
    for theme_file in themes_dir.rglob("*.json"):
        theme_name = theme_file.stem
        themes.append((theme_name, theme_file))
    return sorted(themes, key=lambda x: x[0])


def load_theme(theme_path: Path) -> Dict:
    """Load theme JSON safely."""
    try:
        with open(theme_path, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.warning(f"Failed to load {theme_path}: {e}")
        return {}


def color_swatch(color: str, label: str) -> str:
    """Generate HTML for a color swatch."""
    return (
        f'<div class="swatch" style="background-color: {color};" '
        f'title="{label}"></div>'
    )


def generate_theme_card(theme_name: str, theme_data: Dict, theme_json: str) -> str:
    """Generate HTML card for a single theme."""
    colors = theme_data.get("colors", {})
    fonts = theme_data.get("fonts", {})

    primary = colors.get("primary", "#333333")
    secondary = colors.get("secondary", "#666666")
    accent = colors.get("accent", "#0066cc")
    background = colors.get("background", "#ffffff")
    text = colors.get("text", "#000000")

    header_font = fonts.get("header", "sans-serif")
    body_font = fonts.get("body", "sans-serif")

    modal_id = theme_name.replace(" ", "-").lower()
    json_escaped = theme_json.replace('"', "&quot;").replace("\n", "&#10;")

    card_html = f"""
    <div class="theme-card">
        <div class="theme-header">
            <h3>{theme_name}</h3>
        </div>

        <div class="color-swatches">
            {color_swatch(primary, f"Primary: {primary}")}
            {color_swatch(secondary, f"Secondary: {secondary}")}
            {color_swatch(accent, f"Accent: {accent}")}
            {color_swatch(background, f"Background: {background}")}
            {color_swatch(text, f"Text: {text}")}
        </div>

        <div class="font-samples">
            <div style="font-family: {header_font}; font-size: 18px; font-weight: bold; margin-bottom: 8px;">
                Header Font: {header_font}
            </div>
            <div style="font-family: {header_font}; font-size: 14px; margin-bottom: 12px;">
                ทดสอบฟอนต์หัวข้อภาษาไทย
            </div>

            <div style="font-family: {body_font}; font-size: 14px; margin-bottom: 8px;">
                Body Font: {body_font}
            </div>
            <div style="font-family: {body_font}; font-size: 12px; margin-bottom: 12px;">
                ตัวอย่างข้อความภาษาไทยในฟอนต์ Body
            </div>
        </div>

        <button class="json-button" onclick="showModal('{modal_id}')">View JSON</button>

        <div id="{modal_id}" class="modal" onclick="closeModal('{modal_id}')">
            <div class="modal-content" onclick="event.stopPropagation()">
                <span class="close" onclick="closeModal('{modal_id}')">&times;</span>
                <h4>{theme_name}</h4>
                <pre>{theme_json}</pre>
            </div>
        </div>
    </div>
    """
    return card_html


def generate_html(themes: List[Tuple[str, Path]]) -> str:
    """Generate complete HTML document with all theme cards."""
    cards_html = ""

    for theme_name, theme_path in themes:
        theme_data = load_theme(theme_path)
        with open(theme_path, "r") as f:
            theme_json = json.dumps(theme_data, indent=2)

        cards_html += generate_theme_card(theme_name, theme_data, theme_json)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>b2b-presentation-creator — Theme Showcase</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Sarabun:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            color-scheme: light;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', sans-serif;
            background: #f9fafb;
            color: #1f2937;
            padding: 40px 20px;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        h1 {{
            text-align: center;
            margin-bottom: 40px;
            font-size: 32px;
            color: #111827;
        }}

        .theme-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
            gap: 24px;
            margin-bottom: 40px;
        }}

        .theme-card {{
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 24px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            transition: box-shadow 0.3s ease;
        }}

        .theme-card:hover {{
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }}

        .theme-header h3 {{
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 16px;
        }}

        .color-swatches {{
            display: flex;
            gap: 8px;
            margin-bottom: 20px;
            height: 40px;
        }}

        .swatch {{
            flex: 1;
            border-radius: 4px;
            border: 1px solid #d1d5db;
            cursor: pointer;
        }}

        .font-samples {{
            margin-bottom: 20px;
            padding-bottom: 20px;
            border-bottom: 1px solid #f0f0f0;
            font-size: 13px;
        }}

        .json-button {{
            background: #3b82f6;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            transition: background 0.3s ease;
        }}

        .json-button:hover {{
            background: #2563eb;
        }}

        .modal {{
            display: none;
            position: fixed;
            z-index: 1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
        }}

        .modal-content {{
            background: white;
            margin: 10% auto;
            padding: 20px;
            border-radius: 8px;
            width: 80%;
            max-width: 600px;
            max-height: 70vh;
            overflow-y: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }}

        .modal-content h4 {{
            margin-bottom: 16px;
            font-size: 18px;
        }}

        .modal-content pre {{
            background: #f9fafb;
            padding: 12px;
            border-radius: 4px;
            font-size: 12px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
        }}

        .close {{
            color: #6b7280;
            float: right;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
        }}

        .close:hover {{
            color: #111827;
        }}

        footer {{
            text-align: center;
            color: #6b7280;
            font-size: 13px;
            margin-top: 40px;
        }}

        @media (max-width: 768px) {{
            .theme-grid {{
                grid-template-columns: 1fr;
            }}

            h1 {{
                font-size: 24px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>b2b-presentation-creator — Theme Showcase</h1>
        <div class="theme-grid">
            {cards_html}
        </div>
        <footer>
            <p>All themes are self-contained. Click "View JSON" to see theme configuration details.</p>
        </footer>
    </div>

    <script>
        function showModal(modalId) {{
            document.getElementById(modalId).style.display = "block";
        }}

        function closeModal(modalId) {{
            document.getElementById(modalId).style.display = "none";
        }}

        window.onclick = function(event) {{
            if (event.target.classList.contains('modal')) {{
                event.target.style.display = "none";
            }}
        }};
    </script>
</body>
</html>
"""
    return html


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate HTML showcase of all available themes."
    )
    parser.add_argument(
        "--themes-dir",
        type=Path,
        default=Path(__file__).parent.parent / "assets" / "themes",
        help="Path to themes directory (default: ../assets/themes/)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent.parent / "assets" / "theme-showcase.html",
        help="Output HTML file path (default: ../assets/theme-showcase.html)",
    )

    args = parser.parse_args()

    if not args.themes_dir.exists():
        logger.error(f"Themes directory not found: {args.themes_dir}")
        return

    themes = discover_themes(args.themes_dir)
    logger.info(f"Discovered {len(themes)} themes")

    if not themes:
        logger.warning("No themes found in directory")
        return

    html = generate_html(themes)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html)

    logger.info(f"Theme showcase generated: {args.output}")


if __name__ == "__main__":
    main()
