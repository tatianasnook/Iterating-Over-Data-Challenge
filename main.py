def calculate_total_sales(sales_totals):
    if not sales_totals:
        return 0.0
    total = 0
    for value in sales_totals.values():
        total += value['quantity'] * value['price']
    return total

def calculate_average_sales(sales_totals):
    if not sales_totals:
        return 0.0
    total = calculate_total_sales(sales_totals)
    average = total / len(sales_totals)
    return average

def filter_to_better_than_average_sales(sales_totals):
    if not sales_totals:
        return {}
    average = calculate_average_sales(sales_totals)
    above_average = {}
    for key, value in sales_totals.items():
        if value['quantity'] * value['price'] > average:
            above_average[key] = value
    return above_average

    
def ninety_nine_bottles(count, beverage):
    lines = []
    if count > 2:
        for number in range(count, -1, -1):
            lines.append(f'{number} bottles of {beverage} on the wall, {number} bottles of {beverage}')
            lines.append(f"If one of those bottles should happen to fall, {number - 1} bottle of pop on the wall")
                         
    return len(lines)