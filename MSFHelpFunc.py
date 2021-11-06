def var_type_list(column_list, df_code):

	cat_cols = []
	num_cols = []

	for col in column_list:
		df_code = df_code
		if grab_variable_type(col, df_code) == "Coded":
			cat_cols.append(col)
		if grab_variable_type(col, df_code) == "Numeric":
			num_cols.append(col)

	return cat_cols, num_cols


def grab_variable_type(var_name, df_code):
	x = df_code.loc[(df_code['Variable Name'] == var_name),'Variable Type'].iloc[0]
	return x

def get_variable_label(variable_name, df_code):
	"""
		df_code is the name of the dataframe from which to grab the label
	"""
	try:
		x = df_code.loc[(df_code['Variable Name'] == variable_name), 'Variable Label'].iloc[0]
	except:
		x = df_code.loc[(df_code['Variable Name'] == variable_name.split("_")[0]), 'Variable Label'].iloc[0]
	return x

