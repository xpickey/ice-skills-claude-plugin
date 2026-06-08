#!/usr/bin/env python3

"""
infographic_builder.py
Generate SVG/PNG infographics from text descriptions, applying theme colors.
Supports Mermaid, Graphviz, and Matplotlib diagram types.
"""

import argparse
import json
import logging
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional, Tuple

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def load_theme(theme_path: str) -> dict:
    """Load theme JSON and return color mapping."""
    try:
        with open(theme_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Theme file not found: {theme_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid theme JSON: {e}")
        sys.exit(1)


def mermaid_to_png(
    input_text: str, theme: dict, output_path: str, width: int, height: int
) -> None:
    """Convert Mermaid diagram to PNG using mermaid-cli."""
    try:
        import shutil
        if not shutil.which("mmdc"):
            logger.error(
                "mermaid-cli not found. Install: npm i -g @mermaid-js/mermaid-cli"
            )
            sys.exit(1)
    except Exception:
        pass

    colors = theme.get("colors", {})
    mermaid_config = {
        "theme": "base",
        "themeVariables": {
            "primaryColor": colors.get("primary", "#3b82f6"),
            "primaryBorderColor": colors.get("primary", "#1e40af"),
            "tertiaryColor": colors.get("accent", "#f97316"),
            "fontFamily": theme.get("fonts", {}).get("body", "Inter"),
            "fontSize": "14px",
        },
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        mermaid_file = tmpdir_path / "diagram.mmd"
        config_file = tmpdir_path / "mermaidConfig.json"
        svg_output = tmpdir_path / "diagram.svg"

        mermaid_file.write_text(input_text)
        config_file.write_text(json.dumps(mermaid_config))

        try:
            subprocess.run(
                [
                    "mmdc",
                    "-i",
                    str(mermaid_file),
                    "-o",
                    str(svg_output),
                    "-c",
                    str(config_file),
                    "-s",
                    "2",
                ],
                check=True,
                capture_output=True,
            )
            logger.info(f"Mermaid SVG generated: {svg_output}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Mermaid render failed: {e.stderr.decode()}")
            sys.exit(1)

        svg_to_png(str(svg_output), output_path, width, height)


def svg_to_png(svg_path: str, output_path: str, width: int, height: int) -> None:
    """Convert SVG to PNG using cairosvg or inkscape."""
    try:
        import cairosvg
        cairosvg.svg2png(url=svg_path, write_to=output_path, output_width=width)
        logger.info(f"PNG saved: {output_path}")
    except ImportError:
        logger.warning("cairosvg not installed. Trying inkscape...")
        try:
            subprocess.run(
                [
                    "inkscape",
                    svg_path,
                    "-o",
                    output_path,
                    f"--export-width={width}",
                    f"--export-height={height}",
                ],
                check=True,
                capture_output=True,
            )
            logger.info(f"PNG saved via inkscape: {output_path}")
        except (subprocess.CalledProcessError, FileNotFoundError):
            logger.error(
                "Neither cairosvg nor inkscape available. "
                "Install: pip install cairosvg OR brew install inkscape"
            )
            sys.exit(1)


def graphviz_to_png(
    input_text: str, theme: dict, output_path: str, width: int, height: int
) -> None:
    """Convert Graphviz DOT to PNG using graphviz Python library."""
    try:
        from graphviz import Source
    except ImportError:
        logger.error("graphviz package not installed. Install: pip install graphviz")
        sys.exit(1)

    colors = theme.get("colors", {})
    fonts = theme.get("fonts", {})

    dot_with_colors = (
        f'graph [bgcolor="{colors.get("background", "white")}", '
        f'fontname="{fonts.get("body", "Inter")}"];\n'
        f'node [color="{colors.get("primary", "#3b82f6")}", '
        f'fontname="{fonts.get("body", "Inter")}"];\n'
        f'edge [color="{colors.get("accent", "#f97316")}"];\n{input_text}'
    )

    try:
        src = Source(dot_with_colors)
        src.render(output_path.replace(".png", ""), format="png", cleanup=True)
        logger.info(f"PNG saved: {output_path}")
    except Exception as e:
        logger.error(f"Graphviz render failed: {e}")
        sys.exit(1)


def matplotlib_to_png(
    input_text: str, theme: dict, output_path: str, width: int, height: int
) -> None:
    """Execute matplotlib Python expression and save as PNG."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        logger.error("matplotlib not installed. Install: pip install matplotlib")
        sys.exit(1)

    colors = theme.get("colors", {})
    fonts = theme.get("fonts", {})

    plt.rcParams["figure.facecolor"] = colors.get("background", "white")
    plt.rcParams["font.family"] = fonts.get("body", "sans-serif")

    try:
        local_ns = {"plt": plt}
        exec(input_text, {"__builtins__": __builtins__}, local_ns)
        fig = local_ns.get("fig")
        if fig:
            dpi = 300
            fig.set_size_inches(width / dpi, height / dpi)
            fig.savefig(output_path, dpi=dpi, bbox_inches="tight")
            plt.close(fig)
            logger.info(f"PNG saved: {output_path}")
        else:
            logger.error("matplotlib code must set 'fig' variable")
            sys.exit(1)
    except Exception as e:
        logger.error(f"matplotlib execution failed: {e}")
        sys.exit(1)


def read_input(input_arg: Optional[str]) -> str:
    """Read diagram source from file or stdin."""
    if input_arg is None or input_arg == "-":
        logger.info("Reading from stdin...")
        return sys.stdin.read()
    try:
        with open(input_arg, "r") as f:
            return f.read()
    except FileNotFoundError:
        logger.error(f"Input file not found: {input_arg}")
        sys.exit(1)


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate SVG/PNG infographics from text descriptions."
    )
    parser.add_argument(
        "--type",
        choices=["mermaid", "graphviz", "matplotlib"],
        required=True,
        help="Diagram type",
    )
    parser.add_argument(
        "--input", help="Input file path or '-' for stdin (default: stdin)"
    )
    parser.add_argument("--theme", required=True, help="Theme JSON path")
    parser.add_argument("--output", required=True, help="Output PNG file path")
    parser.add_argument("--width", type=int, default=1600, help="Width in pixels")
    parser.add_argument("--height", type=int, default=900, help="Height in pixels")

    args = parser.parse_args()

    theme = load_theme(args.theme)
    diagram_source = read_input(args.input)

    logger.info(f"Generating {args.type} infographic: {args.output}")

    if args.type == "mermaid":
        mermaid_to_png(diagram_source, theme, args.output, args.width, args.height)
    elif args.type == "graphviz":
        graphviz_to_png(diagram_source, theme, args.output, args.width, args.height)
    elif args.type == "matplotlib":
        matplotlib_to_png(diagram_source, theme, args.output, args.width, args.height)

    logger.info("Infographic generation complete")


if __name__ == "__main__":
    main()
