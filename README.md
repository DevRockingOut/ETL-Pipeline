The file web_scraper.py contains the code used to extract data 
from the website https://www.rrpcanada.org/#/
and save it on a mongo database in the cloud

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