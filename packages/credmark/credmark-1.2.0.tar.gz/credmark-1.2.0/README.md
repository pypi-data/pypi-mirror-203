# Credmark

A client library for accessing Credmark Gateway

## Installation

Install using pip:

```bash
pip install credmark
```

## Usage

First, create an instance of `Credmark` client. In order to access the API, you will need an API key. Information about getting a key is available in our [API setup guide](https://docs.credmark.com/api-how-to-guide/).

```python
from credmark import Credmark

client = Credmark(api_key="<Your API Key>")
```

Alternatively you can also set the API key in the OS environment and the client will automatically pick from it.

```bash
export CREDMARK_API_KEY=<Your API Key>
```

```python
from credmark import Credmark

client = Credmark() # It reads the api key from CREDMARK_API_KEY env var
```

Now call your endpoint by tag and use your models:

```python
metadata = client.token_api.get_token_metadata(1, "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9")

print(metadata)
# TokenMetadataResponse(chain_id=1, block_number=17044112, block_timestamp=1681459199, token_address='0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9', name='Aave Token', symbol='AAVE', decimals=18, additional_properties={})
```

Or do the same thing with an async version:

```python
import asyncio

async def get_metadata():
    metadata = await client.token_api.get_token_metadata_async(1, "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9")
    print(metadata)
    # TokenMetadataResponse(chain_id=1, block_number=17044112, block_timestamp=1681459199, token_address='0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9', name='Aave Token', symbol='AAVE', decimals=18, additional_properties={})

loop = asyncio.get_event_loop()
loop.run_until_complete(get_metadata())
loop.close()
```

## Run a model

You can run a model using DeFi API:

```python
from credmark.models import RunModelDto

result = client.defi_api.run_model(
    json_body=RunModelDto(
        chain_id=1, 
        block_number="latest", 
        slug="price.quote", 
        input={"base": {"symbol": "AAVE"}, "prefer": "dex"}
    ),
)

print(result.chain_id, result.block_number)
# 1 17044112
print(result.slug, result.version)
# price.quote 1.11
print(result.output)
# {'src': 'dex|uniswap-v2,sushiswap,uniswap-v3|Non-zero:9|Zero:2|4.0', 'price': 82.19716419870656, 'quoteAddress': '0x0000000000000000000000000000000000000348'}
```

## Handling Errors

Each method can raise:

- errors.CredmarkError: If the server returns a non 2xx status code.
- httpx.TimeoutException: If the request takes longer than Client.timeout.

```python
from httpx import TimeoutException
from credmark.errors import CredmarkError

try:
    metadata = client.token_api.get_token_metadata(1, "WRONG TOKEN ADDRESS")
except CredmarkError as e:
    print(e.status_code)
    # 400
    print(e.parsed)
    # TokenErrorResponse(status_code=400, error='Bad Request', message=['Invalid token address'], additional_properties={})
    print(str(e.content, "UTF-8"))
    # {"statusCode":400,"message":["Invalid token address"],"error":"Bad Request"}
except TimeoutException:
    print('timeout occurred')
```

## Available APIs

- [Token API](https://github.com/credmark/credmark-sdk-py/blob/main/credmark/docs/TokenAPI.md)
- [DeFi API](https://github.com/credmark/credmark-sdk-py/blob/main/credmark/docs/DeFiAPI.md)
- [Utilities API](https://github.com/credmark/credmark-sdk-py/blob/main/credmark/docs/Utilities.md)

## Things to know

1. Every path/method combo has four functions:
    1. default: Blocking request that returns parsed data (if successful) or `None`
    2. `async`: Like default but async instead of blocking

2. All path/query params, and bodies become method arguments.

## Advanced Usage

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = Credmark(
    base_url="https://internal_api.example.com", 
    api_key="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = Credmark(
    base_url="https://internal_api.example.com", 
    api_key="SuperSecretToken", 
    verify_ssl=False
)
```

There are more settings on the generated `Credmark` class which let you control more runtime behavior, check out the docstring on that class for more info.
