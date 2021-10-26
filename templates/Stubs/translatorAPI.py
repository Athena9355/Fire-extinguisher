
import requests


def get_numberfact(english_test):

    english_test_final = str(english_test)

    url = "https://numbersapi.p.rapidapi.com/" + english_test_final + "/math"

    querystring = {"fragment":"true","json":"true"}

    headers = {
        'x-rapidapi-host': "numbersapi.p.rapidapi.com",
        'x-rapidapi-key': "72ed5e9bb2mshcd00aff882afab9p1a2357jsnf95bed300a3a"
    }

    responses = requests.request("GET", url, headers=headers, params=querystring)
    return responses.text

