from django.shortcuts import render
from brmapp.forms import NewBookFrom,SearchFrom
from brmapp import models
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='/userlogin')
def newbook(request):
    form=NewBookFrom()
    res=render(request,'new-book.html',{'form':form})
    return(res)
@login_required(login_url='/userlogin')
def send(request):
    if request.method=='POST':
      form=NewBookFrom(request.POST)
      book=models.Book()
      book.title=form.data['title']
      book.price=form.data['price']
      book.author=form.data['author']
      book.publisher=form.data['publisher']
      book.save()
      s="Record stored<br><a href='view-books'>View All Books</a>"
      return HttpResponse(s)
@login_required(login_url='/userlogin')
def viewbooks(request):
   books=models.Book.objects.all()
   #username=request.GET['username']
   res=render(request,'view-books.html',{'books':books})
   return res
@login_required(login_url='/userlogin')
def editbook(request):
   book=models.Book.objects.get(id=request.GET['bookid'])
   fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
   form=NewBookFrom(initial=fields)
   res=render(request,'edit-book.html',{'form':form,'book':book})
   return res
@login_required(login_url='/userlogin')
def edit(request):
    if request.method=='POST':
        form=NewBookFrom(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
        return HttpResponseRedirect('view-books')
@login_required(login_url='/userlogin')
def deletebook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('view-books')
@login_required(login_url='/userlogin')
def searchbook(request):
    form=SearchFrom()
    res=render(request,'search-book.html',{'form':form})
    return res
@login_required(login_url='/userlogin')
def search(request):
    form=SearchFrom(request.POST)
    books=models.Book.objects.filter(title=form.data['title'])
    res=render(request,'search-book.html',{'form':form,'books':books})
    return res

def userlogin(request):
    data={}
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect('view-books')

        else:
             data['error']="incorrect username and password"
             return render(request,'userlogin.html',data)
    else:
        return render(request,'userlogin.html')

def userlogout(request):
     logout(request)
     return HttpResponseRedirect('userlogin')    






