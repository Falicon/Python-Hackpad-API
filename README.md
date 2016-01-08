Python-Hackpad-API
==================

A simple wrapper library for the Hackpad API. [Hackpad API Documentation](https://hackpad.com/Public-Hackpad-API-Draft-nGhsrCJFlP7)

Installation 
==================

Navigate to the folder where you have downloaded this repo, and type

```
easy_install .
```

into your terminal / command prompt.

Usage
==================

```python
temp = Hackpad('your_hackpad_subdomain','your_hackpad_client_id','your_hackpad_secret')
my_hackpads = temp.list_all()
````

Note:

* For `your_hackpad_subdomain`, just type the stem, not the full domain name (i.e. `mysubdomain`, not `http://mysubdomain.hackpad.com`, etc).
* Your Client ID and Secret for the different subdomains you are signed into. Make sure to use the correct keys for the subdomain you are signing into.

