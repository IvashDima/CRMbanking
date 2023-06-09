
# for https://api.agify.io/?name= and https://api.genderize.io/?name=

UNAUTHERIZED = f"Error: 401 - Unautherized. Error text: Invalid API key"
PAYMENT_REQUIRED = f"Error: 402 - Payment Required. Error text: Subscription is not active"
UNPROCESSABLE_ENTITY = f"Error: 422 - Unprocessable Entity. Error text: Missing 'name' parameter"
TOO_MANY_REQUESTS = f"Error: 429 - Too Many Requests. Error text: Request limit reached"
