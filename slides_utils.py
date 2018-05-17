# Import Python Packages
from notebook.services.config import ConfigManager
from IPython.core.display import HTML, display

# Configure Display Layout

dict_mode={'4x3':[1280,1024,720],'laptop':[1366, 768,620]}
mode='laptop'
cm = ConfigManager()
cm.update('livereveal', {
		  'width' : dict_mode[mode][0],
		  'height': dict_mode[mode][1],
		  'scroll': True,
		  'autolaunch': True,
		  
});
print("Slides Layout Configured: %s"% mode)

def change_mode(mode):
	cm.update('livereveal', {
			  'width' : dict_mode[mode][0],
			  'height': dict_mode[mode][1],
			  'scroll': True,
	});
	print("Slides Layout Configured: %s"% mode)

#html_code='<center><img src="./MIR/Slide%d.JPG" style="height:%dpx;"></center>'% (slide_number,dict_mode[mode][2])

def show_slide(slide_number):
	html_code='<img src="./MIR/Slide%d.JPG" style="height:%dpx;">'% (slide_number,dict_mode[mode][2])
	display(HTML(html_code))
	
def show_web(url):
    html_code='<center><iframe src="%s" width="800" height="%d" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></center>' \
		% (url,dict_mode[mode][2])
    display(HTML(html_code))
	
def get_slide(slide_number):
	html_code='<center><img src="./MIR/Slide%d.JPG" style="height:%dpx;"></center>'% (slide_number,dict_mode[mode][2])
	return html_code

def get_web(url):
	html_code='<center><iframe src="%s" width="800" height="%d" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></center>' \
		% (url,dict_mode[mode][2])
	return html_code