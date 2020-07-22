from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from DailyNews.models import *
from django.contrib.auth.decorators import login_required
from .serializers import NewsSerializers
from rest_framework import viewsets

# ******************************************************************************************************************************
# index


def index(request):
    allnews = news.objects.all()
    cat = subcategory.objects.all()
    # latest sport news
    sport = []
    for i in allnews:
        if i.category.category == "SPORT":
            sport.append(i)
    lastsport = sport[-1]

    # latest business news
    business = []
    for i in allnews:
        if i.category.category == "BUSINESS":
            business.append(i)
    lastbusiness = business[-1]

    # latest entertainment news
    entertainment = []
    for i in allnews:
        if i.category.category == "ENTERTAINMENT":
            entertainment.append(i)
    lastentertainment = entertainment[-1]

    # International news
    International = []
    for i in allnews:
        if i.subcat.subcat == "International-News":
            International.append(i)
    Internationalnews = International[-5:-1]

    # Breaking news
    Breaking = []
    for i in allnews:
        if i.subcat.subcat == "Breaking-News":
            Breaking.append(i)
    Breakingnews = Breaking[-5:-1]

    news_list = news.objects.all().order_by('-id')[1:7][::-1]
    latest_news = news.objects.latest('date')
    args = {'news': news_list, 'latest_news': latest_news, 'allnews': allnews,
            'lastsport': lastsport, 'lastentertainment': lastentertainment,
            'lastbusiness': lastbusiness, 'Internationalnews': Internationalnews, 'Breakingnews': Breakingnews, 'cat': cat}
    return render(request, 'index.html', args)

# ******************************************************************************************************************************
# about


def about(request):
    cat = subcategory.objects.all()
    data = About.objects.all()
    emp = Employee.objects.all()
    allnews = news.objects.all()
    latest_news = news.objects.latest('date')
    news_list = news.objects.all().order_by('-id')[1:7][::-1]
    args = {'about': data, 'emp': emp, 'latest_news': latest_news,
            'news': news_list, 'allnews': allnews, 'cat': cat}
    return render(request, 'about.html', args)

# ******************************************************************************************************************************
# contactus


def contact(request):
    allnews = news.objects.all()
    cat = subcategory.objects.all()
    latest_news = news.objects.latest('date')
    news_list = news.objects.all().order_by('-id')[1:7][::-1]
    args = {'latest_news': latest_news,
            'news': news_list, 'allnews': allnews, 'cat': cat}
    return render(request, 'contact.html', args)

# ******************************************************************************************************************************
# allnews


def allnews(request):
    cat = subcategory.objects.all()
    allnews = news.objects.all().order_by('-id')[2:22][::-1]
    latest_news = news.objects.latest('date')
    news_list = news.objects.all().order_by('-id')[1:7][::-1]
    args = {'allnews': allnews, 'cat': cat,
            'latest_news': latest_news, 'news': news_list}
    return render(request, 'catagories-post.html', args)

# ******************************************************************************************************************************
# view_more


def view_more(request, id):
    mynews = []
    allnews = news.objects.filter(id=id)
    for i in allnews:
        mynews.append(i)
    passnews = mynews[0]
    cat = subcategory.objects.all()
    com = Comment.objects.all().order_by('-id')[0:10]
    latest_news = news.objects.latest('date')
    news_list = news.objects.all().order_by('-id')[1:7][::-1]
    counter = 0
    for i in com:
        if passnews.id == i.newsid:
            counter = counter + 1
    counters = counter
    args = {'mynews': passnews, 'cat': cat,
            'latest_news': latest_news, 'news': news_list, 'comment': com, 'counter': counters}
    return render(request, 'view_more.html', args)

# ******************************************************************************************************************************
# category_news


def category_news(request, id):
    latest_news = news.objects.latest('date')
    newscat = []
    catnews = subcategory.objects.filter(id=id)
    for i in catnews:
        newscat.append(i)
    passcat = newscat[0]
    allnews = news.objects.all()
    cat = subcategory.objects.all()
    args = {'latest_news': latest_news, 'catnews': passcat,
            'allnews': allnews, 'news': allnews, 'cat': cat}
    return render(request, 'category_news.html', args)
# ******************************************************************************************************************************
# User Search Area


def search(request):
    if request.method == 'POST':
        cat = request.POST['search']

        if cat == 'national' or cat == 'National-News' or cat == 'nationalnews' or cat == 'national-news':
            newstype = subcategory.objects.get(id=5)
            allnews = news.objects.all()
            cat = subcategory.objects.all()
            latest_news = news.objects.latest('date')
            return render(request, 'search.html', {'latest_news': latest_news, 'catnews': newstype, 'news': allnews, 'cat': cat})
        elif cat == 'international' or cat == 'International-News' or cat == 'internationalnews' or cat == 'international-news':
            newstype = subcategory.objects.get(id=6)
            allnews = news.objects.all()
            cat = subcategory.objects.all()
            latest_news = news.objects.latest('date')
            return render(request, 'search.html', {'latest_news': latest_news, 'catnews': newstype, 'news': allnews, 'cat': cat})
        elif cat == 'states' or cat == 'States-News' or cat == 'statesnews' or cat == 'states-news':
            newstype = subcategory.objects.get(id=7)
            allnews = news.objects.all()
            cat = subcategory.objects.all()
            latest_news = news.objects.latest('date')
            return render(request, 'search.html', {'latest_news': latest_news, 'catnews': newstype, 'news': allnews, 'cat': cat})
        elif cat == 'cities' or cat == 'Cities-News' or cat == 'citiesnews' or cat == 'cities-news':
            newstype = subcategory.objects.get(id=8)
            allnews = news.objects.all()
            cat = subcategory.objects.all()
            latest_news = news.objects.latest('date')
            return render(request, 'search.html', {'latest_news': latest_news, 'catnews': newstype, 'news': allnews, 'cat': cat})
        elif cat == 'breaking' or cat == 'Breaking-News' or cat == 'breakingnews' or cat == 'breaking-news':
            newstype = subcategory.objects.get(id=20)
            allnews = news.objects.all()
            cat = subcategory.objects.all()
            latest_news = news.objects.latest('date')
            return render(request, 'search.html', {'latest_news': latest_news, 'catnews': newstype, 'news': allnews, 'cat': cat})
        else:
            allnews = news.objects.all()
            cat = subcategory.objects.all()
            # latest sport news
            sport = []
            for i in allnews:
                if i.category.category == "SPORT":
                    sport.append(i)
            lastsport = sport[-1]

            # latest business news
            business = []
            for i in allnews:
                if i.category.category == "BUSINESS":
                    business.append(i)
            lastbusiness = business[-1]

            # latest entertainment news
            entertainment = []
            for i in allnews:
                if i.category.category == "ENTERTAINMENT":
                    entertainment.append(i)
            lastentertainment = entertainment[-1]

            # International news
            International = []
            for i in allnews:
                if i.subcat.subcat == "International-News":
                    International.append(i)
            Internationalnews = International[-5:-1]

            # Breaking news
            Breaking = []
            for i in allnews:
                if i.subcat.subcat == "Breaking-News":
                    Breaking.append(i)
            Breakingnews = Breaking[-5:-1]

            news_list = news.objects.all().order_by('-id')[1:7][::-1]
            latest_news = news.objects.latest('date')
            args = {'news': news_list, 'latest_news': latest_news, 'allnews': allnews,
                    'lastsport': lastsport, 'lastentertainment': lastentertainment,
                    'lastbusiness': lastbusiness, 'Internationalnews': Internationalnews, 'Breakingnews': Breakingnews, 'cat': cat}
            messages.info(request, 'Invalid Search')
            return render(request, 'index.html', args)


# ******************************************************************************************************************************
# User Registration Area


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        img_prof = request.FILES['myfile']
        age = request.POST['age']
        gender = request.POST['gender']

        if password1 == password2:
            # username is already exists or not
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Name is Taken..!!')
                return redirect('register')
            # user email is already exists or not
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Id is Taken..!!')
                return redirect('register')
            else:
                user_form = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user_form.save()
                user_id = User.objects.get(
                    username=username).pk
                profile_form = UserProfile(
                    age=age, gender=gender, image=img_prof, user_id=user_id)
                profile_form.save()
                messages.info(
                    request, 'User Registration Successfuly Now You Can Login..!!')
                return redirect('login')
    else:
        cat = subcategory.objects.all()
        latest_news = news.objects.latest('date')
        news_list = news.objects.all().order_by('-id')[1:7][::-1]
        args = {'cat': cat, 'latest_news': latest_news, 'news': news_list}
        return render(request, 'user_register.html', args)
# End User Registration Area

# ******************************************************************************************************************************
# User Login


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = user.username
            request.session['userid'] = user.id

            auth.login(request, user)
            allnews = news.objects.all()
            cat = subcategory.objects.all()

            # latest sport news
            sport = []
            for i in allnews:
                if i.category.category == "SPORT":
                    sport.append(i)
            lastsport = sport[-1]

            # latest business news
            business = []
            for i in allnews:
                if i.category.category == "BUSINESS":
                    business.append(i)
            lastbusiness = business[-1]

            # latest entertainment news
            entertainment = []
            for i in allnews:
                if i.category.category == "ENTERTAINMENT":
                    entertainment.append(i)
            lastentertainment = entertainment[-1]

            # International news
            International = []
            for i in allnews:
                if i.subcat.subcat == "International-News":
                    International.append(i)
            Internationalnews = International[-5:-1]

            # Breaking news
            Breaking = []
            for i in allnews:
                if i.subcat.subcat == "Breaking-News":
                    Breaking.append(i)
            Breakingnews = Breaking[-5:-1]

            news_list = news.objects.all().order_by('-id')[1:7][::-1]
            latest_news = news.objects.latest('date')
            args = {'user': request.user, 'news': news_list,
                    'latest_news': latest_news, 'allnews': allnews,
                    'lastsport': lastsport, 'lastentertainment': lastentertainment,
                    'lastbusiness': lastbusiness, 'Internationalnews': Internationalnews, 'Breakingnews': Breakingnews, 'cat': cat}
            messages.info(request, 'User Login Successfuly..!!')
            return render(request, 'index.html', args)
        else:
            messages.info(request, 'Invelid Credentials..!!')
            return redirect('login')
    else:
        cat = subcategory.objects.all()
        latest_news = news.objects.latest('date')
        news_list = news.objects.all().order_by('-id')[1:7][::-1]
        args = {'cat': cat, 'latest_news': latest_news, 'news': news_list}
        return render(request, 'user_login.html', args)
# End User Login

# ******************************************************************************************************************************
# user Logout


@login_required
def logoutform(request):
    auth.logout(request)
    messages.info(request, 'User Logout Successfuly..!!')
    allnews = news.objects.all()
    cat = subcategory.objects.all()

    # latest sport news
    sport = []
    for i in allnews:
        if i.category.category == "SPORT":
            sport.append(i)
    lastsport = sport[-1]

    # latest business news
    business = []
    for i in allnews:
        if i.category.category == "BUSINESS":
            business.append(i)
    lastbusiness = business[-1]

    # latest entertainment news
    entertainment = []
    for i in allnews:
        if i.category.category == "ENTERTAINMENT":
            entertainment.append(i)
    lastentertainment = entertainment[-1]

    # International news
    International = []
    for i in allnews:
        if i.subcat.subcat == "International-News":
            International.append(i)
    Internationalnews = International[-5:-1]

    # Breaking news
    Breaking = []
    for i in allnews:
        if i.subcat.subcat == "Breaking-News":
            Breaking.append(i)
    Breakingnews = Breaking[-5:-1]

    news_list = news.objects.all().order_by('-id')[1:7][::-1]
    latest_news = news.objects.latest('date')
    args = {'news': news_list, 'latest_news': latest_news, 'allnews': allnews,
            'lastsport': lastsport, 'lastentertainment': lastentertainment, 'lastbusiness': lastbusiness,
            'Internationalnews': Internationalnews, 'Breakingnews': Breakingnews, 'cat': cat}
    return render(request, 'index.html', args)
# End user Logout

# ******************************************************************************************************************************
# ContactUs


def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = ContactUs(name=name, email=email,
                         subject=subject, message=message)
        data.save()
        messages.info(request, "Your message send successfuly.")
        return render(request, "contact.html")
    else:
        messages.info(request, "Please Input Valid Details.")
        return render(request, "contact.html")
# End ContactUs
# ******************************************************************************************************************************
# comments


def comment(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            comments = request.POST['comment']
            username = request.session['username']
            userid = request.session['userid']
            userimage = UserProfile.objects.get(user_id=userid)
            image = userimage.image
            newsid = id
            form = Comment(userid=userid, newsid=newsid,
                           username=username, userimage=image, comments=comments)
            form.save()
            com = Comment.objects.all().order_by('-id')[0:10]
            mynews = []
            allnews = news.objects.filter(id=id)
            for i in allnews:
                mynews.append(i)
            passnews = mynews[0]
            cat = subcategory.objects.all()
            latest_news = news.objects.latest('date')
            news_list = news.objects.all().order_by('-id')[1:7][::-1]
            counter = 0
            for i in com:
                if passnews.id == i.newsid:
                    counter = counter + 1
            counters = counter
            args = {'comment': com, 'mynews': passnews, 'cat': cat,
                    'latest_news': latest_news, 'news': news_list, 'counter': counters}
            return render(request, 'view_more.html', args)
        else:
            com = Comment.objects.all().order_by('-id')[0:4]
            mynews = []
            allnews = news.objects.filter(id=id)
            for i in allnews:
                mynews.append(i)
            passnews = mynews[0]
            counter = 0
            for i in com:
                if passnews.id == i.newsid:
                    counter = counter + 1
            counters = counter
            args = {'comment': com, 'mynews': passnews, 'counter': counters}
            return render(request, 'view_more.html')
    else:
        cat = subcategory.objects.all()
        latest_news = news.objects.latest('date')
        news_list = news.objects.all().order_by('-id')[1:7][::-1]
        args = {'cat': cat, 'latest_news': latest_news, 'news': news_list}
        messages.info(request, "Please First Login.")
        return render(request, 'user_login.html', args)


# ******************************************************************************************************************************
# Rest_Framework

class news_list(viewsets.ModelViewSet):
    queryset = news.objects.all()
    serializer_class = NewsSerializers
# End Rest_Framework

# ******************************************************************************************************************************
