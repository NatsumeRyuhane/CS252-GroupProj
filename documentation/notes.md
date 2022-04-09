# Notes

## Tools will be used in dev

* Frontend: HTML, CSS, JavaScript, jinja2, jQuery
* Backend: Python3.7, Flask
* Database: MySQL, (maybe switch to a non-relational DB will be better? Like mongo or redis or sth)

***Notes***
* The Python3.7 environment and all pip packages is packed with the project (under `/venv`)
* The project is build and tested with the latest version of Firefox under desktop screen ratio. Mobile view is too much and too painful to support, so we won't cover that


## How will this thing work?

Basically like this:

1. The app is done initializing and started a Flask server, entry point is `app.py`
2. The backend gets a HTTP GET request from a client (browser) with a certain URL
3. Based on the request URL, the backend finds a function to handle the request
4. After the backend is done processing (like r/w the DB, process the business logic, etc), the backend utilizes one of the pre-defined jinja2 HTML template (under `/app/templates`) to render a HTML page and send it to the client
5. The client browser display the page (js and css will be run/applied on the client browser and does not require the app to do anything)

As you can see, the hardest part is to write the HTML templates in a manner that they could adapt to various situations that a user may encounter when they use the app.

Another point that might be problematic is that we need to find a way to let the app 'remember' what state/page a user is previously at (like 'remember login' feature). Maybe we could use cookies or sessionID attached at the end of URL? I currently have no idea

## How do we get inputs from the user's browser?

We can do this by using HTML Forms, with HTTP GET or POST method.

Simply say, the HTTP GET is that we make the user to send a request to a certain URL, along with the data they want to submit. That based on which URL they want to visit and the param is encoded inside the request URL itself, we can respond to the user request.

The HTTP POST is even simpler, it is designed to send data to the server after all.

There is a tutorial with this on MDN, there is even a use case with Flask under section 3, I recommend to read it: 

> https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data

## References & Tutorials

* [HTML, CSS, JS] MDN Web Docs - https://developer.mozilla.org/en-US/
* [jQuery] - https://www.runoob.com/jquery/jquery-tutorial.html
* [jinja2] - https://geek-docs.com/python/python-tutorial/python-jinja.html


## Comments & Gibberish

> If we modify the template and the business logics, this project can also be repurposed for the AI course as well, save us some time - CYL, APR 9