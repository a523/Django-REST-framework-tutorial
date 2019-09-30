DRF 快速开始代码

https://www.django-rest-framework.org/tutorial/1-serialization/

--------------------------
## 笔记

>ViewSets & Routers > generics.ListCreateAPIView >  generics.GenericAPIView + mixins > APIView + method

依赖 model 关系由强转弱
- 使用类视图
> commit: 5e92c89eeaa792da4cd13a3cb42bbc0404aa49dc
- 使用通用类视图
> commit: 112b9e2ea1ad847d0ed4da4aac54d8bf562f86d6
- 自定义权限：
> 8f2b222d999c060154bfbe80e230c4d1b7ca5663


### ViewSets
> 以model为中心
```python
from rest_framework import viewsets
from rest_framework.decorators import action
viewsets.ModelViewSet
# 可以通过 action 装饰器自定义路径和视图，默认是get方法，可以method='XXX'，修改
# 自定义保存对象的方法
# 通过重写 perform_create(self, serializer) 函数
# 视图集可以通过DefaultRouter 生成url
from rest_framework.routers import DefaultRouter
```
### 通用的基于类的视图

```python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
```
### 关系和超链接API
HyperlinkedModelSerializer  
serializers.HyperlinkedRelatedField 
可以连接另外一个接口
#### 分页
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

### 请求和响应
```python
request.POST  # 只处理表单数据  只适用于'POST'方法
request.data  # 处理任意数据  适用于'POST'，'PUT'和'PATCH'方法
```
#### 保存数据时触发
在model 里面 重写 def save(self, *args, **kwargs) 方法可以
执行在存数据的时候触发做其他的事情。
