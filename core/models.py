from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.db import models
from tinymce.models import HTMLField

    
# Create your models here.
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,self).get_queryset()\
			.filter(status='published')


class Top_news(models.Model):	
	status_no_yes = models.CharField(max_length=5)

	def __str__(self):
		return self.status_no_yes


class Latest_release(models.Model):	
	status_no_yes = models.CharField(max_length=5)

	def __str__(self):
		return self.status_no_yes


class Price_range(models.Model):
	price_range = models.CharField(max_length=200)

	def __str__(self):
		return self.price_range



class Post(models.Model):
	STATUS_CHOICES = (
 	('draft', 'Draft'),
 	('published', 'Published'),
 	)
	id = models.AutoField(auto_created = True,primary_key = True,)
	is_it_smartphone = models.BooleanField(default=False,)
	title = models.CharField(max_length=300)
	short_line_to_define = models.CharField(max_length=150,default="ruhezz")
	small_line = models.CharField(max_length=200, null=True, blank=True)
	tags = TaggableManager()
	slug = models.SlugField(max_length=300, unique_for_date='publish')
	top_news_banner = models.ForeignKey(Top_news , on_delete=models.CASCADE, null=True, blank=True)
	# tag = models.CharField(max_length=field_length, attributes)
	thumbanil= models.ImageField(upload_to='thumbanils/')
	banner_new = models.ImageField(upload_to='banners/')
	adv =HTMLField(null=True, blank=True)
	dis =HTMLField(null=True, blank=True)
	para1 =HTMLField(null=True, blank=True)
	para2 =HTMLField(null=True, blank=True)
	para3 =HTMLField(null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)


	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='published')




	# for the mobile
	# physical overview
	device_name = models.CharField(max_length=150,null=True , blank=True)
	latest_release = models.ForeignKey(Latest_release, null=True, blank=True, on_delete=models.CASCADE)
	price_range = models.ForeignKey(Price_range, null=True, blank=True, on_delete=models.CASCADE)
	dimensions = models.CharField(max_length=150 , null=True,blank=True , default='---')
	weight = models.CharField(max_length=100 ,null=True,blank=True , default='---')
	material = models.CharField(max_length=100, null=True,blank=True , default='---')

	no_sim = models.CharField(max_length=20,default="dual sim")
	network_2g_3g = models.CharField(max_length=100, null=True,blank=True , default='2G,3G,4G')
	wifi = models.CharField(max_length=100, null=True,blank=True , default='Yes, type: _')
	bluetooth = models.CharField(max_length=100, null=True,blank=True , default='yes')
	nfc = models.CharField(max_length=20, null=True,blank=True , default='No')
	ir_blasster = models.CharField(max_length=20, null=True,blank=True , default='No')

	battery_size = models.CharField(max_length=50, null=True,blank=True , default='__mAh')
	removable_battery = models.CharField(max_length=20, null=True,blank=True , default='No')
	charger_detail = models.CharField(max_length=50, null=True,blank=True , default='suported: In box(10wh)')
	charge_0_to_100 = models.CharField(max_length=20,  null=True,blank=True , default='__')
	backup = models.CharField(max_length=20, null=True,blank=True , default='__')

	processor = models.CharField(max_length=50, null=True,blank=True , default='---')
	os = models.CharField(max_length=50, null=True,blank=True , default='Andriod 11,  ')
	antutu_score = models.CharField(max_length=100,null=True,blank=True, default="_")

	camera_type = models.CharField(max_length=20, null=True,blank=True , default='Triple')
	rear_camera_detail = models.CharField(max_length=100 , null=True,blank=True , default='')
	video_resolutions = models.CharField(max_length=50, null=True,blank=True , default='4K@30fps, 1080p@30/60/120fps, 720p@960fps')
	front_camera_detail = models.CharField(max_length=100,  null=True,blank=True , default='')
	video_resolutions_front = models.CharField(max_length=50, null=True,blank=True , default=' 1080p@30/60fps, 720p@60fps')


	display_resolution = models.CharField(max_length=50, null=True,blank=True , default='FHD')
	display_type = models.CharField(max_length=50, null=True,blank=True , default='Amled')
	protection = models.CharField(max_length=50, null=True,blank=True , default='__')

	storage_variant = models.CharField(max_length=100, null=True,blank=True , default='4GB 64GB, 6GB 128GB')
	expandable = models.CharField(max_length=10, null=True,blank=True , default='Yes')

	stero_speaker = models.CharField(max_length=20, null=True,blank=True , default='Yes')
	headphone_jack = models.CharField(max_length=20, null=True,blank=True , default='Yes')

	pricing1 = models.CharField(max_length=30, null=True,blank=True ,)
	storage_pric1 =models.CharField(max_length=30, null=True,blank=True ,)
	buy_link_1 = models.CharField(max_length=150,null=True,blank=True ,)

	pricing2 = models.CharField(max_length=30, null=True,blank=True ,)
	storage_pric2 =models.CharField(max_length=30, null=True,blank=True ,)
	buy_link_2 = models.CharField(max_length=150,null=True,blank=True ,)

	pricing3 = models.CharField(max_length=30, null=True,blank=True ,)
	storage_pric3 =models.CharField(max_length=30, null=True,blank=True ,)
	buy_link_3 = models.CharField(max_length=150,null=True,blank=True ,)

	pricing4 = models.CharField(max_length=30, null=True,blank=True ,)
	storage_pric4 =models.CharField(max_length=30, null=True,blank=True ,)
	buy_link_4 = models.CharField(max_length=150,null=True,blank=True ,)




	smartphone_img_1 = models.CharField(max_length=500, null=True, blank=True)
	smartphone_img_2 = models.CharField(max_length=500, null=True, blank=True)
	smartphone_img_3 = models.CharField(max_length=500, null=True, blank=True)
	smartphone_img_4 = models.CharField(max_length=500, null=True, blank=True)
	smartphone_img_5 = models.CharField(max_length=500, null=True, blank=True)
	smartphone_img_6 = models.CharField(max_length=500, null=True, blank=True)
	smartphone_img_7 = models.CharField(max_length=500, null=True, blank=True)
	smartphone_img_8 = models.CharField(max_length=500, null=True, blank=True)

	rear_img_1 = models.CharField(max_length=500, null=True, blank=True)
	rear_img_2 = models.CharField(max_length=500, null=True, blank=True)
	rear_img_3 = models.CharField(max_length=500, null=True, blank=True)
	rear_img_4 = models.CharField(max_length=500, null=True, blank=True)
	rear_img_5 = models.CharField(max_length=500, null=True, blank=True)
	rear_img_6 = models.CharField(max_length=500, null=True, blank=True)
	rear_img_7 = models.CharField(max_length=500, null=True, blank=True)
	rear_img_8 = models.CharField(max_length=500, null=True, blank=True)


	front_img_1 = models.CharField(max_length=500, null=True, blank=True)
	front_img_2 = models.CharField(max_length=500, null=True, blank=True)
	front_img_3 = models.CharField(max_length=500, null=True, blank=True)
	front_img_4 = models.CharField(max_length=500, null=True, blank=True)
	front_img_5 = models.CharField(max_length=500, null=True, blank=True)
	front_img_6 = models.CharField(max_length=500, null=True, blank=True)
	front_img_7 = models.CharField(max_length=500, null=True, blank=True)
	front_img_8 = models.CharField(max_length=500, null=True, blank=True)

	objects = models.Manager()
	published = PublishedManager()

	class Meta:
 		ordering = ('-publish',)

	def __str__(self):
 		return self.title


class Flip_or_ama(models.Model):	
	status_no_yes = models.CharField(max_length=20)

	def __str__(self):
		return self.status_no_yes



class Deal_products(models.Model):
	img_url = models.CharField(max_length=300,)
	name = models.CharField(max_length=200)
	link_item = models.CharField(max_length=300,)
	price = models.CharField(max_length=102,)
	from_which = models.ForeignKey(Flip_or_ama, on_delete=models.CASCADE , null=True)
	created = models.DateTimeField( auto_now_add=True)
	image_width = models.CharField(max_length=50,default="60")

	class Meta:
 		ordering = ('-created',)

	def __str__(self):
 		return self.name


