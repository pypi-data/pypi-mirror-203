# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from ..types import shared
from .._models import BaseModel

__all__ = ["TypeEnumsResponse"]


class TypeEnumsResponse(BaseModel):
    currency: shared.Currency

    my_problematic_enum: Literal["123_FOO", "30%"]

    number_enum: Literal[200, 201, 404, 403]
