from django.db import models

class Deal(models.Model):
	deal_name = models.CharField(max_length=32)

	def __str__(self):
		return self.deal_name

class Loan(models.Model):
	link_id = models.CharField(max_length=128, primary_key=True)
	deal = models.ForeignKey(Deal)
	loan_name = models.CharField(max_length=256)
	percent_deal = models.DecimalField(max_digits=5, decimal_places=2)
	percent_deal_cutoff = models.DecimalField(max_digits=5, decimal_places=2)
	status = models.CharField(max_length=64)
	status_history = models.CharField(max_length=60)
	city = models.CharField(max_length=256)
	state = models.CharField(max_length=2)
	zip_code = models.CharField(max_length=5)
	# msa = models.CharField(max_length=128)
	# property_type = models.CharField(max_length=128)
	# property_subtype = models.CharField(max_length=128)
	# num_properties = models.IntegerField()
	# units = models.IntegerField()
	# units_type = models.CharField(max_length=64)
	# year_built = models.CharField(max_length=64)
	# cum_mo_dq = models.IntegerField()
	# cpn = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# cutoff_cpn = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# rate_type = models.CharField(max_length=32, null=True)
	# protection = models.CharField(max_length=64, null=True)
	# due = models.DateField(null=True)
	# maturity_type = models.CharField(max_length=32, null=True)
	# amort_type = models.CharField(max_length=32, null=True)
	# curr_trust_bal_usd = models.IntegerField(null=True)
	# curr_wh_ln_bal_usd = models.IntegerField(null=True)
	# cur_bal_per_unit_usd = models.IntegerField(null=True)
	# orig_trust_bal_usd = models.IntegerField(null=True)
	# original_bal_usd = models.IntegerField(null=True)
	# cutoff_trust_bal_usd = models.IntegerField(null=True)
	# cutoff_bal_per_unit_usd = models.IntegerField(null=True)
	# scheduled_balloon_usd = models.IntegerField(null=True)
	# recent_val_usd = models.IntegerField(null=True)
	# recent_val_dt = models.DateField(null=True)
	# orig_amortization = models.IntegerField(null=True)
	# change_in_noi = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# ltv = models.IntegerField(null=True)
	# curr_occ = models.IntegerField(null=True)
	# dscr = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# curr_debt_yld = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# noi_start_dt = models.DateField(null=True)
	# noi_end_dt = models.DateField(null=True)
	# rec_noi_usd = models.IntegerField(null=True)
	# rev_ytd_usd = models.IntegerField(null=True)
	# occ_ytd_usd = models.IntegerField(null=True)
	# noi_ytd_usd = models.IntegerField(null=True)
	# dscr_noi_ytd = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# rev_py_usd = models.IntegerField(null=True)
	# occ_py = models.IntegerField(null=True)
	# noi_py_usd = models.IntegerField(null=True)
	# dscr_noi_py = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# rev_spy_usd = models.IntegerField(null=True)
	# occ_spy = models.IntegerField(null=True)
	# noi_spy_usd = models.IntegerField(null=True)
	# dscr_noi_spy = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# cutoff_dscr = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# cutoff_debt_yld = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# cutoff_noi_usd = models.IntegerField(null=True)
	# cutoff_ncf_usd = models.IntegerField(null=True)
	# cutoff_ltv = models.IntegerField(null=True)
	# cutoff_occ = models.IntegerField(null=True)
	# largest_tenant = models.CharField(max_length=256, null= True)
	# lrg_tenant_pct = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# lrg_tenant_exp_dt = models.DateField(null=True)
	# second_largest_tenant = models.CharField(max_length=256, null=True)
	# second_lrg_tenant_pct = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# second_lrg_tenant_exp_dt = models.DateField(null=True)
	# third_lrg_tenant_exp_dt = models.DateField(null=True)
	# third_lrg_tenant_pct = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# third_largest_tenant = models.CharField(max_length=256, null=True)
	# fourth_lrg_tenant_exp_dt = models.DateField(null=True)
	# fourth_lrg_tenant_pct = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# fourth_largest_tenant = models.CharField(max_length=256, null=True)
	# fifth_lrg_tenant_exp_dt = models.DateField(null=True)
	# fifth_lrg_tenant_pct = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# fifth_largest_tenant = models.CharField(max_length=256, null=True)
	# originator = models.CharField(max_length=256)
	# origination_dt = models.DateField()
	# collateral_id = models.IntegerField()
	# trustee_id = models.IntegerField()


	def __str__(self):
		return self.loan_name


class Property(models.Model):
	property_name = models.CharField(max_length=256)
	# uw = models.CharField(max_length=256)
	deal = models.ForeignKey(Deal)
	loan_name = models.CharField(max_length=128)
	loan_status = models.CharField(max_length=32)
	property_type = models.CharField(max_length=16)
	address = models.CharField(max_length=256)
	city = models.CharField(max_length=128)
	zip_code = models.CharField(max_length=5)
	# msa = models.CharField(max_length=64)
	state = models.CharField(max_length=2)
	country = models.CharField(max_length=74)
	loan_link_id = models.ForeignKey(Loan)
	# appraisal_value_usd = models.IntegerField()
	# value_as_of = models.DateField()
	# cutoff_value_usd = models.IntegerField()
	# occ = models.IntegerField()
	# occ_as_of = models.DateField()
	# cutoff_occ = models.IntegerField()
	# cap_rate = models.DecimalField(max_digits=5, decimal_places=2)
	# cutoff_noi_usd = models.IntegerField()
	# noi_usd = models.IntegerField()
	# noi_as_of = models.DateField()
	# cutoff_ncf_usd = models.IntegerField()
	# ncf_usd = models.IntegerField()
	# ncf_as_of = models.DateField()
	# curr_sqft_units = models.IntegerField()
	# cutoff_sqft_units = models.IntegerField()
	# curr_alloc_amt_usd = models.IntegerField()
	# curr_alloc_pct = models.IntegerField()
	# fin_indic = models.CharField(max_length=4)
	# def_maintenance = models.CharField(max_length=1)
	# loan_trustee_id = models.CharField(max_length=32)
	# year_built = models.CharField(max_length=4)
	# year_renovated = models.CharField(max_length=4)
	# lease_review_dt = models.DateField()
	# lease_r_o_1st_yr = models.IntegerField()
	# lease_r_o_2nd_yr = models.IntegerField()
	# lease_r_o_3rd_yr = models.IntegerField()
	# lease_r_o_4th_yr = models.IntegerField()
	# lease_r_o_5th_yr = models.IntegerField()
	# reo_comm = models.TextField()
	# reo_comm_asof = models.DateField()


	def __str__(self):
		return self.property_name


class Lease(models.Model):
	lease_name = models.CharField(max_length=256)
	as_of = models.CharField(max_length=7)
	loan_name = models.CharField(max_length=256)
	property_name = models.CharField(max_length=256)
	expiration = models.DateField()
	loanexp = models.DecimalField(max_digits=5, decimal_places=2)
	exposure_usd = models.IntegerField()
	square_feet = models.IntegerField()
	loan_mat_dt = models.DateField()
	loan_link = models.ForeignKey(Loan)

	def __str__(self):
		return self.lease_name

class Keyword(models.Model):
	word = models.CharField(max_length=64)

	def __str__(self):
		return self.word


class Publisher(models.Model):
	name = models.CharField(max_length=256)
	Article_searched = models.IntegerField()
	relevant_found = models.IntegerField()

	def __str__(self):
		return self.name


class Article(models.Model):
	title = models.CharField(max_length=256)
	author = models.CharField(max_length=256)
	url = models.URLField(null=True)
	blurb = models.TextField()
	property = models.ForeignKey(Property)
	publisher_ID = models.ForeignKey(Publisher)
	key_words = models.ManyToManyField(Keyword)

	def __str__(self):
		return self.title
