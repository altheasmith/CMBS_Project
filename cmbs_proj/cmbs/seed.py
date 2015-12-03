import csv
import re
from datetime import datetime
from cmbs.models import Deal, Loan, Property, Lease


def main(deal):
	#this line will get the row based on the deal entered, or create a new row if it doesn't exist
	current_deal, created = Deal.objects.get_or_create(deal_name= deal)
	# read the csv files into the program
	loan_reader = csv.DictReader(open("cmbs/{} loan.csv".format(deal)), delimiter="$")
	#property_reader = csv.DictReader(open("cmbs/{} property.csv".format(deal)), delimiter="$")
	#lease_reader = csv.DictReader(open("cmbs/{} lease.csv".format(deal)), delimiter="$")

	# Clean the data for insertion into database
	loan_data = data_clean(loan_reader)
	#property_data = data_clean(property_reader)
	#lease_data = data_clean(lease_reader)

	# insert rows into database
	loan_seed(current_deal, loan_data)
	# property_seed(current_deal, property_data)
	# lease_seed(current_deal, lease_data)


def loan_seed(current_deal, data):
	# seeding the loan table	
	for row in data:
		Loan.objects.create(
		deal = current_deal,
		loan_name = row["Loan Name"],
		percent_deal = row["% Deal"],
		percent_deal_cutoff = row["% Deal Cutoff"],
		status = row["Status"],
		status_history = row["Status History"],
		city = row["City"],
		state = row["State"],
		zip_code = row["Zip"],
		msa = row["MSA"],
		property_type = row["Property Type"],
		property_subtype = row["Property Subtype"],
		num_properties = row["Num Properties"],
		units = row["Units"],
		units_type = row["Units Type"],
		year_built = row["Year Built"],
		cum_mo_dq = row["Cum Mo Dq"],
		cpn = row["Cpn"],
		cutoff_cpn = row["Cutoff Cpn"],
		rate_type = row["Rate Type"],
		protection = row["Protection"],
		due = row["Due"],
		maturity_type = row["Maturity Type"],
		amort_type = row["Amort Type"],
		curr_trust_bal_usd = row["Curr Trust Bal(USD)"],
		curr_wh_ln_bal_usd = row["Curr Wh Ln Bal(USD)"],
		cur_bal_per_unit_usd = row["Cur Bal Per Unit(USD)"],
		orig_trust_bal_usd = row["Orig Trust Bal(USD)"],
		original_bal_usd = row["Original Bal(USD)"],
		cutoff_trust_bal_usd = row["Cutoff Trust Bal(USD)"],
		cutoff_bal_per_unit_usd = row["Cutoff Bal Per Unit(USD)"],
		scheduled_balloon_usd = row["Scheduled Balloon(USD)"],
		recent_val_usd = row["Recent Val(USD)"],
		recent_val_dt = row["Recent Val Dt"],
		orig_amortization = row["Orig Amortization"],
		change_in_noi = row["Change in NOI"],
		ltv = row["LTV"],
		curr_occ = row["Curr Occ"],
		dscr = row["DSCR"],
		curr_debt_yld = row["Curr Debt Yld"],
		noi_start_dt = row["NOI Start Dt"],
		noi_end_dt = row["NOI End Dt"],
		rec_noi_usd = row["Rec NOI(USD)"],
		rev_ytd_usd = row["Rev YTD(USD)"],
		occ_ytd_usd = row["Occ YTD(USD)"],
		noi_ytd_usd = row["NOI YTD(USD)"],
		dscr_noi_ytd = row["Dscr NOI YTD"],
		rev_py_usd = row["Rev PY(USD)"],
		occ_py = row["Occ PY"],
		noi_py_usd = row["NOI PY(USD)"],
		dscr_noi_py = row["DSCR NOI PY"],
		rev_spy_usd = row["Rev SPY(USD)"],
		occ_spy = row["Occ SPY"],
		noi_spy_usd = row["NOI SPY(USD)"],
		dscr_noi_spy = row["DSCR NOI SPY"],
		cutoff_dscr = row["Cutoff DSCR"],
		cutoff_debt_yld = row["Cutoff Debt Yld"],
		cutoff_noi_usd = row["Cutoff NOI(USD)"],
		cutoff_ncf_usd = row["Cutoff NCF(USD)"],
		cutoff_ltv = row["Cutoff LTV"],
		cutoff_occ = row["Cutoff Occ"],
		largest_tenant = row["Largest Tenant"],
		lrg_tenant_pct = row["Lrg Tenant Pct"],
		lrg_tenant_exp_dt = row["Lrg Tenant Exp Dt"],
		second_largest_tenant = row["2nd Largest Tenant"],
		second_lrg_tenant_pct = row["2nd Lrg Tenant Pct"],
		second_lrg_tenant_exp_dt = row["2nd Lrg Tenant Exp Dt"],
		third_lrg_tenant_exp_dt = row["3rd Lrg Tenant Exp Dt"],
		third_lrg_tenant_pct = row["3rd Lrg Tenant Pct"],
		third_largest_tenant = row["3rd Largest Tenant"],
		fourth_lrg_tenant_exp_dt = row["4th Lrg Tenant Exp Dt"],
		fourth_lrg_tenant_pct = row["4th Lrg Tenant Pct"],
		fourth_largest_tenant = row["4th Largest Tenant"],
		fifth_lrg_tenant_exp_dt = row["5th Lrg Tenant Exp Dt"],
		fifth_lrg_tenant_pct = row["5th Lrg Tenant Pct"],
		fifth_largest_tenant = row["5th Largest Tenant"],
		originator = row["Originator"],
		origination_dt = row["Origination Dt"],
		collateral_id = row["Collateral Id"],
		trustee_id = row["Trustee Id"],
		link_ID = row["Link to Propty/Lease List"]
		)


def data_clean(reader):
	data = []
	# cleaning the file data
	for row in reader:
		for key in row.keys():
			if row[key] == "N/A":
				row[key] = None
			elif re.match(r'\d+/\d+/\d+', row[key]):
				row[key] = datetime.strptime(row[key], '%m/%d/%Y').date()
			else:
				row[key] = re.sub(r',', '', row[key])
				row[key] = re.sub(r'%', '', row[key])
		data.append(row)
	return data

"""
from cmbs.seed import main, data_clean, loan_seed
main('BACM 2007-4')
"""

