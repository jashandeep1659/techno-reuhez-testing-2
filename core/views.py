from django.shortcuts import render , redirect ,  get_object_or_404
from .models import Post,Top_news, Price_range ,Latest_release,Deal_products
from .forms import PostForm, PhoneForm ,Deal_productsForm 
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger

from django.db.models import Count

# Create your views here.

def home(request ,):
	post =  Post.published.all()[:6:]

	top_banner_items = Top_news.objects.all()
	latest_release = Latest_release.objects.all()

	return render(request , 'core/index.html' , {'post': post , 'top_banner_items':top_banner_items,'latest_release':latest_release })



def detail_view(request , slug , id ,):
	post = get_object_or_404(Post, slug=slug , id=id)
	post_tags_ids = post.tags.values_list('id', flat=True)
	latest_post =  Post.published.all()\
		.exclude(id=post.id)

	similar_posts = Post.published.filter(tags__in=post_tags_ids)\
		.exclude(id=post.id)
	similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
 	.order_by('-same_tags','-publish')[:5]
	similar_posts_all = Post.published.filter(tags__in=post_tags_ids)\
		.exclude(id=post.id)
	similar_posts_all = similar_posts_all.annotate(same_tags=Count('tags'))\
 	.order_by('-same_tags','-publish')[6:]

	same_price_range = Price_range.objects.all()
	latest_release = Latest_release.objects.all()

	deal_products = Deal_products.objects.all()
	return render(request, 'core/detail_view.html',{'post':post,'similar_posts': similar_posts,	'similar_posts_all':similar_posts_all, 'latest_post':latest_post,'same_price_range':same_price_range,'latest_release':latest_release,'deal_products':deal_products })

def post_list_all(request):
	object_list = Post.published.all()
	all_tags = Tag.objects.all().order_by('name')
	paginator = Paginator(object_list, 20) 
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)


	return render(request , 'core/list.html', {'all_tags':all_tags ,'posts':posts,'page':page})

def post_list(request, tag_slug=None):
	all_tags = Tag.objects.all().order_by('name')
	print(all_tags)
	object_list = Post.published.all()
	tag = None
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		object_list = object_list.filter(tags__in=[tag])
		paginator = Paginator(object_list,20 ) 
		page = request.GET.get('page')
		try:
			posts = paginator.page(page)
		except PageNotAnInteger:
			posts = paginator.page(1)
		except EmptyPage:
			posts = paginator.page(paginator.num_pages)

		return render(request, 'core/list.html', {'page': page,
		'posts': posts,
		'tag': tag,'all_tags':all_tags})

def all_deals(request):
	object_list = Deal_products.objects.all()
	paginator = Paginator(object_list, 20)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request , 'core/other/all_deals.html', {'posts':posts,'page':page})


@login_required
def add_phone(request):
	if request.method == 'POST':
		add_phones = PhoneForm(request.POST , request.FILES)
		if add_phones.is_valid():
			phone = add_phones.save(commit=False)
			phone.slug = slugify(phone.short_line_to_define)
			phone.save()
			add_phones.save_m2m()
			return redirect('home')
	else:
		add_phones = PhoneForm()
	return render(request, 'core/admin_folder/add_phone.html', {'add_phone':add_phones})

@login_required
def add_deal(request):
	if request.method =='POST':
		add_deal = Deal_productsForm(request.POST)
		if add_deal.is_valid():
			add_deal.save()
	else:
		add_deal = Deal_productsForm()

	return render(request, 'core/admin_folder/add_deal.html',{'add_deal':add_deal})


@login_required
def add_news(request):
	if request.method == 'POST':
		add_news = PostForm(request.POST, request.FILES)
		if add_news.is_valid():
			post  = add_news.save(commit=False)
			post.slug = slugify(post.short_line_to_define)
			post.save()
			add_news.save_m2m()
			return redirect('home')
	else:
		add_news = PostForm()
	return render(request , 'core/admin_folder/add_news.html',{'add_news':add_news})