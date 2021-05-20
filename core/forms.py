from django import forms
from .models import Post , Deal_products
from tinymce.widgets import TinyMCE

class Deal_productsForm(forms.ModelForm):
	class Meta:
		model = Deal_products
		fields = ('img_url','name','link_item','price','image_width','from_which')

class PostForm(forms.ModelForm):
	class Meta:
		model = Post

		fields = ('is_it_smartphone','title','short_line_to_define','small_line','tags','top_news_banner', 'thumbanil', 'banner_new','para1','para2','para3','publish','status')


class PhoneForm(forms.ModelForm):
	class Meta:
		model = Post
		fields= (
'is_it_smartphone',
'title',
'latest_release',	
'price_range',	
'device_name',
'short_line_to_define',
'small_line',
'tags',
'top_news_banner',
'thumbanil',
'banner_new',
'dimensions',
'weight',
'material',
'no_sim',
'network_2g_3g',
'wifi',
'bluetooth',
'nfc',
'ir_blasster',
'battery_size',
'removable_battery',
'charger_detail',
'charge_0_to_100',
'backup',
'processor',
'antutu_score',
'os',
'camera_type',
'rear_camera_detail',
'video_resolutions',
'front_camera_detail',
'video_resolutions_front',
'display_resolution',
'display_type',
'protection',
'storage_variant',
'expandable',
'stero_speaker',
'headphone_jack',
'pricing1',
'storage_pric1',
'buy_link_1',
'pricing2',
'storage_pric2',
'buy_link_2',
'pricing3',
'storage_pric3',
'buy_link_3',
'pricing4',
'storage_pric4',
'buy_link_4',
'adv',
'dis',
'para1',
'para2',
'smartphone_img_1',
'smartphone_img_2',
'smartphone_img_3',
'smartphone_img_4',
'smartphone_img_5',
'smartphone_img_6',
'smartphone_img_7',
'smartphone_img_8',
'rear_img_1',
'rear_img_2',
'rear_img_3',
'rear_img_4',
'rear_img_5',
'rear_img_6',
'rear_img_7',
'rear_img_8',
'front_img_1',
'front_img_2',
'front_img_3',
'front_img_4',
'front_img_5',
'front_img_6',
'front_img_7',
'front_img_8',
'status',
)