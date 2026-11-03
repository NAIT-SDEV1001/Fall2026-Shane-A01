from pathlib import Path

def write_movie(file_path, movie):

    with open(file_path,"a",encoding="utf-8") as file:        
        file.write(f"{movie}\n")

#write a list of movies to a file
def write_movies(file_path, movies):
    with open(file_path,"w",encoding="utf-8") as file:
        for movie in movies:
           file.write(f"{movie}\n") 

#write a list of movies to a file using writelines()
def write_movies_writelines(file_path, movies):
    with open(file_path,"w",encoding="utf-8") as file:
        file.writelines(f"{movie}\n"  for movie in movies)#generated expression. behaves like list comprehension BUT does not create a new list
        
#mainline
file_path = Path(__file__).parent/"movies.txt"
#print(file_path.exists())
write_movie(file_path,"Nightmare before Christmas")
write_movie(file_path,"Cujo")

#write a list of movies to a file
file_path = Path(__file__).parent/"movies_list.txt"
movies = ["pacific rim", "Men in Black", "Shrek", "Star Wars", "Paul"]
write_movies(file_path,movies)


#write a list of movies to a file using writelines()    
file_path = Path(__file__).parent/"movies_list_writelines.txt"
write_movies_writelines(file_path,movies)


 

