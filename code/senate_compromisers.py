"""
A script to find senators most likely to
compromise with the opposing party.

We use the ProPublica Congress Members API
to find senators most likely to vote
against their own party.


USAGE:

From the command-line:

    python senate_compromisers.py

OUTPUT:

    A list of top 5 most likely to break ranks
    from each major party.

"""
import os
import requests


# The entry point for our script, which calls
# other functions defined below. The "main" function
# is also commonly placed at the end the script, but
# I like putting it at the top to improve readability.
def main():
    api_key = os.environ["PROPUBLICA_API_KEY"]
    members = get_members_data(api_key)
    # TODO: invoke the other functions
    # you create to sort candidates, print
    # the report on top 5 candidates, etc.

### TASK-SPECIFIC FUNCTIONS GO HERE ###

# For example, here's a function to get you started
# on obtaining the members data from the ProPublica API
def get_members_data(api_key):
    """
    Get the members data using requests library
    and return the data as a Python data structure.
    """
    # In order to use the ProPublica API, we must send our
    # API key in the request's "headers." HTTP headers allow us
    # to exchange metadata with a web server.
    # For more background on HTTP:
    #  https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
    # For details on the header required by ProPub's API:
    #  https://projects.propublica.org/api-docs/congress-api/#authentication

    # Below we've prepared the HTTP headers for you.
    # You'll need to use them with requests.get
    headers = {'X-API-Key': api_key }

    # The URL for the Members endpoint
    url = "https://api.propublica.org/congress/v1/117/senate/members.json"

    # TODO: Use requests to call the API
    # This is a bit more involved than our usual requests.get call.
    # See below link for details on how to implement:
    #   https://2.python-requests.org/en/master/user/quickstart/#custom-headers

    # Lastly, below is a placeholder "data" value that
    # you should replace with actual data from the ProPublica API
    data = {}
    return data



# Kick off the script by calling the "main" function
main()
