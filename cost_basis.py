



def average_cost_basis(sells, buys):
    """
    """
    pass


def lifo_cost_basis(sells, buys):
    """
    """
    pass


def fifo_cost_basis(sells, buys):
    """
    """
    pass


def high_cost_first_out_cost_basis(sells, buys):
    """
    """
    pass


def low_cost_first_out_cost_basis(sells, buys):
    """
    """
    pass


    

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
    
