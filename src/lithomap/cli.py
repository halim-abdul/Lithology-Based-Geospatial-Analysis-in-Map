"""Command-line entry point."""
from __future__ import annotations
import argparse
import json
from lithomap.io import load_fault_slip
from lithomap.schema import validate_schema, validate_ranges
from lithomap.summary import geographic_extent, category_summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Lithology-aware geospatial analysis")
    parser.add_argument("data", help="Path to the PANGAEA tab-delimited table")
    parser.add_argument("--skiprows", type=int, default=119)
    args = parser.parse_args()

    df = load_fault_slip(args.data, skiprows=args.skiprows)
    validate_schema(df)
    validate_ranges(df)
    payload = {**category_summary(df), "extent": geographic_extent(df)}
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
