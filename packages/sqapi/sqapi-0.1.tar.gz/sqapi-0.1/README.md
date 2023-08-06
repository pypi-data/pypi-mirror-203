# SQAPI

`sqapi` is a python package that simplifies interactions with the 
[SQUIDLE+ API](https://squidle.org/api/help?template=api_help_page.html).
It can be used to integrate automated labelling from machine learning algorithms and plenty other cool things.

### Installation
To install the `sqapi` module, you can use `pip`
```shell
pip install git+https://ariell@bitbucket.org/ariell/pysq.git 
```

### Why & how
The `sqapi` module helps to build the `HTTP` requests that are sent to the `API`. These are 
`GET`, `POST`, `PATCH` or `DELETE` requests. Setting `verbosity=2` on the `sqapi` module will print the `HTTP` 
requests that are being made.

`sqapi` takes care of authentication, and simplifies the creation of API queries. 
For example:

```python
from sqapi.api import SQAPI

sqapi = SQAPI(host=<HOST>,api_key=<API_KEY>, verbosity=2)  # instantiate the sqapi module
r=sqapi.get(<ENDPOINT>)              # define a get request using a specific endpoint
r.filter(<NAME>,<OPERATORE>,<VALUE>) # define a filter to compare a property with a value using an operator
data = r.execute().json()            # perform the request & return result as JSON dict (don't set template)
```

Instantiating `sqapi` without an API key argument will prompt for a user login, i.e.:
```python
sqapi = SQAPI(host=<HOST>, verbosity=2)  # instantiate the sqapi module
```

You can also use it to apply templates to the data that comes out of the API:
```python
r.template(<TEMPLATE>)               # format the output of the request using an inbuilt HTML template
html = r.execute().text              # perform the request & return result as text (eg: for html)
```

> **IMPORTANT:** in order to proceed, you will need a user account on [SQUIDLE+](https://squidle.org). You will also 
> need to activate your API key.

## Example of AUTO Annotate Bot
Set up the environment and a mini project
```shell
mkdir sqbot_demo && cd sqbot_demo   # make a directory
virtualenv -p python3 env           # create a virtual environment
source env/bin/activate             # activate it
pip install git+https://ariell@bitbucket.org/ariell/pysq.git  # install sqapi
```

In your project directory, create a file named `run_bot.py` with the following content:

```python
import random
from sqapi.annotate import Annotator
from sqapi.request import query_filter as qf
from sqapi.helpers import cli_init, create_parser
from sqapi.media import SQMediaObject


class RandoBOT(Annotator):
    def __init__(self, user_group_id: int, **annotator_args):
        """
        Demo classifier that creates random class allocations and probabilities
        :param user_group_id: the ID of the user_group that you wish to classify
        """
        super().__init__(**annotator_args)  # calls base class with all required inputs
        self.user_group_id = user_group_id  # example of an extra parameter added to the init
        self.possible_codes = ["ECK", "ASC", "SUB"]

    def classify_point(self, mediaobj: SQMediaObject, x, y, t):
        """Overridden method: predict label for x-y point"""
        # image_data = mediaobj.data()            # cv2 image object containing media data
        # media_path = mediaobj.url               # path to media item
        classifier_code = random.sample(self.possible_codes, 1)[0]  # get a random code
        prob = round(random.random(), 2)  # generate a random probability
        # TODO: use the image_data, x and y point position to generate a real label and prob
        return classifier_code, prob


if __name__ == '__main__':
    bot = cli_init(RandoBOT)  # convenience method that initialises the class from command line arguments

    # Initialise the list of annotation_set that you want classified
    # only consider annotation_sets that do not already have suggestions from this user
    r = bot.sqapi.get("/api/annotation_set")
        .filter_not(qf("children", "any", val=qf("user_id", "eq", bot.sqapi.current_user.get("id"))))

    # filter annotation_sets within a nominated user_group 
    # as specified by the extra parameter added to RandoBot.__init__
    r.filter(name="usergroups", op="any", val=dict(name="id", op="eq", val=bot.user_group_id))

    bot.start(r)
```

The `cli_init` method is a convenience tool that allows you to initialise the Class from the command line based on the 
signature of the `__init__` methods for that class and all base classes.

To see the parameters and how to use it from the command line, run the following:
```shell
python run_bot.py --help
```

It will show you all the required parameters from the base class `Annotator` as well as any extra arguments added to the 
`__init__` method of the `RandoBot` class.

You also need to create a label map file to pass into the `--label_map_file` argument. 
This maps the outputs from your classifier to real class labels in the system.

In your project directory, create a file named `rando_bot_label_map.json` 
with the following content:
```json
{
  "ECK": [{"or":[{"name":"vocab_elements","op":"any","val":{"name":"key","op":"eq","val":"214344"}},{"name":"vocab_elements","op":"any","val":{"name":"key","op":"eq","val":"54079009"}}]}],
  "ASC": [{"or":[{"name":"vocab_elements","op":"any","val":{"name":"key","op":"eq","val":"1839"}},{"name":"vocab_elements","op":"any","val":{"name":"key","op":"eq","val":"35000000"}}]}],
  "SUB": [{"name":"vocab_elements","op":"any","val":{"name":"key","op":"eq","val":"82001000"}}]
}
```

Now you're ready to run your classifier RandoBot, by simply executing this from the command line:
```shell
python run_bot.py --label_map_file rando_bot_label_map.json --user_group_id=55 --poll_delay 5 --email_results
```

This will get the list of annotation_sets contained in the user_group with the id of `55`
and attempt to provide automated suggestions on the labels it contains using random class allocations and probabilities. 
It will continue this indefinitely in a loop every 5s ( as defined by the `--poll_delay` parameter) until canceled. 
It will send an email to the owner of every annotation_set that it completes.

Now all that's left is for you to make the labels and probabilities real, and bob's your uncle,
you've made an automated classifier.

