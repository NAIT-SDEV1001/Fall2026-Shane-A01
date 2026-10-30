#Import the Path class
from pathlib import Path

def read_all_movies(file_path):
    try:
        #open a connection to the file for reading
        with open(file_path,"r", encoding = "utf-8") as file:
            movies = file.readlines()
            #for each movie, if after removing the extra spaces, still has a value, then add it to the clean_movies list
            clean_movies = [movie.strip() for movie in movies if movie.strip()] 
        return clean_movies

    except FileNotFoundError:
        return None

def main():
    #from the path of the current file(py file), find it's parent folder and get the txt file from there
    file_path = Path(__file__).parent/"movies.txt"
    movies = read_all_movies(file_path)
    
    if movies is None:
        print("The file could not be found")
    else:
        #loop through list to show movies
        for movie in movies:
            print(movie)

if __name__ == "__main__":
    main()