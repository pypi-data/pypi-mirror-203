from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, Union

import httpx

if TYPE_CHECKING:
    from ...client import Credmark

from typing import Dict, Union

from ... import errors
from ...models.get_token_price_historical_src import GetTokenPriceHistoricalSrc
from ...models.token_error_response import TokenErrorResponse
from ...models.token_price_historical_response import TokenPriceHistoricalResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    token_address: str,
    *,
    start_block_number: Union[Unset, None, float] = UNSET,
    end_block_number: Union[Unset, None, float] = UNSET,
    block_interval: Union[Unset, None, float] = UNSET,
    start_timestamp: Union[Unset, None, float] = UNSET,
    end_timestamp: Union[Unset, None, float] = UNSET,
    time_interval: Union[Unset, None, float] = UNSET,
    quote_address: Union[Unset, None, str] = UNSET,
    src: Union[Unset, None, GetTokenPriceHistoricalSrc] = GetTokenPriceHistoricalSrc.DEX,
    client: "Credmark",
) -> Dict[str, Any]:
    url = "{}/v1/tokens/{chainId}/{tokenAddress}/price/historical".format(
        client.base_url, chainId=chain_id, tokenAddress=token_address
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["startBlockNumber"] = start_block_number

    params["endBlockNumber"] = end_block_number

    params["blockInterval"] = block_interval

    params["startTimestamp"] = start_timestamp

    params["endTimestamp"] = end_timestamp

    params["timeInterval"] = time_interval

    params["quoteAddress"] = quote_address

    json_src: Union[Unset, None, str] = UNSET
    if not isinstance(src, Unset):
        json_src = src.value if src else None

    params["src"] = json_src

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: "Credmark", response: httpx.Response) -> TokenPriceHistoricalResponse:
    if response.status_code == HTTPStatus.OK:
        response_200 = TokenPriceHistoricalResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = TokenErrorResponse.from_dict(response.json())

        raise errors.CredmarkError(response.status_code, response.content, response_400)
    raise errors.CredmarkError(response.status_code, response.content)


def _build_response(*, client: "Credmark", response: httpx.Response) -> Response[TokenPriceHistoricalResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chain_id: float,
    token_address: str,
    *,
    start_block_number: Union[Unset, None, float] = UNSET,
    end_block_number: Union[Unset, None, float] = UNSET,
    block_interval: Union[Unset, None, float] = UNSET,
    start_timestamp: Union[Unset, None, float] = UNSET,
    end_timestamp: Union[Unset, None, float] = UNSET,
    time_interval: Union[Unset, None, float] = UNSET,
    quote_address: Union[Unset, None, str] = UNSET,
    src: Union[Unset, None, GetTokenPriceHistoricalSrc] = GetTokenPriceHistoricalSrc.DEX,
    client: "Credmark",
) -> Response[TokenPriceHistoricalResponse]:
    """Get historical price

     Returns historical price data for a token.

    Args:
        chain_id (float):
        token_address (str):
        start_block_number (Union[Unset, None, float]):
        end_block_number (Union[Unset, None, float]):
        block_interval (Union[Unset, None, float]):
        start_timestamp (Union[Unset, None, float]):
        end_timestamp (Union[Unset, None, float]):
        time_interval (Union[Unset, None, float]):
        quote_address (Union[Unset, None, str]):
        src (Union[Unset, None, GetTokenPriceHistoricalSrc]):  Default:
            GetTokenPriceHistoricalSrc.DEX.

    Raises:
        errors.CredmarkError: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenPriceHistoricalResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        token_address=token_address,
        client=client,
        start_block_number=start_block_number,
        end_block_number=end_block_number,
        block_interval=block_interval,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        time_interval=time_interval,
        quote_address=quote_address,
        src=src,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    token_address: str,
    *,
    start_block_number: Union[Unset, None, float] = UNSET,
    end_block_number: Union[Unset, None, float] = UNSET,
    block_interval: Union[Unset, None, float] = UNSET,
    start_timestamp: Union[Unset, None, float] = UNSET,
    end_timestamp: Union[Unset, None, float] = UNSET,
    time_interval: Union[Unset, None, float] = UNSET,
    quote_address: Union[Unset, None, str] = UNSET,
    src: Union[Unset, None, GetTokenPriceHistoricalSrc] = GetTokenPriceHistoricalSrc.DEX,
    client: "Credmark",
) -> TokenPriceHistoricalResponse:
    """Get historical price

     Returns historical price data for a token.

    Args:
        chain_id (float):
        token_address (str):
        start_block_number (Union[Unset, None, float]):
        end_block_number (Union[Unset, None, float]):
        block_interval (Union[Unset, None, float]):
        start_timestamp (Union[Unset, None, float]):
        end_timestamp (Union[Unset, None, float]):
        time_interval (Union[Unset, None, float]):
        quote_address (Union[Unset, None, str]):
        src (Union[Unset, None, GetTokenPriceHistoricalSrc]):  Default:
            GetTokenPriceHistoricalSrc.DEX.

    Raises:
        errors.CredmarkError: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenPriceHistoricalResponse]
    """

    return sync_detailed(
        chain_id=chain_id,
        token_address=token_address,
        client=client,
        start_block_number=start_block_number,
        end_block_number=end_block_number,
        block_interval=block_interval,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        time_interval=time_interval,
        quote_address=quote_address,
        src=src,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    token_address: str,
    *,
    start_block_number: Union[Unset, None, float] = UNSET,
    end_block_number: Union[Unset, None, float] = UNSET,
    block_interval: Union[Unset, None, float] = UNSET,
    start_timestamp: Union[Unset, None, float] = UNSET,
    end_timestamp: Union[Unset, None, float] = UNSET,
    time_interval: Union[Unset, None, float] = UNSET,
    quote_address: Union[Unset, None, str] = UNSET,
    src: Union[Unset, None, GetTokenPriceHistoricalSrc] = GetTokenPriceHistoricalSrc.DEX,
    client: "Credmark",
) -> Response[TokenPriceHistoricalResponse]:
    """Get historical price

     Returns historical price data for a token.

    Args:
        chain_id (float):
        token_address (str):
        start_block_number (Union[Unset, None, float]):
        end_block_number (Union[Unset, None, float]):
        block_interval (Union[Unset, None, float]):
        start_timestamp (Union[Unset, None, float]):
        end_timestamp (Union[Unset, None, float]):
        time_interval (Union[Unset, None, float]):
        quote_address (Union[Unset, None, str]):
        src (Union[Unset, None, GetTokenPriceHistoricalSrc]):  Default:
            GetTokenPriceHistoricalSrc.DEX.

    Raises:
        errors.CredmarkError: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenPriceHistoricalResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        token_address=token_address,
        client=client,
        start_block_number=start_block_number,
        end_block_number=end_block_number,
        block_interval=block_interval,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        time_interval=time_interval,
        quote_address=quote_address,
        src=src,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    token_address: str,
    *,
    start_block_number: Union[Unset, None, float] = UNSET,
    end_block_number: Union[Unset, None, float] = UNSET,
    block_interval: Union[Unset, None, float] = UNSET,
    start_timestamp: Union[Unset, None, float] = UNSET,
    end_timestamp: Union[Unset, None, float] = UNSET,
    time_interval: Union[Unset, None, float] = UNSET,
    quote_address: Union[Unset, None, str] = UNSET,
    src: Union[Unset, None, GetTokenPriceHistoricalSrc] = GetTokenPriceHistoricalSrc.DEX,
    client: "Credmark",
) -> TokenPriceHistoricalResponse:
    """Get historical price

     Returns historical price data for a token.

    Args:
        chain_id (float):
        token_address (str):
        start_block_number (Union[Unset, None, float]):
        end_block_number (Union[Unset, None, float]):
        block_interval (Union[Unset, None, float]):
        start_timestamp (Union[Unset, None, float]):
        end_timestamp (Union[Unset, None, float]):
        time_interval (Union[Unset, None, float]):
        quote_address (Union[Unset, None, str]):
        src (Union[Unset, None, GetTokenPriceHistoricalSrc]):  Default:
            GetTokenPriceHistoricalSrc.DEX.

    Raises:
        errors.CredmarkError: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenPriceHistoricalResponse]
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            token_address=token_address,
            client=client,
            start_block_number=start_block_number,
            end_block_number=end_block_number,
            block_interval=block_interval,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            time_interval=time_interval,
            quote_address=quote_address,
            src=src,
        )
    ).parsed
