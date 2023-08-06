# SQAPI

`sqapi` is a python package that simplifies interactions with the 
[SQUIDLE+ API](https://squidle.org/api/help?template=api_help_page.html).
It can be used to integrate automated labelling from machine learning algorithms and plenty other cool things.

### Installation
To install the `sqapi` module, you can use `pip`
```shell
pip install sqapi 
```

### What is this?
The `sqapi` module helps to build the `HTTP` requests that are sent to the [SQUIDLE+](squidle.org) `API`. These are 
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

For more information about structuring queries, check out the [Making API queries](https://squidle.org/api/help?template=api_help_page.html#api_query)
section of the SQ+ API documentation page.

Instantiating `sqapi` without an API key argument will prompt for a user login, i.e.:
```python
sqapi = SQAPI(host=<HOST>, verbosity=2)  # instantiate the sqapi module
```

You can also use it to apply built-in templates to the data that comes out of the API:
```python
r.template(<TEMPLATE>)               # format the output of the request using an inbuilt HTML template
html = r.execute().text              # perform the request & return result as text (eg: for html)
```

> **IMPORTANT:** in order to proceed, you will need a user account on [SQUIDLE+](https://squidle.org). You will also 
> need to activate your API key.

## Examples
### Random annotation BOT
This is an example of an automated labelling bot that selects random class labels to assign to points.
It provides terrible suggestions, however it provides a simple boiler-plate example of how to integrate a
Machine Learning algorithm for label suggestions.

Set up the environment and a mini project
```shell
mkdir sqbot_demo && cd sqbot_demo   # make a directory
virtualenv -p python3 env           # create a virtual environment
source env/bin/activate             # activate it
pip install sqapi  # install sqapi
```

#### 1. Create a bot class
In this example, we'll create an automated classifier that suggests random label suggestions for an annotation_set. 
It uses the `Annotator` class from the `sqapi.annotate` module, which does most of the heavy-lifting. The implementation
of the classifier is relatively straight forward.
In your project directory, create a file named `run_bot.py`:

```python
# run_bot.py
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
    # Get the cli arguments from the Class __init__ function signatures
    parser = create_parser(RandoBOT)  # convenient method to build a parser from the bot class
    
    # Add an extra argument to the parser to get an annotation_set id to classify
    parser.add_argument('--annotation_set_id', help="Process annotation_set with specific ID", type=int)
    
    # Instantiate the bot class
    args = parser.parse_args()
    bot = RandoBOT(**vars(args))
    
    # Initialise the request for the annotation_set that you want classified
    # update the ID to the ID you want
    r = bot.sqapi.get("/api/annotation_set").filter(name="id", op="in", val=args.annotation_set_id)

    bot.start(r)
```

The `create_parser` method is a convenience tool that allows you to build a command line parser from the  
signature of the `__init__` methods for the RandoBot class and all inherited base classes (eg: Annotator).

This allows you to pass arguments from the command line, and helps to show how to use it:
```shell
# from the command line, run:
python run_bot.py --help
```

It will show you all the required parameters from the base class `Annotator` as well as any extra arguments added to the 
`__init__` method of the `RandoBot` class. Parameter descriptions come from the comment block.

#### 2. Create a Label Mapper File
Before you run it, you also need to create a label map file to pass into the `--label_map_file` argument. 
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

#### 3. Run your bot
Now you're ready to run your classifier `RandoBot`, by simply executing this from the command line:
```shell
python run_bot.py --label_map_file rando_bot_label_map.json --annotation_set_id=55 --poll_delay -1 --email_results
```

This will run the classifier once on the annotation_set with an `ID=55`
and attempt to provide automated suggestions on the labels it contains using random class allocations and probabilities. 
It will run once (as defined by the `--poll_delay=-1` parameter) and it will send an email to the owner the
annotation_set once complete.

Now all that's left is for you to make the labels and probabilities real, and bob's your uncle,
you've made an automated classifier.

The [examples](https://bitbucket.org/ariell/pysq/src/master/examples/) directory has some examples that you can use and/or adapt for 
your purposes. Specifically with regard to classifiers:

1. **[demo_randobot.py](https://bitbucket.org/ariell/pysq/src/master/examples/bots/demo_randobot.py)**: same as example above, but with additional command line 
   arguments for filtering annotation_sets and to keep running as a service.
2. **[keras_cnn_bot.py](https://bitbucket.org/ariell/pysq/src/master/examples/bots/keras_cnn_bot.py)**: a real classifier that uses a tensor_flow/keras model for 
   classifying points in images. The class received a number of additional parameters that can all be passed in as 
   command line arguments. Run `python keras_cnn_bot.py --help` for more information. This shows an example of how to 
   include additional model-specific arguments along with other parameters, as well as how to process the images and 
   for a real classifier.

