"""
This file is the main file in the project-1.
It crates a list of movies and generates a HTML file.
That would be opened in the browser to display the output
required for the project-1
"""
from media import Movie
import fresh_tomatoes


# creating the Movie objects
raabta = Movie(
                    "Raabta",
                    "147 mins",
                    'A cool call center executive Jimmy Cliff (Saif Ali Khan), a'
                    'wannabe gangster Bachchan Pande (Akshay Kumar), a beautiful'
                    'girl Pooja (Kareena Kapoor) who cant be trusted, Bhaiyyaji'
                    '(Anil Kapoor) a gangster who enjoys killing people as much as he enjoys',
                    'https://images-eu.ssl-images-amazon.com/images/S/sgp-catalog-'
                    'images/boxart_images/2c2fb680-d278-414f-8ffb-87246e18000c-2271'
                    '69d3-47e9-4182-8e57-c5c24287e7c6_RGB_SD._UR150,200_FMJPG_.jpg',
                    "https://www.youtube.com/watch?v=YXjYfpqg8Z0")

bahubali = Movie(
                "Bahubali 2",
                "167 mins",
                'When Shiva, the son of Bahubali, learns about his heritage, '
                'he begins to look for answers. His story is juxtaposed with '
                'past events that unfolded in the Mahishmati Kingdom.',
                'https://images-na.ssl-images-amazon.com/images/M/MV5BYmE1MTg'
                '0MDMtZmFlMC00ZGM3LTlkYWItNzEzOWRmODlhNDQ2XkEyXkFqcGdeQXVyN'
                'zMxMzYyOTI@._V1_UX182_CR0,0,182,268_AL__QL50.jpg',
                "https://www.youtube.com/watch?v=qD-6d8Wo3do")

kaatruveliyidai = Movie(
                                "KaatruVeliyidai",
                                "138 mins",
                                'Kaatru Veliyidai is a passionate love story, between'
                                ' a fighter pilot, VC and a doctor, Leela, that mirrors'
                                ' the picturesque and turbulent Srinagar that it is set in.',
                                'https://images-eu.ssl-images-amazon.com/images/'
                                'S/sgp-catalog-images/boxart_images/09296134-82a1-'
                                '44a8-85f7-02251b8828a9-9b560633-2d83-407f-955f-55'
                                'b4ef6ea58c_RGB_SD._UY500_UX375_RI_VlE80LGFCKSiyOD7'
                                'PYd5qciFYtsNipm5B_TTW_SX400_SY300_.jpg',
                                "https://www.youtube.com/watch?v=KPq5I282jKQ")

singam = Movie(
                    "Singam 3",
                    "151 mins",
                    'A police officer makes it his mission to destroy the '
                    'most corrupt person in the country, Singam.',
                    'https://images-eu.ssl-images-amazon.com/images/S/sgp-catalog'
                    '-images/boxart_images/a66ad5a6-ad22-48b8-b7b8-5f9072930ef3-35'
                    '595703-1795-41b5-ba0d-7b1d81ea0459_RGB_SD._RI_VmgQV9brLnCDzFZ'
                    '1qEHb18T2zIHtUHPjs_TTW_SX300_.jpg',
                    "https://www.youtube.com/watch?v=L5YMrYNSxiE")

thalapathi = Movie(
                    "Thalapathi",
                    "157 mins",
                    'Surya (Rajnikanth) is an orphan raised in a slum. '
                    'He finds a friend in the local Godfather (Mamooty). '
                    'They rule the town and forms a parallel government.',
                    'https://images-na.ssl-images-amazon.com/images/M/MV5BZGE5'
                    'NzVjNTEtMGUwYi00YzU0LWIyYTctNDc0ZjMxNGNhYzg5XkEyXkFqcGde'
                    'QXVyMjMwODI3NDE@._V1_QL50_.jpg',
                    "https://www.youtube.com/watch?v=GJnQVMbNa_Y")

"""
creating a list of movies which is required as an input for
open_movies_page function in the fresh_tomatoes module
"""
movies_list = [
                raabta,
                bahubali,
                kaatruveliyidai,
                singam,
                thalapathi]

# Generates the html file and opens browser to display it
fresh_tomatoes.open_movies_page(movies_list)
