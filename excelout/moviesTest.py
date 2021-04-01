#!/usr/bin/python3
import pandas as pd
# use this when you are not rendering to a window
import matplotlib
matplotlib.use('Agg')
# create some graphs
import matplotlib.pyplot as plt

def main():

    excel_file = 'C:/Users/asylb/OneDrive/Documents/TLG/Python/mycode/excelout/movies.xls'

    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)

    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

    movies.drop_duplicates(inplace=True) #remove duplicates
    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)

    sorted_by_gross['Gross Earnings'].head(10).plot(kind="barh")
    plt.savefig("C:/Users/asylb/OneDrive/Documents/TLG/Python/mycode/excelout/movieStackBar.png", bbox_inches='tight')

    sorted_by_imdb = movies.sort_values(["IMDB Score"], ascending=False)
    sorted_by_imdb['IMDB Score'].head(10).plot(kind="line")
    plt.savefig("C:/Users/asylb/OneDrive/Documents/TLG/Python/mycode/excelout/movieIMDB.png", bbox_inches='tight')
    print(sorted_by_imdb.head(10))
    print(movies_sheet1.head())
    print(movies.shape)
    print(sorted_by_gross.head(10))

if __name__ == "__main__":
    main()