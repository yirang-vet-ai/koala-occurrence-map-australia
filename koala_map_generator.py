"""
Koala occurrence map generator for Australia.

Author: YIRANG JUNG
License: Apache License 2.0

This script loads koala occurrence records from a CSV file and generates
an interactive Folium HTML map with clustered koala emoji markers.
"""

from pathlib import Path

import pandas as pd
import folium
from folium.plugins import MarkerCluster
from folium.features import DivIcon


# -----------------------------
# Configuration
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
INPUT_CSV = BASE_DIR / "data" / "koala_selected_columns.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_HTML = OUTPUT_DIR / "koala_map_emoji.html"

SAMPLE_N = 5000
ZOOM_START = 7


def load_and_prepare_data(csv_path: Path) -> pd.DataFrame:
    """Load koala data and clean coordinate columns."""
    df = pd.read_csv(csv_path)

    df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
    df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")

    df = df.dropna(subset=["Latitude", "Longitude"]).copy()
    return df


def sample_data(df: pd.DataFrame, sample_n: int) -> pd.DataFrame:
    """Sample records for faster map rendering."""
    if len(df) > sample_n:
        return df.sample(sample_n, random_state=42)
    return df


def build_popup_html(row: pd.Series) -> str:
    """Create popup HTML for a map marker."""
    return (
        f"<b>ScientificName:</b> {row.get('ScientificName', '')}<br>"
        f"<b>StartDate:</b> {row.get('StartDate', '')}<br>"
        f"<b>EndDate:</b> {row.get('EndDate', '')}<br>"
        f"<b>Locality:</b> {row.get('LocalityDetails', '')}<br>"
        f"<b>Project:</b> {row.get('ProjectName', '')}<br>"
        f"<b>Org:</b> {row.get('OrganisationAcronym', '')}"
    )


def create_map(df_plot: pd.DataFrame, zoom_start: int = 7) -> folium.Map:
    """Create an interactive Folium map with clustered koala markers."""
    center_lat = df_plot["Latitude"].mean()
    center_lon = df_plot["Longitude"].mean()

    koala_map = folium.Map(location=[center_lat, center_lon], zoom_start=zoom_start)
    cluster = MarkerCluster().add_to(koala_map)

    for _, row in df_plot.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=folium.Popup(build_popup_html(row), max_width=350),
            icon=DivIcon(
                icon_size=(36, 36),
                icon_anchor=(18, 18),
                html='<div style="font-size:36px; line-height:36px;">🐨</div>',
            ),
        ).add_to(cluster)

    return koala_map


def main() -> None:
    """Run the full koala map generation pipeline."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = load_and_prepare_data(INPUT_CSV)
    df_plot = sample_data(df, SAMPLE_N)
    koala_map = create_map(df_plot, zoom_start=ZOOM_START)

    koala_map.save(str(OUTPUT_HTML))
    print(f"Saved interactive map to: {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
