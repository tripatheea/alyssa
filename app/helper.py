import constants
import urllib2
import json
import mechanize

class MITClass:

    def __init__(self):
        url = constants.url['classes']
        request = urllib2.Request(url, headers=constants.header)
        try:
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.set_handle_refresh(False)
            response = br.open(request)
            message = json.loads(response.read().decode("utf-8"))
            self.classes_data = message['items']
        except urllib2.HTTPError as e:
            message = e.fp.read()

    def get_class_info(self, class_name, what_info):
        if (what_info == "lecture"):
        	return self.get_info(class_name, "LectureSession")
        elif (what_info == "recitation"):
        	return self.get_info(class_name, "RecitationSession")
        elif (what_info == 'lab'):
        	return self.get_info(class_name, "LabSession")

        return self.get_general_info(class_name)

    def get_general_info(self, class_name):
        all_classes = self.classes_data
        return [some_class for some_class in all_classes \
                         if ('id' in some_class and some_class['id'] == class_name)]

    def get_info(self, class_name, what_info):
        all_classes = self.classes_data
        return [some_class for some_class in all_classes \
        			if ('section-of' in some_class and some_class['section-of'] == class_name \
        					and 'type' in some_class and some_class['type'] == what_info)]

class MITExam:
    def __init__(self):
        pass

    def all_exams(self):
        url = constants.url['stellar']
        username = constants.username
        password = constants.password

        request = urllib2.Request(url, headers=constants.header)
        try:
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.set_handle_refresh(False)

            response = br.open(request)

            return response.read()
        
        except urllib2.HTTPError as e:
            return e.fp.read()