from __future__ import annotations

from typing import Protocol

from .utils import Result, Payer


# class MobileCarrier(Protocol):
#     id: str
#     allowed_prefixes: list[str]
#     reference_factory: callable[[Payer], str]
#
#     def pay(self, http_client: Client, *, payer: Payer) -> Result:
#         ...
#
#     def refund(self, http_client: Client, *, reference: str, phone: str) -> Result:
#         ...


class MobileCarrier(Protocol):
    id: str
    allowed_prefixes: list[str]
    reference_factory: callable[[Payer], str]

    def get_pay_request_params(self, payer: Payer) -> dict[str, str]:
        ...

    def handle_pay_response(self, response: dict[str, str]) -> Result:
        ...

    def get_pay_transaction_status_request_params(
        self, reference: str
    ) -> dict[str, str]:
        ...

    def handle_pay_transaction_status_response(
        self, response: dict[str, str]
    ) -> Result:
        ...

    def get_refund_request_params(self, reference: str, phone: str) -> dict[str, str]:
        ...

    def handle_refund_response(self, response: dict[str, str]) -> Result:
        ...

    def get_refund_transaction_status_request_params(
        self, reference: str
    ) -> dict[str, str]:
        ...

    def handle_refund_transaction_status_response(
        self, response: dict[str, str]
    ) -> Result:
        ...
