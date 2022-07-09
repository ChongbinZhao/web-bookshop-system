import hashlib

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from app01 import models

# Create your views here.

# 出版社展示列表
from app01.models import LmsUser
from app01.models import Customer


def publisher_list(request):
    publisher = models.Publisher.objects.all()
    return render(request, 'pub_list.html', {'pub_list': publisher})


# 添加出版社

def add_publisher(request):
    if request.method == 'POST':
        new_publisher_name = request.POST.get('name')
        new_publisher_addr = request.POST.get('addr')
        models.Publisher.objects.create(name=new_publisher_name, addr=new_publisher_addr)
        return redirect('/pub_list/')
    return render(request, 'pub_add.html')


# 编辑出版社

def edit_publisher(request):
    if request.method == 'POST':
        edit_id = request.GET.get('id')
        edit_obj = models.Publisher.objects.get(id=edit_id)
        new_name = request.POST.get('edit_name')
        new_addr = request.POST.get('edit_addr')
        edit_obj.name = new_name
        edit_obj.addr = new_addr
        edit_obj.save()
        return redirect('/pub_list/')

    edit_id = request.GET.get('id')
    edit_obj = models.Publisher.objects.get(id=edit_id)
    return render(request, 'pub_edit.html', {'publisher': edit_obj})


# 删除出版社

def drop_publisher(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Publisher.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/pub_list/')


# 作者的列表
def author_list(request):
    author = models.Author.objects.all()
    return render(request, 'auth_list.html', {'author_list': author})


# 添加作者
def add_author(request):
    if request.method == 'POST':
        new_author_name = request.POST.get('name')
        new_author_sex = request.POST.get('sex')
        new_author_age = request.POST.get('age')
        new_author_tel = request.POST.get('tel')
        models.Author.objects.create(name=new_author_name, sex=new_author_sex, age=new_author_age, tel=new_author_tel)
        return redirect('/author_list/')
    return render(request, 'author_add.html')


# 删除作者
def drop_author(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Author.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/author_list/')


# 修改作者
def edit_author(request):
    if request.method == 'POST':
        edit_id = request.GET.get('id')
        edit_obj = models.Author.objects.get(id=edit_id)
        new_author_name = request.POST.get('edit_name')
        new_author_sex = request.POST.get('edit_sex')
        new_author_age = request.POST.get('edit_age')
        new_author_tel = request.POST.get('edit_tel')
        new_book_id = request.POST.getlist('book_id')
        edit_obj.name = new_author_name
        edit_obj.sex = new_author_sex
        edit_obj.age = new_author_age
        edit_obj.tel = new_author_tel
        edit_obj.book.set(new_book_id)
        edit_obj.save()
        return redirect('/author_list/')
    edit_id = request.GET.get('id')
    edit_obj = models.Author.objects.get(id=edit_id)
    all_book = models.Book.objects.all()
    return render(request, 'auth_edit.html', {
        'author': edit_obj,
        'book_list': all_book
    })


# 书籍列表
def book_list(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book_list': book})


# 添加书籍
def add_book(request):
    if request.method == 'POST':
        new_book_name = request.POST.get('name')
        new_book_ISBN = request.POST.get('ISBN')
        new_book_translator = request.POST.get('translator')
        new_book_date = request.POST.get('date')
        publisher_id = request.POST.get('publisher_id')
        models.Book.objects.create(name=new_book_name, publisher_id=publisher_id, ISBN=new_book_ISBN,
                                   translator=new_book_translator, date=new_book_date)
        return redirect('/book_list/')  # 成功提交后就返回book_list
    res = models.Publisher.objects.all()
    return render(request, 'book_add.html', {'publisher_list': res})  # 点击返回就返回publisher_list?


# 删除书籍
def drop_book(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Book.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/book_list/')


# 完成订单
def order_finished(request):
    finish_id = request.GET.get('id')
    finish_obj = models.Orders.objects.get(id=finish_id)
    finish_obj.delete()
    return redirect('/customer_order_list/')


# 编辑书籍
def edit_book(request):
    if request.method == 'POST':
        new_book_name = request.POST.get('name')
        new_book_ISBN = request.POST.get('ISBN')
        new_book_translator = request.POST.get('translator')
        new_book_date = request.POST.get('date')
        new_publisher_id = request.POST.get('publisher_id')
        edit_id = request.GET.get('id')
        edit_obj = models.Book.objects.get(id=edit_id)
        edit_obj.name = new_book_name
        edit_obj.ISBN = new_book_ISBN
        edit_obj.translator = new_book_translator
        edit_obj.date = new_book_date
        edit_obj.publisher_id = new_publisher_id
        edit_obj.save()
        return redirect('/book_list/')
    edit_id = request.GET.get('id')
    edit_obj = models.Book.objects.get(id=edit_id)
    all_publisher = models.Publisher.objects.all()
    return render(request, 'book_edit.html', {'book': edit_obj, 'publisher_list': all_publisher})


# 顾客修改订单
def order_modify(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        mobile = request.POST.get('mobile')
        addr = request.POST.get('addr')
        edit_id = request.GET.get('id')
        edit_obj = models.Orders.objects.get(id=edit_id)
        edit_obj.customer_name = customer_name
        edit_obj.mobile = mobile
        edit_obj.addr = addr
        edit_obj.save()
        return redirect('/customer_order_list/')  # 成功提交就返回book_purchasing_list
    edit_id = request.GET.get('id')
    edit_obj = models.Orders.objects.get(id=edit_id)
    # 否则返回book_purchasing_list
    return render(request, 'order_modify.html', {'order': edit_obj})


# 购书列表
def book_purchasing_list(request):
    book_purchasing = models.Book.objects.all()
    return render(request, 'book_purchasing.html', {'book_purchasing_list': book_purchasing})


# 顾客选中图书购买，创建订单
def add_order(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        customer_name = request.POST.get('customer_name')
        number = request.POST.get('number')
        mobile = request.POST.get('mobile')
        addr = request.POST.get('addr')
        models.Orders.objects.create(book_name=book_name, customer_name=customer_name,
                                     number=number, mobile=mobile, addr=addr)
        edit_id = request.GET.get('id')
        edit_obj = models.Book.objects.get(id=edit_id)
        edit_obj.inventory -= int(number)
        edit_obj.save()
        return redirect('/book_purchasing_list/')  # 成功提交就返回book_purchasing_list
    edit_id = request.GET.get('id')
    edit_obj = models.Book.objects.get(id=edit_id)
    # 否则返回book_purchasing_list
    return render(request, 'add_order.html', {'book': edit_obj})


# 顾客查看订单中心
def customer_order_list(request):
    orders = models.Orders.objects.all()
    return render(request, 'customer_order_list.html', {'customer_orders': orders})


# 管理员查看订单
def library_order_list(request):
    orders = models.Orders.objects.all()
    return render(request, 'library_order_list.html', {'library_orders': orders})


# 密码加密
def setPassword(password):
    """
    加密密码，算法单次md5
    :param apssword: 传入的密码
    :return: 加密后的密码
    """
    md5 = hashlib.md5()
    md5.update(password.encode())
    password = md5.hexdigest()
    return str(password)


# 管理员登录

def login(request):
    if request.method == 'POST' and request.POST:
        email = request.POST.get("email")
        password = request.POST.get("password")
        e = LmsUser.objects.filter(email=email).first()
        if e:
            now_password = setPassword(password)
            db_password = e.password
            if now_password == db_password:
                # return render(request, "pub_list.html")
                response = HttpResponseRedirect('/pub_list/')
                response.set_cookie("username", e.username)
                return response

    return render(request, "login.html")


# 管理员注册

def register(request):
    if request.method == "POST" and request.POST:
        data = request.POST
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        mobile = data.get("mobile")
        LmsUser.objects.create(
            username=username,
            email=email,
            password=setPassword(password),
            # password=password,
            mobile=mobile,
        )
        return HttpResponseRedirect('/login/')
    return render(request, "register.html")


# 顾客登录
def customer_login(request):
    if request.method == 'POST' and request.POST:
        email = request.POST.get("email")
        password = request.POST.get("password")
        e = Customer.objects.filter(email=email).first()
        if e:
            now_password = setPassword(password)
            db_password = e.password
            if now_password == db_password:
                # return render(request, "pub_list.html")
                response = HttpResponseRedirect('/book_purchasing_list/')
                response.set_cookie("username", e.username)
                return response

    return render(request, "customer_login.html")


# 顾客注册
def customer_register(request):
    if request.method == "POST" and request.POST:
        data = request.POST
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        mobile = data.get("mobile")
        Customer.objects.create(
            username=username,
            email=email,
            password=setPassword(password),
            # password=password,
            mobile=mobile,
        )
        return HttpResponseRedirect('/customer_login/')
    return render(request, "customer_register.html")


