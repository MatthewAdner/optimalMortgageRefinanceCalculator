import math
import numpy
from scipy.special import lambertw

def calculateOptimalRate(remaining_mor_principal, years_left_on_mor, current_mor_interest_rate, income_tax_rate, years_remaining_in_house, points_on_new_mor, new_mor_closing_costs, future_cost_discount_rate, inflation_rate_over_new_mor, mor_interest_rate_std_dev):
    psi = calculate_psi(future_cost_discount_rate, points_on_new_mor, mor_interest_rate_std_dev)
    phi = calculate_phi(psi, future_cost_discount_rate, points_on_new_mor, (new_mor_closing_costs / remaining_mor_principal), income_tax_rate)
    
    result = (1 / psi) * (phi + lambertw(-(math.exp(-phi))))
    return(result.real)  # lambertw returns a complex number. this returns only the real component


def calculate_psi(real_discount_rate, expected_real_rate_of_exogenous_mor_repayment, mor_repayment_stddev):
    result = (math.sqrt(2 * (real_discount_rate + expected_real_rate_of_exogenous_mor_repayment))) / mor_repayment_stddev
    return(result)


def calculate_phi(psi, real_discount_rate, expected_real_rate_of_exogenous_mor_repayment, tax_adj_refinancing_cost_to_remaining_mor_value, marginal_tax_rate):
    result = 1 + psi * (real_discount_rate + expected_real_rate_of_exogenous_mor_repayment) * (tax_adj_refinancing_cost_to_remaining_mor_value / (1 - marginal_tax_rate))
    return(result)


def calculate_lambda(mu, i0, tau, pi):
    result = mu + (i0/(math.exp(i0*tau)-1)) + pi
    return(result)