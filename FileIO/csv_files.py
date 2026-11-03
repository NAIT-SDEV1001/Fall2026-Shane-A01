#csv files store tabular data
import csv
from pathlib import Path
from pprint import pprint

#Read all the artists
def read_artists(file_path):
    all_artists = []
    try:
        with open(file_path,"r", encoding = "utf-8") as file:
            #Create a reader that
                #creates ONE dictionary per row in the file
                #treat it like a list of dictionaries
                #The first row defines the keys
            reader = csv.DictReader(file)#returns one dictionary at a time
            for artist in reader:#the reader NOW goes to the file to get the next row
                all_artists.append(artist)    

    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    return all_artists

# function to return artists that have more than a certain number of monthly listeners
def filter_by_min_listeners(file_path, minimum):
    artists = read_artists(file_path)
    return [artist for artist in artists if int(artist["monthly_listeners"]) > minimum]   

#write to file
def write_artists_to_file(file_path, artists):
    #create a list of headers. This can come from the keys
    #get the keys from the first dictionary in the list
    fieldnames = list(artists[0].keys())
        
    with open(file_path,"w",newline="",encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        for artist in artists:
            writer.writerow(artist)

def main():
    file_path = Path(__file__).parent/"data"/"music_artists.csv"
    artists = read_artists(file_path)
    # pprint (artists)

    popular_artists = filter_by_min_listeners(file_path,12500000)
    pprint(popular_artists)

    file_path = Path(__file__).parent/"data"/"popular_music_artists.csv"
    write_artists_to_file(file_path,popular_artists)





if __name__ == "__main__":
    main()


