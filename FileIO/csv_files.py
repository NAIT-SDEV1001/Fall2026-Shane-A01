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

#read the file into a list of dictionaries
# add a new key/value pair to each dictionary in the list and return the new list 
# new key/value will be listeners_per_member (monthly_listeners/members)
# return the new list
# call the function in the main() and write the new list of dictionaries (with the new key/value pair) to a new file called artists_listeners_per_member.csv   

def listeners_per_member(file_path):
    artists = read_artists(file_path)
    for artist in artists:
        artist['listeners_per_member'] = round(int(artist['monthly_listeners'])/int(artist['members']))
    return artists

def main():
    file_path_read = Path(__file__).parent/"data"/"music_artists.csv"
    artists = read_artists(file_path_read)
    # pprint (artists)

    popular_artists = filter_by_min_listeners(file_path_read,12500000)
    # pprint(popular_artists)

    file_path = Path(__file__).parent/"data"/"popular_music_artists.csv"
    write_artists_to_file(file_path,popular_artists)

    # pprint(listeners_per_member(file_path_read))
    artists = listeners_per_member(file_path_read)

    file_path_listeners_per_file = Path(__file__).parent/"data"/"artists_listeners_per_member.csv"
    write_artists_to_file(file_path_listeners_per_file,artists)



if __name__ == "__main__":
    main()


