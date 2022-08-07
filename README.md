# PaymentWorks
A simple coding test for PaymentWorks

This coding exersize pulls code from the `https://api-v3.mbta.com/` api that serves the greater boston area

To build and run the project make sure to have docker and docker-compose installed on your system then run the following command:

`docker-compose up --build`

Once the container is finished building open your browser and navigate to:
**http://localhost:5000**

### Things I would do if I spent more time:
* build out dataclass's for all of the data stored with numerical values (eg. the various transport types)
* if there were a larger scope I may have gone with a blueprint view instead of a function based one.
* I would have used proper wtforms classes and data validation. Given the scope, this was unnessicarry.
* there was a ton of data availabe in that api. You could expand with heaps of features.
* Added a logger and pushed logs to an appropriate external provider
* Build a testing suite in PyTest. 
* refined the CSS and and page layout.
* depending on deploy stack, prop up a web server and some ssl certs
* Setup some form of caching for API results to reduce the number of calls and improve performance.
