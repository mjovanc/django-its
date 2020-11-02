from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class IssueType(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Issue Type')
        verbose_name_plural = _('Issue Types')


class IssuePriority(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Issue Priority')
        verbose_name_plural = _('Issue Priorities')


class Issue(models.Model):
    STATUSES = (
        ('Open', _('Open')),
        ('Reopen', _('Reopen')),
        ('In Progress', _('In Progress')),
        ('Fixed', _('Fixed')),
        ('Closed', _('Closed')),
    )

    title = models.CharField(verbose_name=_('Title'), max_length=200)
    description = models.TextField(verbose_name=_('Description'), max_length=10000)
    priority = models.ForeignKey(IssuePriority, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(IssueType, on_delete=models.SET_NULL, null=True)
    status = models.CharField(verbose_name=_('Status'), max_length=50, choices=STATUSES, default='Open')
    linked_issues = models.ManyToManyField('self', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='author_users')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assign_to_users')
    add_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Issue')
        verbose_name_plural = _('Issues')
