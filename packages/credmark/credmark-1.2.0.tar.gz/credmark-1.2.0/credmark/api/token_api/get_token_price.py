from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, Union

import httpx

if TYPE_CHECKING:
    from ...client import Credmark

from typing import Dict, Union

from ... import errors
from ...models.get_token_price_align import GetTokenPriceAlign
from ...models.get_token_price_src import GetTokenPriceSrc
from ...models.token_error_response import TokenErrorResponse
from ...models.token_price_response import TokenPriceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    token_address: str,
    *,
    quote_address: Union[Unset, None, str] = UNSET,
    block_number: Union[Unset, None, float] = UNSET,
    timestamp: Union[Unset, None, float] = UNSET,
    src: Union[Unset, None, GetTokenPriceSrc] = GetTokenPriceSrc.DEX,
    align: Union[Unset, None, GetTokenPriceAlign] = UNSET,
    client: "Credmark",
) -> Dict[str, Any]:
    url = "{}/v1/tokens/{chainId}/{tokenAddress}/price".format(
        client.base_url, chainId=chain_id, tokenAddress=token_address
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["quoteAddress"] = quote_address

    params["blockNumber"] = block_number

    params["timestamp"] = timestamp

    json_src: Union[Unset, None, str] = UNSET
    if not isinstance(src, Unset):
        json_src = src.value if src else None

    params["src"] = json_src

    json_align: Union[Unset, None, str] = UNSET
    if not isinstance(align, Unset):
        json_align = align.value if align else None

    params["align"] = json_align

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


def _parse_response(*, client: "Credmark", response: httpx.Response) -> TokenPriceResponse:
    if response.status_code == HTTPStatus.OK:
        response_200 = TokenPriceResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = TokenErrorResponse.from_dict(response.json())

        raise errors.CredmarkError(response.status_code, response.content, response_400)
    raise errors.CredmarkError(response.status_code, response.content)


def _build_response(*, client: "Credmark", response: httpx.Response) -> Response[TokenPriceResponse]:
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
    quote_address: Union[Unset, None, str] = UNSET,
    block_number: Union[Unset, None, float] = UNSET,
    timestamp: Union[Unset, None, float] = UNSET,
    src: Union[Unset, None, GetTokenPriceSrc] = GetTokenPriceSrc.DEX,
    align: Union[Unset, None, GetTokenPriceAlign] = UNSET,
    client: "Credmark",
) -> Response[TokenPriceResponse]:
    """Get token price data

     Returns price data for a token.

    Args:
        chain_id (float):
        token_address (str):
        quote_address (Union[Unset, None, str]):
        block_number (Union[Unset, None, float]):
        timestamp (Union[Unset, None, float]):
        src (Union[Unset, None, GetTokenPriceSrc]):  Default: GetTokenPriceSrc.DEX.
        align (Union[Unset, None, GetTokenPriceAlign]):

    Raises:
        errors.CredmarkError: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenPriceResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        token_address=token_address,
        client=client,
        quote_address=quote_address,
        block_number=block_number,
        timestamp=timestamp,
        src=src,
        align=align,
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
    quote_address: Union[Unset, None, str] = UNSET,
    block_number: Union[Unset, None, float] = UNSET,
    timestamp: Union[Unset, None, float] = UNSET,
    src: Union[Unset, None, GetTokenPriceSrc] = GetTokenPriceSrc.DEX,
    align: Union[Unset, None, GetTokenPriceAlign] = UNSET,
    client: "Credmark",
) -> TokenPriceResponse:
    """Get token price data

     Returns price data for a token.

    Args:
        chain_id (float):
        token_address (str):
        quote_address (Union[Unset, None, str]):
        block_number (Union[Unset, None, float]):
        timestamp (Union[Unset, None, float]):
        src (Union[Unset, None, GetTokenPriceSrc]):  Default: GetTokenPriceSrc.DEX.
        align (Union[Unset, None, GetTokenPriceAlign]):

    Raises:
        errors.CredmarkError: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenPriceResponse]
    """

    return sync_detailed(
        chain_id=chain_id,
        token_address=token_address,
        client=client,
        quote_address=quote_address,
        block_number=block_number,
        timestamp=timestamp,
        src=src,
        align=align,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    token_address: str,
    *,
    quote_address: Union[Unset, None, str] = UNSET,
    block_number: Union[Unset, None, float] = UNSET,
    timestamp: Union[Unset, None, float] = UNSET,
    src: Union[Unset, None, GetTokenPriceSrc] = GetTokenPriceSrc.DEX,
    align: Union[Unset, None, GetTokenPriceAlign] = UNSET,
    client: "Credmark",
) -> Response[TokenPriceResponse]:
    """Get token price data

     Returns price data for a token.

    Args:
        chain_id (float):
        token_address (str):
        quote_address (Union[Unset, None, str]):
        block_number (Union[Unset, None, float]):
        timestamp (Union[Unset, None, float]):
        src (Union[Unset, None, GetTokenPriceSrc]):  Default: GetTokenPriceSrc.DEX.
        align (Union[Unset, None, GetTokenPriceAlign]):

    Raises:
        errors.CredmarkError: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenPriceResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        token_address=token_address,
        client=client,
        quote_address=quote_address,
        block_number=block_number,
        timestamp=timestamp,
        src=src,
        align=align,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    token_address: str,
    *,
    quote_address: Union[Unset, None, str] = UNSET,
    block_number: Union[Unset, None, float] = UNSET,
    timestamp: Union[Unset, None, float] = UNSET,
    src: Union[Unset, None, GetTokenPriceSrc] = GetTokenPriceSrc.DEX,
    align: Union[Unset, None, GetTokenPriceAlign] = UNSET,
    client: "Credmark",
) -> TokenPriceResponse:
    """Get token price data

     Returns price data for a token.

    Args:
        chain_id (float):
        token_address (str):
        quote_address (Union[Unset, None, str]):
        block_number (Union[Unset, None, float]):
        timestamp (Union[Unset, None, float]):
        src (Union[Unset, None, GetTokenPriceSrc]):  Default: GetTokenPriceSrc.DEX.
        align (Union[Unset, None, GetTokenPriceAlign]):

    Raises:
        errors.CredmarkError: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenPriceResponse]
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            token_address=token_address,
            client=client,
            quote_address=quote_address,
            block_number=block_number,
            timestamp=timestamp,
            src=src,
            align=align,
        )
    ).parsed
