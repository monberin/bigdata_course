from datetime import datetime

def print_task(name):
	current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
	print(name + '\t' + current_time)
	
if __name__ == '__main__':
	print_task('Daryna Hnatenko')
