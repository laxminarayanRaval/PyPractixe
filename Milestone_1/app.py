movies = []
"""
movie = {
    'name': ...(str),
    'director': ...(str),
    'year': ...(str),
    'rating': ...(str)
}
"""


def menu():
    print("--------------------")
    print("\ta - Add Movie")
    print("\tl - See Movie")
    print("\tf - Find a Movie")
    print("\tq - Quit the Program")
    user_input = input("Enter anything among these 'a','l','f' & 'q' : ")
    print("--------------------")
    return user_input


def add_movie():
    name = input('Movie Name  : ')
    dirct= input('Director    : ')
    year = input('Release Year: ')
    # ratg = float(input('Ratings     : '))
    ratg = input('Ratings     : ')
    movie = {"name": name, "director": dirct, "year": year, "rating": ratg}
    # movies.append(movie)
    # movies.append({"name": name, "director": dirct, "year": year, "rating": ratg})
    return movie


def see_movie(movies_list):
    print("Movie Title \t Director\t Year \t Ratings")
    print("----------- \t --------\t ---- \t -------")
    for i in movies_list:
        print(f"{i['name']} \t {i['director']}\t {i['year']} \t {i['rating']}")
    print("----------- \t --------\t ---- \t -------")
    # print(movies_list)


def find_movie(movies_list):
    choice = {"d": "director", "y": "year", "r": "rating"}
    category = input("Specify in which Category you \n\t (Director : d, Year : y, Ratings : r) \n\t want to find : ").lower()
    looking4 = input("In specified category what you \n\t\t want to find: ")
    print(f"Started looking for {looking4} in {choice[category].capitalize()} Category")
    print(".........")
    found_movies = find_specific_movies(movies_list, choice[category], looking4)
    see_movie(found_movies)
    print(".........")


def find_specific_movies(movies_list, movie_cat, find_data):
    found_movies = []
    for i in movies_list:
        if i[movie_cat].lower() == find_data.lower():
            found_movies.append(i)
    return found_movies


def main():
    while 1:
        x = menu().lower()
        if x == 'q':
            print("Quiting the Program")
            break
        elif x == 'a':
            # print("Perform Add Movie")
            movies.append(add_movie())
        elif x == 'l':
            # print("Perform See Movie")
            see_movie(movies)
        elif x == 'f':
            # print("Perform Find a Movie")
            find_movie(movies)
        else:
            print("Unknown Command")


main()
