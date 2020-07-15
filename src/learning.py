from fastapi import FastAPI
from enum import Enum # makes code easier to maintain and endpoints have more efficient checks

###################
# predefined params
###################

# enum base class is for fixed/predefined values/choices like radio boxes/dropdown.
# str base class is so docs know that the endpoint type should be of type str.
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
# with type hints, fastapi gives auto data conversion and validation.
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet: # enum member comparision
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet": # enum member's actual value comparision
        return {"model_name": model_name, "message": "LeCNN all the images"}
    # on return of an enum member, it gets converted to its .value before returning them to the client.
    return {"model_name": model_name, "message": "Have some residuals"}

##############
# query params
##############
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/someparams/")
# setting the params as int type parses them as int, into the function.
async def get_some_params(start: int = 0, range_val: int = 10):
    return fake_items_db[start: start + range_val]

# for optional params you can use async def my_func(my_optional_param: Optional[str] = None):
# you can also convert 0/1 query params into bool type using async def my_func(my_param: bool = False):
# works for: 1/0, True/False, true/false, on/off, On/Off, yes/no, Yes/No
# can also use Enums with predefined query params too.

##############
# request body
##############
