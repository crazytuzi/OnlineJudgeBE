from django.db import models
from contests.models import Contests
# Create your models here.


class ProblemTag(models.Model):
    name = models.TextField()

    class Meta:
        db_table = "problem_tag"


class Problems(models.Model):
    # ID
    problem_id = models.IntegerField(db_index=True, default=0)
    # 比赛
    contest = models.ForeignKey(Contests, blank=True, null=True)
    # 标题
    title = models.CharField(unique=True, max_length=255)
    # 描述
    description = models.TextField(null=True)
    # 输入描述
    input_description = models.TextField(null=True)
    # 输出描述
    output_description = models.TextField(null=True)
    # 输入样例
    sample_input = models.TextField(null=True)
    # 输出样例
    sample_output = models.TextField(null=True)
    # 时间限制
    time_limit = models.IntegerField()
    # 空间限制
    memory_limit = models.IntegerField()
    # 提交数量
    submission_number = models.IntegerField(default=0)
    # 通过数量
    accepted_number = models.IntegerField(default=0)
    # 答案错误
    wrong_answer_number = models.IntegerField(default=0)
    # 超过时间
    time_limit_number = models.IntegerField(default=0)
    # 超过空间
    memory_limit_number = models.IntegerField(default=0)
    # 运行错误
    runtime_error_number = models.IntegerField(default=0)
    # 超过输出
    output_limit_number = models.IntegerField(default=0)
    # 编译错误
    compile_error_number = models.IntegerField(default=0)
    # 格式错误
    presentation_error_number = models.IntegerField(default=0)
    # 标签
    tags = models.ManyToManyField(ProblemTag, blank=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "problem"
        db_table = "problems"

    def add_submission_number(self):
        self.submission_number = models.F("submission_number") + 1
        self.save(update_fields=["submission_number"])

    def add_accepted_number(self):
        self.accepted_number = models.F("accepted_number") + 1
        self.save(update_fields=["accepted_number"])

    def add_wrong_answer_number(self):
        self.wrong_answer_number = models.F("wrong_answer_number") + 1
        self.save(update_fields=["wrong_answer_number"])

    def add_time_limit_number(self):
        self.time_limit_number = models.F("time_limit_number") + 1
        self.save(update_fields=["time_limit_number"])

    def add_memory_limit_number(self):
        self.memory_limit_number = models.F("memory_limit_number") + 1
        self.save(update_fields=["memory_limit_number"])

    def add_runtime_error_number(self):
        self.runtime_error_number = models.F("runtime_error_number") + 1
        self.save(update_fields=["runtime_error_number"])

    def add_output_limit_number(self):
        self.output_limit_number = models.F("output_limit_number") + 1
        self.save(update_fields=["output_limit_number"])

    def add_compile_error_number(self):
        self.compile_error_number = models.F("compile_error_number") + 1
        self.save(update_fields=["compile_error_number"])

    def add_presentation_error_number(self):
        self.accepted_number = models.F("presentation_error_number") + 1
        self.save(update_fields=["presentation_error_number"])
