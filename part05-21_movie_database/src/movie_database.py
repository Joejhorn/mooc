def add_movie(database, name, director, year, runtime):
    temp = {}
    temp["name"] = name
    temp['director'] = director
    temp["year"] = year
    temp["runtime"] = runtime
    database.append(temp)

if __name__ == '__main__':
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)