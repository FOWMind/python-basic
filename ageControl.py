# Age control for cinema

def watchMovie(movie):
    print( 'Playing "{}"'.format( movie.capitalize() ) )


# normal movies
movies = [
    'lion king',
    'toy story 4'
]

# +18 movies list
movies_18 = [
    'fifty shades of grey'
]

def ageControl():
    try:
        # Show movies list (not +18)
        output = ''
        moviesListLen = len(movies)
        for i in range(0, moviesListLen):
            output += '{}.- {}\n'.format( i, movies[i].capitalize() )
        print(output)

        movie = input('Select your movie (name): ').lower()

        # if movie doesn't exist
        if movie not in movies and movie not in movies_18:
            print('Oops! that movie doesn\'t exist.')
            return ''

        maxAge = 130
        age = int( input('Please enter your age (number): ') )
        
        # Default message
        message = 'Unknown error. Please contact to our support team.'

        if age < 0:
            print('Insert an valid input!')
            return ''
        elif age > maxAge:
            exit()

        if movie in movies_18:
            if age >= 18:
                message = 'Welcome, enjoy your +18 movie.'
                watchMovie(movie)
            elif age >= 0 and age < 18:
                message = 'Hey, you are too chiquito, please grow before enter to our cinema!'
        else:
            message = 'Welcome, enjoy your movie! :)'
            watchMovie(movie)
        
        return message
    except:
        print('An unexpected error ocurred while processing input.')
        return ''

if __name__ == '__main__':
    try:
        print( ageControl() )
    except KeyboardInterrupt:
        exit()