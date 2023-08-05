from ..client.client import TheOneAPIClient
from ..common.utils import custom_title_case
from ..common.exceptions import InvalidSearchKeyError


class MoviesAPI:
    """
    This class contains methods for interfacing with TheOneAPI's
    movies endpoint.

    Usage:
        1. Instantiate the TheOneSDK with your API key
        2. Access the movies API methods via `sdk.movies`

    Example:
        ```
        sdk = TheOneSDK('key_123_abc')
        movies = sdk.movies.get_all()
        movies = sdk.movies.search(title
        ```
    """
    def __init__(self, client: TheOneAPIClient):
        self.client = client

    def search(
        self,
        limit: int = None,
        page: int = None,
        offset: int = None,
        sort: str = None,
        **kwargs,
    ) -> dict:
        """
        Search for movies by name. Only movies with an exact character name match will
        be matched. Search is case-insensitive.

        Args:
            limit (int, optional): The maximum number of results to return. Defaults to None.
            page (int, optional): The page of results to return. Defaults to None.
            offset (int, optional): The number of results to skip before starting to return results.
                Defaults to None.
            sort (str, optional): The field to sort the results by. Defaults to None.
            **kwargs: Additional search parameters to filter results by. Only 'name' is an
                approved search key.

        Returns:
            dict: A dictionary containing the search results.

        Raises:
            InvalidSearchKeyError:
                If the match term is not in the following list: ['name']
                (e.g. 'name' is the only approved search key).

        Example usage:
            # Search for all movies with the exact name 'TWO TOWER'
            results = sdk.movies.search(name='TWO TOWER') --> This will not find any results.

            # Search for all movies with the exact name 'THE TWO TOWERS'
            results = sdk.movies.search(name='The Two Tower') --> results for The Two Towers will be found

            # Search for all movies with the exact name 'the return of the king',
            # and sort by release date in ascending order
            results = movies_search(name='the return of the king', limit=10, sort='release_date')
        """
        optional_params = ['limit', 'page', 'offset', 'sort']
        approved_search_keys = ['name']
        # Add additional keyword arguments to the request params
        for key in kwargs:
            if key not in approved_search_keys + optional_params:
                error_msg = f"Invalid search key: {key}. Must be one of {approved_search_keys}."
                self.logger.error(error_msg)
                raise InvalidSearchKeyError(error_msg)
            else:
                value = kwargs[key]
                kwargs[key] = custom_title_case(value)


        return self.get_all(
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            **kwargs,
        )


    def get_all(
        self,
        limit: int = None,
        page: int = None,
        offset: int = None,
        sort: str = None,
        **kwargs,
        # continue to add extra func as time permits (exclude, etc)
    ) -> dict:
        """
        Returns all Lord of the Ring Trilogies and The Hobbit trilogies.

        Args:
            limit (int, optional): Maximum number of results to return.
                Defaults to None.
            page (int, optional): Page of results to return. Defaults to None.
            offset (int, optional): Number of results to skip before
                returning the first item. Defaults to None.
            sort (str, optional): Sort results by this field. Add asc (ascending)
                or desc (descending) to specify the sort order. Defaults to descending

        Returns:
            dict: The response JSON as a dictionary.

        Raises:
            HTTPError: If the API request fails.

        Examples:
            Retrieve all movies:
            >>> sdk.movies.get_all()

            Retrieve the first 10 movies:
            >>> sdk.movies.get_all(limit=10)

            Retrieve the second page of movies, with 3 items per page:
            >>> sdk.movies.get_all(page=2, limit=3)

            Retrieve movies sorted by release date in ascending order:
            >>> sdk.movies.get_all(sort="releaseDate:asc")
        """
        endpoint = self.client.endpoints["movies_list"]
        params = {}

        # Add pagination params to the request if provided
        if limit:
            params["limit"] = limit
        if page:
            params["page"] = page
        if offset:
            params["offset"] = offset
        if sort:
            params["sort"] = sort

        # Add additional keyword arguments to the request params
        for key, value in kwargs.items():
            params[key] = value

        return self.client.get(endpoint, params=params)
