import time
import inspect
import os
import pickle

__fit_model_counter = 0
def fit(model, X, y, debug=False):
	global DIR_PATH
	# Fit and time it ------------------------------------------------------------
	initial_time = time.time()
	model.fit(X, y)
	final_time   = time.time()
	elapsed_time = final_time - initial_time
	print("Elapsed time: " + ("{:.1f} s".format(elapsed_time)) if elapsed_time < 60 else ("{:.0f} min {:.0f} s".format(round(elapsed_time,0)//60,round(elapsed_time,0)%60)) )

	return inspect.currentframe().f_back.f_globals

	# Save the model -------------------------------------------------------------
	# DIR_PATH
	exec_filename = inspect.currentframe().f_back.f_globals.get('__file__', None)
	if exec_filename is None: DIR_PATH = "/content/"
	else: DIR_PATH = os.path.dirname(os.path.abspath(exec_filename))
	existing_models = [fn[:-6] for fn in os.listdir(DIR_PATH) if fn[-6:]==".model"]

	# __fit_model_counter 
	global __fit_model_counter
	__fit_model_counter = 1 + max(__fit_model_counter, *[int(model_name) if model_name.isnumeric() else 0 for model_name in existing_models], -1)

	# save
	filepath = os.path.join(DIR_PATH, f"{__fit_model_counter}.model")
	with open(filepath, "wb") as f:
		print(f"Saving {filepath}...")
		pickle.dump(model, f)

def load_models(model_number=None):
	global DIR_PATH
	DIR_PATH = os.path.dirname(os.path.abspath(inspect.currentframe().f_back.f_globals.get("__file__", None)))
	existing_models = [fn[:-6] for fn in os.listdir(DIR_PATH) if fn[-6:]==".model"]

	if model_number is None:
		if existing_models:
			print("Existing models:\n"+"\n".join([model_name+".model" for model_name in existing_models]))
		else:
			print("No model saved")
		return

	model_number = model_number if type(model_number)==int else int(model_number.replace(".model",""))
	filepath = os.path.join(DIR_PATH, f"{model_number}.model")
	with open(filepath, "rb") as f:
		print(f"Loading {filepath}...")
		model = pickle.load(f)

	return model