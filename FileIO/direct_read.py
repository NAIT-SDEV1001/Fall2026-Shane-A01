from pathlib import Path

def read_movies(file_path):
    with open(file_path,"r", encoding="utf-8") as file:
        #Loop through the file directly
        movies = [movie.strip() for movie in file if movie.strip()]
    return movies

def main():
    file_path = Path(__file__).parent/"movies.txt"
    movies = read_movies(file_path)

    for movie in movies:
            print(movie)

if __name__ == "__main__":
    main()