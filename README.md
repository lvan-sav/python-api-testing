## API Test automation for [FavQs](https://favqs.com/) website implemented via pytest and requests

#### Content

1. Requirements
2. Get started
3. Project content

#### Requirements
* Python 3.12^
* App token for FavQs website. See [documentation](https://favqs.com/api/)

#### Get started
1. Download or fork this repo
2. Create virtual environment and activate it
3. Install required packages via `pip install -r requirements.txt`
4. Create `.env` file and add API key from FavQs like follow example: 
```text
API_KEY=*Your API key*
```
5. Run tests by `pytest tests`

#### Project content

* `tests` - contains all modules required for test execution
* `tests/test_user_api` - contains tests fot verify API of user management feature
* `tests/api` - contains modules to execute basic requests to the API
* `tests/helper` - contains basic functions to generate test data
* `tests/conftest.py` - contains besic fixtures for tests
