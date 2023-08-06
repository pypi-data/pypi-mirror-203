from pathlib import Path
from typing import NoReturn

import requests

__all__ = ["get_cartoon"]


class NetworkError(Exception):
    """Error raised when a network error occurs."""


def get_cartoon(
    struct_format: str,
    structure: str,
    output_path: str,
) -> NoReturn:
    """Get a cartoon image from the GlyConnect API.

    Args:
        struct_format (str): The format of the structure. One of "glycoct" and "gws".
        structure (str): The structure.
        output_path (str): The path to save the image to.

    Raises:
        ValueError: If the input args are invalid.
        NetworkError: If a network error occurs.
    """
    valid_struct_formats = ("glycoct", "gws")
    if struct_format not in valid_struct_formats:
        raise ValueError(f"Invalid struct_format. Must be one of {valid_struct_formats}")

    valid_img_formats = (".png", ".svg", ".jpg", ".bmp")
    if Path(output_path).suffix not in valid_img_formats:
        raise ValueError(f"Invalid output_path. Must be one of {valid_img_formats}")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    url = f"https://glyconnect.expasy.org/api/structures/cartoon/{struct_format}"
    data = {
        struct_format: structure,
        "notation": "cfg",
        "format": Path(output_path).suffix[1:],  # remove the dot
    }
    try:
        response = requests.post(url, json=data, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise NetworkError(e)

    with open(output_path, "wb") as f:
        f.write(response.content)
