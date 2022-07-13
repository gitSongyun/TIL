# REST API



- api_view decorator

  기본적으로 GET 메서드만 허용되며 views에서 함수 선언할 때 반드시 써줘야 한다. 
  DRF에서는 선택이 아닌 필수적으로 작성해야 view 함수가 정상적으로 동작한다. 







이 안에서 post인지만 따로 처리하면 같은 url로 생성의 역할을 할 수 있다. 

 

````python
@api_view(['GET'])
def article_list(request):
    # articles = Article.objects.all()
    articles = get_list_or_404(Article)
    # multiple object 이므로 many=True 가 필요하다. 
    serializer = ArticleListSerializer(articles, many=True) 
    return Response(serializer.data)
````

따라서, 다음과 같이 method에 따라 구문을 나눠서 작성을 하면 된다. 

```python
@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        # multiple object 이므로 many=True 가 필요하다. 
        serializer = ArticleListSerializer(articles, many=True) 
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer()
    
  
```

