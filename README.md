# How to run the code

To run web_scraper.py, the following packages need to be installed on the system:

- pyderman
- selenium
- pymongo

web_scraper.py can be executed as follows:

- Run the file without any argument `web_scraper.py`
- Or, run the file passing two arguments `web_scraper.py <number_of_scans> <wait_time>`


The WebApp folder contains the website based on the Laravel 7.x MVC framerwork:

- Install all the packages required with the command `composer install`
- Run the web app with the command `php artisan serve`


# How it works

The files web_scraper.py contain the code used to extract data 
from the website https://www.rrpcanada.org/#/ and save it on a mongo database in the cloud.<br />
The database.py contains the code to save the data extracted.

The WebApp folder contains the code to display the data from the mongo database into an html table:
- the CriticalProduct model is in `WebApp\app`
- the CriticalProduct controller is in `WebApp\app\Http\Controllers`
- the critical_products view is in `WebApp\app\resources\views`

The controller makes the request to the mongo database to fetch the data.<br />
The model contains a representation of each critical product saved in the database.<br />
The view contains the code to display the data in html table format.