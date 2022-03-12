<h1>Project Instructions</h1>

1. Create a PostgreSQL database
2. Change the database settings inside the file settings.py inside djangoProjectg folder
3. Run: *python manage.py makemigrations djangoProject*
4. Run: *python manage.py migrate*
5. Run: *python manage.py runserver <port>*

<h2> Part1: Works Single View</h2>

Navigate to *http://127.0.0.1:8000/* to check the simple view


1. Describe briefly the matching and reconciling method chosen.

>Basically I used the load.py script inside the scripts folder
to upload the data from the csv file. To avoid duplicated values,
I mainly used the update_or_create and get_or_create functions
that help to not create new records if they already exist based
on the iswc or title fields


2. We constantly receive metadata from our providers, how would
you automatize the process?

>Publishing a POST or PUT Methods api to upload a file an update the
records based on that data

<h2> Part1: Works Single View API</h2>

Navigate to *https://127.0.0.1:8000/meta/<iswc>/* where iswc is 
iswc code from the work. i.e. *http://127.0.0.1:8000/meta/T0101974597/*

1. Imagine that the Single View has 20 million musical works, do
you think your solution would have a similar response time?

> In my opinion 20 million of records will degrade the view performance

2. If not, what would you do to improve it?

> I would implement one or all of the following enhancements:
> * Index the table
> * Check if there is any unnecessary queries that are being executed
> * Using memcached that are most hit by the users