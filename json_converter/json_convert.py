import json
import yaml

class json_convert:
	def __init__(self,path):
		with open(path, 'r') as jf:
			self.json_load = json.load(jf)
		
	def converter(self):
		with open("test.yaml", "w") as yf:
			yaml.dump(
				self.json_load,yf,
				default_flow_style=False
			)
	
		
json_convert = json_convert('test.json')
json_convert.converter()
