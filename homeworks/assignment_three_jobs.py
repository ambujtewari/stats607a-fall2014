# Assignment 3, Part 3: Pull data about federal jobs
#
# Version 

from urllib2 import urlopen, Request
import json
import pandas as pd


# TASK 3.1
# Implement the get_data function
def get_data(url):
    """ Get response in JSON from URL and convert it into Python dict. """

    # TASK 3.1.1
    # use urlopen() to get a response from the server
    response = response

    # TASK 3.1.2
    # get JSON text from server response
    raw_data = response

    # TASK 3.1.3
    # convert JSON text into Python object
    data = data

    return data


# TASK 3.5
# Implement the numeric_value function
def numeric_value(string):
    """ Get rid of dollar sign & commas and convert to float. """

    pass

# the URL for the Public Jobs API
url = 'https://data.usajobs.gov/api/jobs?CountrySubdivision=Michigan'

# get data from the given URL
print 'Getting initial page of results...'
data = get_data(url)

# TASK 3.2.1
# one of the keys in the Python dict will have the actual
# jobs data
job_list = data['some key']

# TASK 3.2.2
# another key will have information about the number
# of result pages
num_pages = int(data['another key'])

# only the first page is returned above, run a loop
# to get other pages
for page in range(2, num_pages+1):

    # TASK 3.3.1
    # change URL to request a specific page
    url_page = url_page

    # get data from the page specific URL
    print 'Getting page %d of results...' % page
    data = get_data(url_page)

    # TASK 3.3.2
    # extend the list to include the newly fetched jobs
    job_list.extend(data['some key'])

print 'Finished fetching data.'

# TASK 3.4.1
# create a DataFrame from jobs data
df = df

n, d = df.shape
print 'Fetched %d jobs. Have %d attributes for each.' % (n, d)

# TASK 3.4.2
# get the unique agencies that have jobs
agencies = agencies

# for each agency report number of jobs and average min salary
for i in range(len(agencies)):

    # boolean pandas Series to select current agency
    agency_jobs = (df['AgencySubElement'] == agencies[i])

    # number of jobs in this agency
    num_jobs = agency_jobs.sum()

    # average of the minimum salary for jobs in this agency
    mean_salarymin = (df['SalaryMin'][agency_jobs]).map(numeric_value).mean()

    # print current agency's no. of jobs and average min salary
    if num_jobs == 1:
        print '%s has %d job with minimum salary %.2f' \
            % (agencies[i], num_jobs, mean_salarymin)
    else:
        print '%s has %d jobs with average minimum salary %.2f' \
            % (agencies[i], num_jobs, mean_salarymin)
