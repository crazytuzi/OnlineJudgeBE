from django.db import models
from contests.models import Contests
from Utlis.JudgeStatus import JudgeStatus
from apps.users.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.


class ProblemTag(models.Model):
    name = models.TextField(verbose_name="标签名")

    class Meta:
        db_table = "problem_tag"


class Problems(models.Model):
    problem_id = models.IntegerField(
        db_index=True, default=0, verbose_name="题目编号")
    parent_problem = models.ForeignKey(
        "self", null=True, blank=True)
    contest = models.ForeignKey(
        Contests,
        null=True,
        blank=True,
        verbose_name="比赛")
    title = models.CharField(max_length=255, verbose_name="标题")
    description = models.TextField(null=True, verbose_name="题目描述")
    input_description = models.TextField(null=True, verbose_name="输入描述")
    output_description = models.TextField(null=True, verbose_name="输出描述")
    sample_input = models.TextField(null=True, verbose_name="输入样例")
    sample_output = models.TextField(null=True, verbose_name="输出样例")
    time_limit = models.IntegerField(default=1000, verbose_name="时间限制")
    memory_limit = models.IntegerField(default=64, verbose_name="空间限制")
    submission_number = models.IntegerField(default=0, verbose_name="提交数量")
    accepted_number = models.IntegerField(default=0, verbose_name="通过数量")
    wrong_answer_number = models.IntegerField(default=0, verbose_name="答案错误")
    time_limit_number = models.IntegerField(default=0, verbose_name="超过时间")
    memory_limit_number = models.IntegerField(default=0, verbose_name="超过空间")
    runtime_error_number = models.IntegerField(default=0, verbose_name="运行错误")
    output_limit_number = models.IntegerField(default=0, verbose_name="超过输出")
    compile_error_number = models.IntegerField(default=0, verbose_name="编译错误")
    presentation_error_number = models.IntegerField(
        default=0, verbose_name="格式错误")
    other_error_number = models.IntegerField(default=0, verbose_name="其他错误")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    tags = models.ManyToManyField(
        ProblemTag,
        blank=True,
        verbose_name="标签")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "题目"
        verbose_name_plural = verbose_name
        db_table = "problems"

    def update_submission(self, status, user):
        from user_operation.models import UserChallengingProblems
        if self.contest is None:
            self.add_submission_number()
            userProfile = UserProfile.objects.get(user=user)
            userProfile.add_submission_number()
            if status == JudgeStatus.ACCEPTED:
                from user_operation.models import UserAcceptedProblems
                self.add_accepted_number()
                obj, created = UserAcceptedProblems.objects.get_or_create(
                    user=user, problem=self)
                if created:
                    userProfile.add_accepted_number()
                    try:
                        UserChallengingProblems.objects.get(
                            user=user, problem=self).delete()
                    except ObjectDoesNotExist:
                        pass
                userProfile.sortUserRankList()
                return
            elif status == JudgeStatus.WRONG_ANSWER:
                self.add_wrong_answer_number()
            elif status == JudgeStatus.TIME_LIMIT_EXCEED:
                self.add_time_limit_number()
            elif status == JudgeStatus.MEMORY_LIMIT_EXCEED:
                self.add_memory_limit_number()
            elif status == JudgeStatus.RUNTIME_ERROR:
                self.add_runtime_error_number()
            elif status == JudgeStatus.OUTPUT_LIMIT_EXCEED:
                self.add_output_limit_number()
            elif status == JudgeStatus.COMPILE_ERROR:
                self.add_compile_error_number()
            elif status == JudgeStatus.PRESENTATION_ERROR:
                self.add_presentation_error_number()
            else:
                self.add_other_error_number()
            UserChallengingProblems.objects.get_or_create(
                user=user, problem=self)
            userProfile.sortUserRankList()
        else:
            if self.contest.isOverdue() is True:
                return
            self.add_submission_number()
            if status == JudgeStatus.ACCEPTED:
                from user_operation.models import UserAcceptedProblems
                self.add_accepted_number()
                obj, created = UserAcceptedProblems.objects.get_or_create(
                    user=user, problem=self)
                if created:
                    from contests.models import ContestRankList
                    obj, created = ContestRankList.objects.get_or_create(
                        contest=self.contest, user=user)
                    if obj.accepted + \
                            1 <= Problems.objects.filter(contest=self.contest).count():
                        obj.accepted = obj.accepted + 1
                        from submissions.models import Submissions
                        submission = Submissions.objects.filter(
                            user=user, problem=self).last()
                        obj.preaccepted_time = submission.submit_time
                        obj.save()
                    try:
                        UserChallengingProblems.objects.get(
                            user=user, problem=self).delete()
                    except ObjectDoesNotExist:
                        pass
                return
            elif status == JudgeStatus.WRONG_ANSWER:
                self.add_wrong_answer_number()
            elif status == JudgeStatus.TIME_LIMIT_EXCEED:
                self.add_time_limit_number()
            elif status == JudgeStatus.MEMORY_LIMIT_EXCEED:
                self.add_memory_limit_number()
            elif status == JudgeStatus.RUNTIME_ERROR:
                self.add_runtime_error_number()
            elif status == JudgeStatus.OUTPUT_LIMIT_EXCEED:
                self.add_output_limit_number()
            elif status == JudgeStatus.COMPILE_ERROR:
                self.add_compile_error_number()
            elif status == JudgeStatus.PRESENTATION_ERROR:
                self.add_presentation_error_number()
            else:
                self.add_other_error_number()
            UserChallengingProblems.objects.get_or_create(
                user=user, problem=self)

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

    def add_other_error_number(self):
        self.other_error_number = models.F("other_error_number") + 1
        self.save(update_fields=["other_error_number"])
