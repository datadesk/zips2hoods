import pathlib
import geopandas as gpd

THIS_DIR = pathlib.Path(__file__).parent.absolute()
PARENT_DIR = THIS_DIR.parent.absolute()
DATA_DIR = PARENT_DIR / "data"


def main():
    zips_df = gpd.read_file(DATA_DIR / 'zips.geojson')
    hoods_df = gpd.read_file(DATA_DIR / 'hoods.geojson')
    joined_df = gpd.sjoin(hoods_df, zips_df, how="inner")
    joined_df[['name_left', 'name_right']].rename(columns={
        "name_left": "hood",
        "name_right": "zipcode",
    }).to_csv(DATA_DIR / "zips2hoods.csv", index=False)


if __name__ == '__main__':
    main()
