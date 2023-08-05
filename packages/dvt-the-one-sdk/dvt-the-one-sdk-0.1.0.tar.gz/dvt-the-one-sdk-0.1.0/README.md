# dvt_the_one_sdk

`dvt_the_one_sdk` Python SDK provides a intuitive way to interface with TheOneAPI service. Look up movie trivia, titles, quotes, character information and more in a simple and intuitve approach.


Current version supported: `v2`
Current active `endpoints` supported: `/movies`
All non listed versions & endpoints will be rejected by sdk.


Installation:
```
pip install dvt_the_one_sdk
```


To use TheOneAPI, you must first create an instance of TheOneAPIClient by providing your API key:
```
api_key = 'my_api_key'
sdk = TheOneSDK(api_key)
```
The api_key parameter is mandatory and must be a valid API key.
To get your own API key, [go here](https://the-one-api.dev/)




# Search:
For movie title names, the only approved key to search on is `name` and it must be an exact match.
name search is case-insensitive.


This method takes the following parameters:
* name (required): The name of the movie to search for.
* limit (optional): The maximum number of results to return. 
                    Defaults to 1000
* page (optional): The page of results to return.
* offset (optional): The number of results to skip before starting to return results.
                     Defaults to 0
* sort (optional): The field to sort the results by.
                   Defaults to desc

## Examples:
Search for all movies with the exact name 'The Two Towers'
```
>>> response = sdk.movies.search(name="The Two Towers")
>>> print(response)
{'docs': [{'_id': '5cd95395de30eff6ebccde5b',
           'academyAwardNominations': 6,
           'academyAwardWins': 2,
           'boxOfficeRevenueInMillions': 926,
           'budgetInMillions': 94,
           'name': 'The Two Towers',
           'rottenTomatoesScore': 96,
           'runtimeInMinutes': 179}],
 'limit': 1000,
 'offset': 0,
 'page': 1,
 'pages': 1,
 'total': 1}
```

Search for all movies with the exact name 'The Return of the King',
Name search is case-insensitve.
```
>>> response = sdk.movies.search(name='The return of THE king')
>>> print(response)
{'docs': [{'_id': '5cd95395de30eff6ebccde5d',
           'academyAwardNominations': 11,
           'academyAwardWins': 11,
           'boxOfficeRevenueInMillions': 1120,
           'budgetInMillions': 94,
           'name': 'The Return of the King',
           'rottenTomatoesScore': 95,
           'runtimeInMinutes': 201}],
 'limit': 1000,
 'offset': 0,
 'page': 1,
 'pages': 1,
 'total': 1}
```

Search for all movies with the subset of any name will result in no hits found.
```
>>> response = sdk.movies.search(name='The return')
>>> print(response)
{'docs': [], 'limit': 1000, 'offset': 0, 'page': 1, 'pages': 1, 'total': 0}
```


## Get all movies
Returns all Lord of the Ring Trilogies and The Hobbit trilogies.

This method accepts the following parameters
* limit (optional): The maximum number of results to return. 
                    Defaults to 1000
* page (optional): The page of results to return.
* offset (optional): The number of results to skip before starting to return results.
                     Defaults to 0
* sort (optional): The field to sort the results by.
                   Defaults to desc
```
>>> all_movies = sdk.movies.get_all()
>>> print(all_movies)
{'docs': [{'_id': '5cd95395de30eff6ebccde56',
           'academyAwardNominations': 30,
           'academyAwardWins': 17,
           'boxOfficeRevenueInMillions': 2917,
           'budgetInMillions': 281,
           'name': 'The Lord of the Rings Series',
           'rottenTomatoesScore': 94,
           'runtimeInMinutes': 558},
          ...
          {'_id': '5cd95395de30eff6ebccde5d',
           'academyAwardNominations': 11,
           'academyAwardWins': 11,
           'boxOfficeRevenueInMillions': 1120,
           'budgetInMillions': 94,
           'name': 'The Return of the King',
           'rottenTomatoesScore': 95,
           'runtimeInMinutes': 201}],
 'limit': 1000,
 'offset': 0,
 'page': 1,
 'pages': 1,
 'total': 8}
```

Soriting is supported.
Note: Default order_by for sorting is `desc`
```
>>> all_sorted_movies = sdk.movies.get_all(sort='name:asc')
>>> print(all_sorted_movies)
{'docs': [
    {'_id': '5cd95395de30eff6ebccde5a',
           'academyAwardNominations': 1,
           'academyAwardWins': 0,
           'boxOfficeRevenueInMillions': 956,
           'budgetInMillions': 250,
           'name': 'The Battle of the Five Armies',
           'rottenTomatoesScore': 60,
           'runtimeInMinutes': 144},
         ...
          {'_id': '5cd95395de30eff6ebccde58',
           'academyAwardNominations': 3,
           'academyAwardWins': 1,
           'boxOfficeRevenueInMillions': 1021,
           'budgetInMillions': 200,
           'name': 'The Unexpected Journey',
           'rottenTomatoesScore': 64,
           'runtimeInMinutes': 169}],
 'limit': 1000,
 'offset': 0,
 'page': 1,
 'pages': 1,
 'total': 8}
```

For pagination, choose the page size limit. Supply the offset to move forward. 
Note: Default offset will always be 0
```
>>> all_sorted_movies = sdk.movies.get_all(limit=2)
>>> print(all_sorted_movies)
 {'docs': [{'_id': '5cd95395de30eff6ebccde56',
           'academyAwardNominations': 30,
           'academyAwardWins': 17,
           'boxOfficeRevenueInMillions': 2917,
           'budgetInMillions': 281,
           'name': 'The Lord of the Rings Series',
           'rottenTomatoesScore': 94,
           'runtimeInMinutes': 558},
          {'_id': '5cd95395de30eff6ebccde57',
           'academyAwardNominations': 7,
           'academyAwardWins': 1,
           'boxOfficeRevenueInMillions': 2932,
           'budgetInMillions': 675,
           'name': 'The Hobbit Series',
           'rottenTomatoesScore': 66.33333333,
           'runtimeInMinutes': 462}],
 'limit': 2,
 'offset': 0,
 'page': 1,
 'pages': 4,
 'total': 8}
>>> next_page = sdk.movies.get_all(limit=2, offset=2)
>>> print(next_page)
{'docs': [{'_id': '5cd95395de30eff6ebccde58',
           'academyAwardNominations': 3,
           'academyAwardWins': 1,
           'boxOfficeRevenueInMillions': 1021,
           'budgetInMillions': 200,
           'name': 'The Unexpected Journey',
           'rottenTomatoesScore': 64,
           'runtimeInMinutes': 169},
          {'_id': '5cd95395de30eff6ebccde59',
           'academyAwardNominations': 3,
           'academyAwardWins': 0,
           'boxOfficeRevenueInMillions': 958.4,
           'budgetInMillions': 217,
           'name': 'The Desolation of Smaug',
           'rottenTomatoesScore': 75,
           'runtimeInMinutes': 161}],
 'limit': 2,
 'offset': 2,
 'total': 8}
```

# Clone & Testing
Repo can be found and cloned [here](https://github.com/danielvantassell/lotr-sdk)
Once cloned, the `virtualenv` & `requirements.txt` have been installed:
```
git clone https://github.com/danielvantassell/lotr-sdk.git
virutalenv -p python3.11 .venv
source .venv/bin/activate
pip install -r requirements.txt
```
You can then run tests for the SDK
```
pytest tests
```


# Logging
Lower or raise logging settings.
Note: Default level is `info`

Accepted Levels: 
* `debug`
* `info`
* `warning`
* `error`
* `critical`

```
sdk.client.logger.set_level('error')
```
