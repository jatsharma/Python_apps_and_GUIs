# A particular state in XYZ country charges taxes on its citizen's income. These tax rates varies '
# from person to person depending on income and age and hence they have to pay different taxes.
# Here are the tax rules laid by the government which states the percent tax for category of individual.
#
# For taxpayers under 60 years of age:
# annual income up to: $20,000 -> No tax
# annual income from $20,001 to $50,000 -> 20% tax
# annual income from $50,001 to $100,000 -> 30% tax
# annual income above $100,001 -> 40% tax
#
# For taxpayers above 60 years of age:
# annual income up to: $20,000 -> No tax
# annual income from $20,001 to $50,000 -> 10% tax
# annual income from $50,001 to $100,000 -> 20% tax
# annual income above $100,001 -> 30% tax
#
# Level 1: Build a tax calculator which accepts the age and total income of an individual and calculates the total
# tax to be paid.
#
# Level 2:
# 1.Design a GUI for the above code.
# 2. Try to add additional category of taxpayers such as businesses and charge them 7.5% additional taxes
# (considering taxes for age group below 60).


def cal(age, income):
    if age > 60:
        if income < 20001:
            return 0
        elif 20000 < income < 50001:
            tax = (10/100) * income
            return tax
        elif 50000 < income < 100001:
            tax = (20/100) * income
            return tax
        elif income > 100000:
            tax = (30/100) * income
            return tax
        else:
            return 0
    elif age < 60:
        if income < 20001:
            return 0
        elif 20000 < income < 50001:
            tax = (20/100) * income
            return tax
        elif 50000 < income < 100001:
            tax = (30/100) * income
            return tax
        elif income > 100000:
            tax = (40/100) * income
            return tax
        else:
            return 0
    else:
        return 0

