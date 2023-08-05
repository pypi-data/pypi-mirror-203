"""Response extensions for SOAP."""

from typing import NoReturn, TypeVar

from combadge.core.response import ErrorResponse


class BaseSoapFault(ErrorResponse):
    """
    SOAP Fault model.

    Notes:
        - This class matches the SOAP Fault specification.
          For custom errors returned in a SOAP response body (such as `<error>` tag),
          subclass the `ErrorResponse`.

    See Also:
        - https://www.w3.org/TR/2000/NOTE-SOAP-20000508/#_Toc478383507
    """

    code: str
    message: str

    def raise_for_result(self) -> NoReturn:
        """Raise the derived error for this fault."""
        raise self.Error(self)


SoapFaultT = TypeVar("SoapFaultT", bound=BaseSoapFault)
"""Specific SOAP Fault model type."""
