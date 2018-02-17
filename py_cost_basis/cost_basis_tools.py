"""
"""


def average_cost_basis(sells, buys):
    """
    """
    return "hello world: average_cost_basis"


def lifo_cost_basis(sells, buys):
    """
    """
    return "hello world: lifo_cost_basis"


def fifo_cost_basis(sells, buys):
    """
    """
    return "hello world: fifo_cost_basis"


def high_cost_first_out_cost_basis(sells, buys):
    """
    """
    return "hello world: high_cost_first_out_cost_basis"


def low_cost_first_out_cost_basis(sells, buys):
    """
    """
    return "hello world: low_cost_first_out_cost_basis"


def cost_basis(sells, buys, method="LIFO"):
    """
    """

    try:
        return {
            "average": average_cost_basis,
            "LIFO": lifo_cost_basis,
            "FIFO": fifo_cost_basis,
            "HCFO": high_cost_first_out_cost_basis,
            "LCFO": low_cost_first_out_cost_basis,
        }[method](sells, buys)

    except:
        raise
