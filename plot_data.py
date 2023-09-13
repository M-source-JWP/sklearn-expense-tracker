import pandas as pd
import matplotlib.pyplot as plt
import argparse
from dateutil.parser import parse

def plot_data(start_date, end_date, categories):
    df = pd.read_csv('classified_data.csv')
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

    df = df[(df['Transaction Date'] >= start_date) & 
            (df['Transaction Date'] <= end_date) & 
            (df['Category'].isin(categories)) &
            (df['Amount'] <= 0)]
    
    df['Month'] = df['Transaction Date'].dt.to_period('M')

    for category in categories:
        category_df = df[df['Category'] == category]
        print(f"\nCategory: {category}")
        print(f"Total Amount: {category_df['Amount'].sum()}")
        print(f"Average Amount: {category_df['Amount'].mean()}")
        print(f"Number of Transactions: {len(category_df)}")

    df.groupby(['Month', 'Category'])['Amount'].sum().unstack().plot(kind='bar', stacked=True)
    plt.title('Total Amount by Month')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.legend(title='Category')
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Process and plot transaction data.')
    parser.add_argument('start_date', type=parse, help='Start date for data filtering (format: YYYY-MM-DD)')
    parser.add_argument('end_date', type=parse, help='End date for data filtering (format: YYYY-MM-DD)')
    parser.add_argument('categories', type=str, help='Comma-separated list of categories for data filtering')
    args = parser.parse_args()

    categories = args.categories.split(',')

    plot_data(args.start_date, args.end_date, categories)
