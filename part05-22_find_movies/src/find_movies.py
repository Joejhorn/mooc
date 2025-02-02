def add_movie(database, name, director, year, runtime):
    temp = {}
    temp["name"] = name
    temp['director'] = director
    temp["year"] = year
    temp["runtime"] = runtime
    database.append(temp)

def find_movies(database, name ):
    temp = []
    for movie in database:
        if name.lower() in movie["name"].lower() or name.lower() in movie["director"].lower():
            temp.append(movie)
    return temp

if __name__ == '__main__':
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)