from django.db import models

# Create your models here.

class Deal(models.Model):
	deal_name = models.CharField(max_length=32)

	def __str__(self):
		return self.deal_name

class Loan(models.Model):
	deal = models.ForeignKey('Deal')
	loan_name = models.CharField(max_length=256)
	percent_deal = models.DecimalField(max_digits=4, decimal_places=2)
	percent_deal_cutoff = models.DecimalField(max_digits=4, decimal_places=2)
	status = models.CharField(max_length=32)
	status_history = models.CharField(max_length=60)
	city = models.CharField(max_length=128)
	state = models.CharField(max_length=2)
	zip_code = models.CharField(max_length=5)
	msa = models.CharField(max_length=64)
	property_type = models.CharField(max_length=64)
	property_subtype = models.CharField(max_length=64)
	num_properties = models.IntegerField()
	units = models.IntegerField()
	units_type = models.CharField(max_length=32)
	year_built = models.CharField(max_length=7)
	cum_mo_dq = models.IntegerField()
	cpn = models.DecimalField(max_digits=4, decimal_places=2, null=True)
	cutoff_cpn = models.DecimalField(max_digits=4, decimal_places=2)
	rate_type = models.CharField(max_length=16)
	protection = models.CharField(max_length=32, null=True)
	due = models.DateField()
	maturity_type = models.CharField(max_length=16)
	amort_type = models.CharField(max_length=16)
	curr_trust_bal_usd = models.IntegerField()
	curr_wh_ln_bal_usd = models.IntegerField()
	cur_bal_per_unit_usd = models.IntegerField()
	orig_trust_bal_usd = models.IntegerField()
	original_bal_usd = models.IntegerField()
	cutoff_trust_bal_usd = models.IntegerField()
	cutoff_bal_per_unit_usd = models.IntegerField()
	scheduled_balloon_usd = models.IntegerField()
	recent_val_usd = models.IntegerField()
	recent_val_dt = models.DateField()
	orig_amortization = models.IntegerField()
	change_in_noi = models.DecimalField(max_digits=5, decimal_places=2)
	ltv = models.IntegerField()
	curr_occ = models.IntegerField()
	dscr = models.DecimalField(max_digits=4, decimal_places=2)
	curr_debt_yld = models.DecimalField(max_digits=4, decimal_places=2)
	noi_start_dt = models.DateField()
	noi_end_dt = models.DateField()
	rec_noi_usd = models.IntegerField()
	rev_ytd_usd = models.IntegerField()
	occ_ytd_usd = models.IntegerField()
	noi_ytd_usd = models.IntegerField()
	dscr_noi_ytd = models.DecimalField(max_digits=4, decimal_places=2)
	rev_py_usd = models.IntegerField()
	occ_py = models.IntegerField()
	noi_py_usd = models.IntegerField()
	dscr_noi_py = models.DecimalField(max_digits=4, decimal_places=2)
	rev_spy_usd = models.IntegerField()
	occ_spy = models.IntegerField()
	noi_spy_usd = models.IntegerField()
	dscr_noi_spy = models.DecimalField(max_digits=4, decimal_places=2)
	cutoff_dscr = models.DecimalField(max_digits=4, decimal_places=2)
	cutoff_debt_yld = models.DecimalField(max_digits=4, decimal_places=2)
	cutoff_noi_usd = models.IntegerField()
	cutoff_ncf_usd = models.IntegerField()
	cutoff_ltv = models.IntegerField()
	cutoff_occ = models.IntegerField()
	largest_tenant = models.CharField(max_length=128, null= True)
	lrg_tenant_pct = models.DecimalField(max_digits=4, decimal_places=2, null=True)
	lrg_tenant_exp_dt = models.DateField(null=True)
	second_largest_tenant = models.CharField(max_length=128, null=True)
	second_lrg_tenant_pct = models.DecimalField(max_digits=4, decimal_places=2, null=True)
	second_lrg_tenant_exp_dt = models.DateField(null=True)
	third_lrg_tenant_exp_dt = models.DateField(null=True)
	third_lrg_tenant_pct = models.DecimalField(max_digits=4, decimal_places=2, null=True)
	third_largest_tenant = models.CharField(max_length=128, null=True)
	fourth_lrg_tenant_exp_dt = models.DateField(null=True)
	fourth_lrg_tenant_pct = models.DecimalField(max_digits=4, decimal_places=2, null=True)
	fourth_largest_tenant = models.CharField(max_length=128, null=True)
	fifth_lrg_tenant_exp_dt = models.DateField(null=True)
	fifth_lrg_tenant_pct = models.DecimalField(max_digits=4, decimal_places=2, null=True)
	fifth_largest_tenant = models.CharField(max_length=128, null=True)
	originator = models.CharField(max_length=128)
	origination_dt = models.DateField()
	collateral_id = models.IntegerField()
	trustee_id = models.IntegerField()
	link_ID = models.CharField(max_length=64, primary_key=True)

	def __str__(self):
		return self.loan_name


class Property(models.Model):
	property_name = models.CharField(max_length=256)
	uw = models.CharField(max_length=256)
	deal = models.ForeignKey(Deal)
	loan_name = models.CharField(max_length=128)
	loan_status = models.CharField(max_length=32)
	property_type = models.CharField(max_length=16)
	address = models.CharField(max_length=256)
	city = models.CharField(max_length=128)
	zip_code = models.CharField(max_length=5)
	msa = models.CharField(max_length=64)
	state = models.CharField(max_length=2)
	country = models.CharField(max_length=74)
	appraisal_value_usd = models.IntegerField()
	value_as_of = models.DateField()
	cutoff_value_usd = models.IntegerField()
	occ = models.IntegerField()
	occ_as_of = models.DateField()
	cutoff_occ = models.IntegerField()
	cap_rate = models.DecimalField(max_digits=4, decimal_places=2)
	cutoff_noi_usd = models.IntegerField()
	noi_usd = models.IntegerField()
	noi_as_of = models.DateField()
	cutoff_ncf_usd = models.IntegerField()
	ncf_usd = models.IntegerField()
	ncf_as_of = models.DateField()
	curr_sqft_units = models.IntegerField()
	cutoff_sqft_units = models.IntegerField()
	curr_alloc_amt_usd = models.IntegerField()
	curr_alloc_pct = models.IntegerField()
	fin_indic = models.CharField(max_length=4)
	def_maintenance = models.CharField(max_length=1)
	loan_trustee_id = models.CharField(max_length=32)
	year_built = models.CharField(max_length=4)
	year_renovated = models.CharField(max_length=4)
	lease_review_dt = models.DateField()
	lease_r_o_1st_yr = models.IntegerField()
	lease_r_o_2nd_yr = models.IntegerField()
	lease_r_o_3rd_yr = models.IntegerField()
	lease_r_o_4th_yr = models.IntegerField()
	lease_r_o_5th_yr = models.IntegerField()
	reo_comm = models.TextField()
	reo_comm_asof = models.DateField()
	loan_link = models.ForeignKey(Loan)

	def __str__(self):
		return self.property_name

class Lease(models.Model):
	lease_name = models.CharField(max_length=256)
	as_of = models.CharField(max_length=7)
	loan_name = models.CharField(max_length=256)
	property_name = models.CharField(max_length=256)
	expiration = models.DateField()
	loanexp = models.DecimalField(max_digits=4, decimal_places=2)
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


class Article(models.Model):
	title = models.CharField(max_length=256)
	author = models.CharField(max_length=256)
	blurb = models.TextField()
	publisher_ID = models.ForeignKey('Publisher')
	key_words = models.ManyToManyField('Keyword')

	def __str__(self):
		return self.title


class Publisher(models.Model):
	name = models.CharField(max_length=256)
	Article_searched = models.IntegerField()
	relevant_found = models.IntegerField()

	def __str__(self):
		return self.name
