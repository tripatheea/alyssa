import constants
import urllib.request
import json


class MITClass:

	def __init__(self):
		url = constants.url['classes']
		response = urllib.request.urlopen(url)
		message = json.loads(response.read().decode("utf-8"))
		response.close()
		self.classes_data = message['items']

	def get_class_info(self, class_name):
		all_classes = self.classes_data
		info = ""
		for element in all_classes:
			info = info + str(element)

		info = self.get_lecture_info('6.01')
		return str(info)


	def get_lecture_info(self, class_name):
		all_classes = self.classes_data
		return [some_class for some_class in all_classes if ('id' in some_class and some_class['id'] == '6.01')]
