import time
import inspect
import os
import sys
import pickle
from tqdm.notebook import tqdm
from sklearn.model_selection import GridSearchCV

__fit_model_counter = 0
def save(model):
	global __fit_model_counter, DIR_PATH

	existing_models = [fn[:-6] for fn in os.listdir(DIR_PATH) if fn[-6:]==".model"]
	__fit_model_counter = 1 + max(__fit_model_counter, *[int(model_name) if model_name.isnumeric() else 0 for model_name in existing_models], -1)

	filepath = os.path.join(DIR_PATH, f"{__fit_model_counter}.model")
	with open(filepath, "wb") as f:
		print(f"Saving {filepath}...")
		pickle.dump(model, f)

__mounted = False
def mount():
	global DIR_PATH, __mounted
	if __mounted: return
	__mounted = True

	try:
		from google.colab import drive
		drive.mount('/content/drive')
		DIR_PATH = "/content/drive/MyDrive/Colab Notebooks/output"
		print("Mounted Google Drive folder successfully")
	except:
		try:
			DIR_PATH = os.path.dirname(os.path.abspath(inspect.currentframe().f_back.f_back.f_globals.get('__file__', None)))
			print(f"Saving locally in directory {DIR_PATH}")
		except:
			DIR_PATH = "/content/"
			print("Couldn't save locally nor in Google Drive. Saving in /content/.")

def bar_fit(model, X, y):
	class BarStdout:
		def write(self, text):
			if "totalling" in text and "fits" in text:
				self.bar_size = int(text.split("totalling")[1].split("fits")[0][1:-1])
				self.bar = tqdm(range(self.bar_size))
				self.count = 0
				return
			if "CV" in text and hasattr(self,"bar"):
				self.count += 1
				self.bar.update(n=self.count-self.bar.n)
				if self.count%(self.bar_size//10)==0:
					time.sleep(0.1)
		def flush(self, text=None):
			pass
	default_stdout= sys.stdout
	sys.stdout = BarStdout()
	model.verbose = 5
	model.fit(X, y)
	sys.stdout = default_stdout

def fit(model, X, y, debug=False):
	mount()

	initial_time = time.time()
	if type(model)==GridSearchCV:
		bar_fit(model, X, y)
	else:
		model.fit(X, y)
	final_time   = time.time()
	elapsed_time = final_time - initial_time
	print("Elapsed time: " + ("{:.1f} s".format(elapsed_time)) if elapsed_time < 60 else ("{:.0f} min {:.0f} s".format(round(elapsed_time,0)//60,round(elapsed_time,0)%60)) )

	save(model)
	
def load_models(model_number=None):
	mount()
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