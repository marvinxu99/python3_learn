# using .get() to remove the membership test is neat
def get_exam_detail_ids(self, json):
	return (
		obj['ExamDetailId'] for obj in json	
			if obj.get('ExamDetailId'] is not None	
	)