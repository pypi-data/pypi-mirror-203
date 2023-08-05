from typing import Any, Dict

from magento.types import Order

__all__ = (
    'is_order_on_hold',
    'is_order_cash_on_delivery',
    'get_order_shipping_address',
)


def is_order_on_hold(order: Order):
    """Test if an order is on hold."""
    return order["status"] == "holded" or "hold_before_state" in order


def is_order_cash_on_delivery(order: Order):
    """Test if an order is paid with 'cash-on-delivery'."""
    # From Magento\OfflinePayments\Model\Cashondelivery::PAYMENT_METHOD_CASHONDELIVERY_CODE
    return order["payment"]["method"] == 'cashondelivery'


def get_order_shipping_address(order: Order) -> Dict[str, Any]:
    """
    Return the first shipping address of an order.
    Note the returned dict is a reference, so if you modify it, it modifies the order.
    Make a copy if you want to modify the address without affecting the order.
    """
    return order["extension_attributes"]["shipping_assignments"][0]["shipping"]["address"]
