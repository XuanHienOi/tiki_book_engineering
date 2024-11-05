# from extract import query_data_from_sqliteDB
import pandas as pd
import json

def format_time(df: pd.DataFrame) -> pd.DataFrame:
    df['crawl_time'] = pd.to_datetime(df['crawl_time'])
    df['crawl_time'] = df['crawl_time'].dt.date
    return df

def calculate_quantity_by_day(df: pd.DataFrame) -> pd.DataFrame:
    # Convert crawl_time to datetime format
    # df['crawl_time'] = pd.to_datetime(df['crawl_time']).dt.date

    # Sort by tiki_id and crawl_time to ensure correct order for diff
    df = df.sort_values(by=['tiki_id', 'crawl_time'])

    # Calculate quantity_by_day as the difference in all_time_quantity_sold for each tiki_id
    df['quantity_by_day'] = df.groupby('tiki_id')['all_time_quantity_sold'].diff().astype("Int64")

    return df

def extract_authors(df: pd.DataFrame):
    # Convert the JSON string to actual JSON objects (lists of dictionaries)
    df['authors'] = df['authors'].apply(json.loads)
    df['authors'] = df['authors'].apply(lambda author_list: ', '.join([author['name'] for author in author_list]))
    # df.drop(columns=['authors'])
    return df

def extract_categories(df: pd.DataFrame):
    df['categories'] = df['categories'].apply(json.loads)
    # Extract 'id' and 'name' into new columns
    df['category_id'] = df['categories'].apply(lambda x: x['id'])
    df['category'] = df['categories'].apply(lambda x: x['name'])

    # Optionally, drop the original 'categories' column
    df = df.drop(columns=['categories'])
    return df

def extract_specifications(df):
    """
    Extracts attributes from the 'specifications' JSON column in the given DataFrame
    and returns a new DataFrame with each attribute as a separate column.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame containing a 'specifications' column with JSON data.
    
    Returns:
        pd.DataFrame: New DataFrame with extracted specification attributes as columns.
    """
    # Convert specifications column from JSON string to list of dictionaries
    df['specifications'] = df['specifications'].apply(json.loads)

    # Function to extract attributes from each row in the 'specifications' column
    def extract_attributes(specs):
        attributes = {}
        if specs and isinstance(specs, list):
            for spec in specs:
                if 'attributes' in spec:
                    for attribute in spec['attributes']:
                        attributes[attribute['code']] = attribute['value']
        return attributes

    # Apply the function to extract specifications for each row
    specs_extracted = df['specifications'].apply(extract_attributes)

    # Create a new DataFrame from the extracted specifications
    specs_df = pd.DataFrame(specs_extracted.tolist())

    # Concatenate the new specs DataFrame with the original DataFrame (without 'specifications' column)
    result_df = pd.concat([df.drop(columns=['specifications']), specs_df], axis=1)

    return result_df

def transform(df: pd.DataFrame):
    date_formated_df = format_time(df)
    qty_df = calculate_quantity_by_day(date_formated_df)
    authors_extracted_df = extract_authors(qty_df)
    categories_extracted_df = extract_categories(authors_extracted_df)
    specifications_extracted_df = extract_specifications(categories_extracted_df)

    return specifications_extracted_df