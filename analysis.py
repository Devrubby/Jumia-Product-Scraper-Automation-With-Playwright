import json
import pandas as pd
from pathlib import Path

output = Path("Output")
output.mkdir(exist_ok=True)
input_path = Path("Data")



def read_json():
    file_path = input_path / "scraped_products.json"
    with open(file_path) as data:
        return json.load(data)


def create_dataframe(arg):
    return  pd.DataFrame(arg)

def get_unique_product(df):
    df = df.drop_duplicates(subset=["Product URL"]).copy()
    df["Discount"] = pd.to_numeric(df["Discount"].str.rstrip("%"), errors="coerce")
    return df

def summary_stats(unique_df, products_df):
    max_discount_index = unique_df["Discount"].idxmax()
    min_discount_index = unique_df["Discount"].idxmin()
    most_review_index = unique_df["Number of Reviews"].idxmax()
    least_review_index = unique_df["Number of Reviews"].idxmin()
    most_expensive_index = unique_df["Promo Price"].idxmax()
    cheapest_product_index = unique_df["Promo Price"].idxmin()
    summary = {
        "Total Products Scraped": products_df.shape[0],
        "Unique Products Count": unique_df.shape[0],
        "Duplicate Products Count": products_df.shape[0] - unique_df.shape[0],
        "Highest Price": int(unique_df["Promo Price"].max()),
        "Lowest Price": int(unique_df["Promo Price"].min()),
        "Average Price": float(round(unique_df["Promo Price"].mean(), 2)),
        "Maximum Discount": float(unique_df["Discount"].max()),
        "Minimum Discount": float(unique_df["Discount"].min()),
        "Average Discount": float(round(unique_df["Discount"].mean(), 2)),
        "Highest Review": float(unique_df["Number of Reviews"].max()),
        "Least Review": float(unique_df["Number of Reviews"].min()),
        "Average Reviews": round(float(unique_df["Number of Reviews"].mean()), 2),
        "Average Rating": round(float(unique_df["Rating"].mean()), 2),
        "Sponsored Products Count": int(unique_df["Sponsored"].sum()),
        "Most Expensive Product": unique_df.loc[most_expensive_index,
        ["Product Name", "Discount", "Promo Price", "Old Price"]].to_dict(),
        "Cheapest Product": unique_df.loc[cheapest_product_index, ["Product Name", "Discount", "Promo Price", "Old Price"]
        ].to_dict(),
        "Most Reviewed Product": unique_df.loc[most_review_index, ["Product Name", "Discount", "Promo Price", "Old Price"]].to_dict(),
        "Lowest Reviewed Product": unique_df.loc[least_review_index, ["Product Name", "Discount", "Promo Price", "Old Price"]].to_dict(),
        "Maximum Discount Details": unique_df.loc[max_discount_index,
        ["Product Name", "Discount", "Promo Price", "Old Price"]].to_dict(),
        "Minimum Discount Details": unique_df.loc[min_discount_index,
        ["Product Name", "Discount", "Promo Price", "Old Price"]].to_dict(),
    }
    return summary




def brand_analysis(df):
    df = df.copy()
    df["Brand"] = df["Product Name"].str.split().str[0]
    return df["Brand"].value_counts()

def find_price_range(df):
    df = df.copy()
    bin_edges = [0, 100000, 200000, 300000, 400000, float('inf')]
    bin_labels = ['0 - 100K', '100K - 200K', '200K - 300K', '300K - 400K', '400K+']
    df["Price Range"] = pd.cut(df["Promo Price"], bins=bin_edges, labels=bin_labels)
    range_counts = df["Price Range"].value_counts().to_dict()
    return  range_counts