#!/bin/bash

# install_fonts.sh
# Install required Thai+English fonts for b2b-presentation-creator skill
# Detects OS (macOS, Linux), installs from Google Fonts, reports success/failure
# Make executable: chmod +x scripts/install_fonts.sh

set -e

FONTS_LATIN=(
    "Inter"
    "Inter Tight"
    "Lora"
    "Manrope"
    "Source Sans 3"
    "Source Serif 4"
    "Playfair Display"
    "Cormorant Garamond"
    "Bricolage Grotesque"
    "JetBrains Mono"
)

FONTS_THAI=(
    "IBM Plex Sans Thai"
    "Sarabun"
    "Prompt"
    "Anuphan"
    "Noto Sans Thai"
    "Noto Serif Thai"
)

INSTALLED=0
FAILED=0

detect_os() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "macOS"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "Linux"
    else
        echo "unknown"
    fi
}

install_mac() {
    local font_name="$1"
    local brew_name=$(echo "$font_name" | tr ' ' '-' | tr '[:upper:]' '[:lower:]')

    echo -n "Installing $font_name... "

    if brew install --cask "font-${brew_name}" &>/dev/null 2>&1; then
        echo "OK"
        ((INSTALLED++))
    else
        echo "FAILED (brew install --cask font-${brew_name})"
        ((FAILED++))
    fi
}

install_linux() {
    local font_name="$1"
    local font_dir="$HOME/.local/share/fonts"
    mkdir -p "$font_dir"

    echo -n "Installing $font_name... "

    local font_url_name=$(echo "$font_name" | tr ' ' '+')

    if curl -sL "https://fonts.google.com/download?family=${font_url_name}" -o "/tmp/${font_name}.zip" 2>/dev/null; then
        unzip -q -o "/tmp/${font_name}.zip" -d "$font_dir" 2>/dev/null && \
        echo "OK" && \
        ((INSTALLED++)) || \
        { echo "FAILED (unzip)"; ((FAILED++)); }
        rm -f "/tmp/${font_name}.zip"
    else
        echo "FAILED (download)"
        ((FAILED++))
    fi
}

main() {
    local os=$(detect_os)

    echo "=================================================="
    echo "b2b-presentation-creator Font Installer"
    echo "Detected OS: $os"
    echo "=================================================="
    echo

    if [[ "$os" == "unknown" ]]; then
        echo "ERROR: Unsupported OS. This script supports macOS and Linux."
        exit 1
    fi

    echo "Installing Latin fonts (Google Fonts, SIL Open Font License)..."
    for font in "${FONTS_LATIN[@]}"; do
        if [[ "$os" == "macOS" ]]; then
            install_mac "$font"
        else
            install_linux "$font"
        fi
    done

    echo
    echo "Installing Thai fonts (Google Fonts, SIL Open Font License)..."
    for font in "${FONTS_THAI[@]}"; do
        if [[ "$os" == "macOS" ]]; then
            install_mac "$font"
        else
            install_linux "$font"
        fi
    done

    if [[ "$os" == "Linux" ]]; then
        echo
        echo -n "Running font cache update... "
        fc-cache -f -v &>/dev/null && echo "OK" || echo "FAILED"
    fi

    echo
    echo "=================================================="
    echo "Installation Summary"
    echo "=================================================="
    echo "Installed: $INSTALLED / $((INSTALLED + FAILED))"
    echo "Failed:    $FAILED / $((INSTALLED + FAILED))"
    echo
    echo "NOTE: TH Sarabun PSK and TH Sarabun New are not available on Google Fonts."
    echo "      For Thai government decks, install these fonts manually:"
    echo "      macOS:  Download from web, double-click to install in Font Book"
    echo "      Linux:  Copy .ttf files to ~/.local/share/fonts/, run fc-cache -f -v"
    echo "=================================================="

    [[ $FAILED -eq 0 ]] && exit 0 || exit 1
}

main "$@"
