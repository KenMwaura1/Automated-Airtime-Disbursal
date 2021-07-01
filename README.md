[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
# Automated-Airtime-Disbursal
This is a simple python script to automate airtime disbursal using google-forms, python and AfricasTalking

This is meant to be a proof of concept code not an exhaustive 
write-up on DIY airtime disbursal.

### Prerequisites
- Python and pip (I am currently using 3.9.2) Any version above 3.5 should work.
- An [Africas Talking account](https://account.africastalking.com/auth/register/).
    - Api Key and username from your account. Create an app and take note of the api key.
    - Additionally, you will need to request them to enable airtime access for your account.
      Email their airtime team for further clarification.
https://github.com/KenMwaura1/Automated-Airtime-Disbursal
## Running the script
1. Clone the Repo

   ```
   git clone https://github.com/KenMwaura1/Automated-Airtime-Disbursal
   ```
2. Create a virtual environment (venv)

   ```
   python3 -m venv venv
   ```

- Activate the virtual environment

  `source ./scripts/activate`

If you are using [pyenv](https://github.com/pyenv/pyenv)

2a. Create a virtualenv

```
    pyenv virtualenv airtime-disbursal
```
2b. Activate the virtualenv

```
pyenv activate airtime-disbursal
```

3. Change into the working folder.

    ```
    cd Automated-Airtime-Disbursal
   ```

4. Create a `.env` file and add your credentials

   ```
   touch .env 
   ```

OR Copy the included example

``` 
cp .env-example .env 
```
5. Add your credentials to the .env file

6. Install the required dependencies
   ```
   pip install -r requirements
   ```
   
7. Edit the script. Change the `airtime_sheet_name` variable
   
8. Run the script 
    ```python
    python airtime_disbursal.py
    ```