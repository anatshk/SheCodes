"""
Example for testing blogpost
"""


def calculate_discount(customer_loyalty, prev_purchases_num, prev_purchases_amount, curr_purchase_amount):
    """
    Calculate the discount we should give a specific customer, based on their loyalty,
    number and amount of previous purchases and amount of current purchase.

    :param customer_loyalty: integer, number between 1-5, 1 being a new customer and 5 being a loyal customer
    :param prev_purchases_num: integer, number of previous purchases by customer
    :param prev_purchases_amount: float, total amount (in USD) spent by the customer in the past
    :param curr_purchase_amount: float,  total amount (in USD) spent by the customer in current purchase
    :return: float, 0-100, percentage of discount given to current purchase
    """

    # TODO: write code here

    return discount_percentage