import os
from scrapper import search_products
import pandas

def getProducts(search_q: str) -> str:
    """
    Helper function that saves the products as a csv file in the root dir as "out.csv"
    Also returns a JSON string that contains product name, price, URL, etc. as a list 
    of objects.

    Args:
        search_q (str): The search query
 
    Returns:
        str: a JSON string containing a list of products
    """
    df = search_products(search_q)
    saveProducts(df)
    jsonObj = df.to_json(orient="records")
    return jsonObj


def saveProducts(df: pandas.DataFrame)->None:
    """
    Saves the dataframe as a CSV file inside ./outputs. Creates the directory if not present already.

    Args:
        df(pandas.Dataframe): Dataframe containing the products
    """
    os.makedirs('output', exist_ok=True)  
    df.to_csv('output/out.csv')

if __name__ == "__main__":
    search_q = input("Enter the search query: ")
    jsonObj = getProducts(search_q)
    print(jsonObj)
