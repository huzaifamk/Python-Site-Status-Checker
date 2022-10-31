import urllib.request as urllib

# For checking the status of a single site


def single_check():

    print("The program is now running...")

    input_url = input("Input the url of the site you want to check: ")

    response = urllib.urlopen(input_url)

    print("Connected to", input_url, "succesfully")

    print("The response code was: ", response.getcode())

    print("**********************************")


# For checking the status of multiple sites
def multiple_check():

    print("The program is now running...")

    with open("urls.txt", "r") as f:

        for line in f:

            response = urllib.urlopen(line)
            try:
                print("Connected to", line, "succesfully")
                print("The response code was: ", response.getcode())
                print("**********************************")
            except urllib.HTTPError as e:
                print("The site", line, "is not responding")
                print("The error code was: ", e.code)
                print("**********************************")
                break


multiple_check()
