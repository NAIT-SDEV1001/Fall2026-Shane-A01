from pathlib import Path

def read_one_movie(file_path):
    movies=[]
    with open(file_path,"r", encoding="utf-8") as file:
        line = file.readline()
        while line !="":
            movie = line.strip()#remove the spaces and \n
            
            if movie:
                movies.append(movie)
            line = file.readline()
    return movies

def main():
    file_path = Path(__file__).parent/"movies.txt"
    movies = read_one_movie(file_path)

    for movie in movies:
        print(movie)

if __name__ == "__main__":
    main()