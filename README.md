# Django Pokemon Theme-Team

Recreate your Pokemon Theme-Team application using Django.


## Requirements
- Create a django project and app, like we've been doing.
- When a user visits the home page, django should send a request to the [pokemon api](https://pokeapi.co/) using the python `requests` library to request a random pokemon, then request 5 more pokemon that share a type with the random one. 
- Render an HTML template that includes images of all 6 pokemon
- Do not use any client-side javascript. 
- Allow the user to optionally specify the first pokemon, instead of choosing it at random, by passing in its ID number in the query string.

## Resources
[requests](https://docs.python-requests.org/en/latest/)
[Pretty Print](https://docs.python.org/3/library/pprint.html)