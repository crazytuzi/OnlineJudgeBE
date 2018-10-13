from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from .models import Problems
from .serializers import ProblemsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProblemsFilter

# Create your views here.


class ProblemsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class ProblemsListViewSet(
        CacheResponseMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    """

    <style>.content-main div{width:100%;}</style>
    <script src="https://cdn.bootcss.com/jquery/2.1.1/jquery.min.js"></script>
    <script>
        $(function(){
             $("#en").css("display","none")
             $("#li_cn").click(function(){
                  $("#en").css("display","none")
                  $("#cn").css("display","")
              });
              $("#li_en").click(function(){
                  $("#cn").css("display","none")
                  $("#en").css("display","")
              });
          }
        )
    </script>
    <h4>获取所有题目数据</h4>
    <lable>请求数据地址：<a href="/api/problems/">/problems/</a></lable>
    <table class="table table-bordered">
    <caption>参数文档</caption>
    <thead><tr><th>参数名称</th><th>类型</th><th>描述</th><th>是否必须</th><th>参数选择</th><th>默认值</th></tr></thead>
    <tbody><tr><td>language</td><td>string</td><td>默认语言</td><td>否</td><td>cn | en</td><td>cn</td></tr>
    <tr><td>page_index</td><td>int</td><td>页码</td><td>否</td><td>1</td><td>1</td></tr>
    <tr><td>page_size</td><td>int</td><td>每页条数</td><td>否</td><td>10</td><td>10</td></tr>
    <tr><td>启用禁用字段名</td><td>string</td><td>启用/禁用</td><td>否</td><td>yes</td><td>yes | no</td></tr>
    <tr><td>format</td><td>string</td><td>返回数据格式</td><td>否</td><td>json | api</td><td>json</td></tr></tbody></table>
    <!--语言选择-->
    <ul  class="nav nav-tabs" style="float:left;">
    <li id="li_cn" class="active"><a href="#cn" data-toggle="tab">CN</a></li>
    <li id="li_en"><a href="#en" data-toggle="tab">EN</a></li>
    </ul>
    <!--CN字段表格-->
    <table id="cn" class="table table-bordered tab-pane fade in active">
    <caption>CN返回数据文档</caption>
    <thead><tr><th>字段名名称</th><th>类型</th><th>描述</th></tr></thead>
    <tbody>
    <tr><td>code</td><td>int</td><td>状态码</td></tr>
    <tr><td>msg</td><td>string</td><td>状态描述</td></tr>
    <tr><td>page_index</td><td>int</td><td>当前页</td></tr>
    <tr><td>page_size</td><td>int</td><td>每页条数</td></tr>
    <tr><td>page_total</td><td>int</td><td>总页数</td></tr>
    <tr><td>record_count</td><td>int</td><td>总条数</td></tr>
    <tr><td>problem_id</td><td>None</td><td>标题</td></tr>
    <tr><td>description</td><td>string</td><td>题目描述</td></tr>
    <tr><td>input_description</td><td>string</td><td>输入描述</td></tr>
    <tr><td>output_description</td><td>string</td><td>输出描述</td></tr>
    <tr><td>sample_input</td><td>string</td><td>输入样例</td></tr>
    <tr><td>sample_output</td><td>string</td><td>输出样例</td></tr>
    <tr><td>time_limit</td><td>int</td><td>时间限制</td></tr>
    <tr><td>memory_limit</td><td>int</td><td>空间限制</td></tr>
    <tr><td>submission_number</td><td>int</td><td>提交数量</td></tr>
    <tr><td>accepted_number</td><td>int</td><td>通过数量</td></tr>
    <tr><td>wrong_answer_number</td><td>int</td><td>答案错误</td></tr>
    <tr><td>time_limit_number</td><td>int</td><td>超过时间</td></tr>
    <tr><td>memory_limit_number</td><td>int</td><td>超过空间</td></tr>
    <tr><td>runtime_error_number</td><td>int</td><td>运行错误</td></tr>
    <tr><td>output_limit_number</td><td>int</td><td>超过输出</td></tr>
    <tr><td>compile_error_number</td><td>int</td><td>编译错误</td></tr>
    <tr><td>presentation_error_number</td><td>None</td><td>标签</td></tr>
    <tr><td>create_time</td><td>None</td><td>创建时间</td></tr>
    </tbody>
    </table>
    <!--EN表格-->
    <table id="en" class="table table-bordered tab-pane fade">
    <caption>EN返回数据文档</caption>
    <thead><tr><th>字段名名称</th><th>类型</th><th>描述</th></tr></thead>
    <tbody>
    <tr><td>code</td><td>int</td><td>状态码</td></tr>
    <tr><td>msg</td><td>string</td><td>状态描述</td></tr>
    <tr><td>page_index</td><td>int</td><td>当前页</td></tr>
    <tr><td>page_size</td><td>int</td><td>每页条数</td></tr>
    <tr><td>page_total</td><td>int</td><td>总页数</td></tr>
    <tr><td>record_count</td><td>int</td><td>总条数</td></tr>
    <tr><td>problem_id</td><td>None</td><td>标题</td></tr>
    <tr><td>description</td><td>string</td><td>题目描述</td></tr>
    <tr><td>input_description</td><td>string</td><td>输入描述</td></tr>
    <tr><td>output_description</td><td>string</td><td>输出描述</td></tr>
    <tr><td>sample_input</td><td>string</td><td>输入样例</td></tr>
    <tr><td>sample_output</td><td>string</td><td>输出样例</td></tr>
    <tr><td>time_limit</td><td>int</td><td>时间限制</td></tr>
    <tr><td>memory_limit</td><td>int</td><td>空间限制</td></tr>
    <tr><td>submission_number</td><td>int</td><td>提交数量</td></tr>
    <tr><td>accepted_number</td><td>int</td><td>通过数量</td></tr>
    <tr><td>wrong_answer_number</td><td>int</td><td>答案错误</td></tr>
    <tr><td>time_limit_number</td><td>int</td><td>超过时间</td></tr>
    <tr><td>memory_limit_number</td><td>int</td><td>超过空间</td></tr>
    <tr><td>runtime_error_number</td><td>int</td><td>运行错误</td></tr>
    <tr><td>output_limit_number</td><td>int</td><td>超过输出</td></tr>
    <tr><td>compile_error_number</td><td>int</td><td>编译错误</td></tr>
    <tr><td>presentation_error_number</td><td>None</td><td>标签</td></tr>
    <tr><td>create_time</td><td>None</td><td>创建时间</td></tr>
    </tbody>
    </table>

    """
    queryset = Problems.objects.all()
    serializer_class = ProblemsSerializer
    pagination_class = ProblemsPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filter_class = ProblemsFilter
    ordering_fields = ('problem_id',)
