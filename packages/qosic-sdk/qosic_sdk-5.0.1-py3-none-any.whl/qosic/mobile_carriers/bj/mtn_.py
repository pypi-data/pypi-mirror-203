from __future__ import annotations

from dataclasses import dataclass, field

from qosic.mobile_carriers.utils import (
    generic_reference_factory,
    handle_common_errors,
)
from ...utils import Payer, Result

MTN_PAYMENT_PATH = "/QosicBridge/user/requestpayment"
MTN_PAYMENT_STATUS_PATH = "/QosicBridge/user/gettransactionstatus"
MTN_PREFIXES = ["51", "52", "53", "61", "62", "66", "67", "69", "90", "91", "96", "97"]
MTN_REFUND_PATH = "/QosicBridge/user/refund"


@dataclass(frozen=True)
class RequestParams:
    path: str
    method: str
    body: dict | None = None


@dataclass(frozen=True)
class MTN:
    id: str
    step: int = 10
    timeout: int = 60 * 2
    max_tries: int | None = None
    allowed_prefixes: list[str] = field(default_factory=lambda: MTN_PREFIXES)
    reference_factory: callable = generic_reference_factory

    def get_pay_request_params(self, payer: Payer) -> RequestParams:
        body = payer.to_qos_compliant_payment_request_body(self)
        return RequestParams(method="post", path=MTN_PAYMENT_PATH, body=body)

    def handle_pay_response(self, response: dict[str, str], payer: Payer) -> Result:
        handle_common_errors(response, provider=self, payer=payer)

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
