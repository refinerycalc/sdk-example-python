from initialization import RefineryCalc


def print_output(name, output_type):
    print(name)
    for i in range(len(name)): print("-",end='')
    print('')
    for output in output_type:
        print(f"name: {output.name} , value: {output.value} {output.uom}")
    print('')

if __name__ == "__main__":
    client = RefineryCalc()
    simulation_id = "10aef717-d138-4a01-b366-2afc8cdf077a"
    response = client.simulations.v1_simulations_id_output_get(simulation_id)

    for refinery in response.refineries:
        print("-----------------------------------")
        print(refinery.refinery_name)
        print("-----------------------------------")

        # Expense Factors
        expense_factors = refinery.outputs.expense_factors
        print_output("Expense Factors", expense_factors)

        # balance output
        balance = refinery.outputs.balance
        print_output("Balance", balance)

        # complexity output
        complexity = refinery.outputs.complexity
        print_output("Complexity", complexity)

        # Product Pricing
        product_pricing = refinery.outputs.product_pricing
        print_output("Product Pricing", product_pricing)

        # Product Output
        products = refinery.outputs.products
        print_output("Products", products)

        # Sustainability
        sustainability = refinery.outputs.sustainability
        print_output("Sustainability", sustainability)

        # unit balance
        unit_balance = refinery.outputs.unit_balance
        print_output("Unit Balance", unit_balance)


