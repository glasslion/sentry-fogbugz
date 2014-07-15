# -*- coding: utf-8 -*-
import urlparse

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from sentry.plugins.bases.issue import IssuePlugin

import fborm

import sentry_fogbugz 

class FogbugzOptionsForm(forms.Form):
    host_url = forms.URLField(
        help_text=_("With schema and trailing slash e.g. https://fogcreek.fogbugz.com/"))
    secret_token = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'span9'}))
    area = forms.CharField(
        label="Case Area (Optional)",
        required=False, widget=forms.TextInput(attrs={'class': 'span9'}))
    category = forms.CharField(
        label="Case Category (Optional)",
        required=False, widget=forms.TextInput(attrs={'class': 'span9'}))
    project = forms.CharField(
        label="Case Project (Optional)",
        required=False, widget=forms.TextInput(attrs={'class': 'span9'}))


    def clean(self):
        config = self.cleaned_data
        if not all(config.get(k) for k in ('host_url', 'secret_token')):
            raise forms.ValidationError('Missing required configuration value')
        return config


class FogbugzPlugin(IssuePlugin):
    author = 'Lijian'
    author_url ='https://github.com/glasslion/sentry-fogbugz'
    version = sentry_fogbugz.VERSION
    description = "Integrate Fogbugz."
    resource_links = [
        ('Bug Tracker', 'https://github.com/glasslion/sentry-fogbugz/issues'),
        ('Source', author_url),
    ]

    slug = 'fogbugz'
    title = _('Fogbugz')
    conf_title = title
    conf_key = slug
    project_conf_form = FogbugzOptionsForm

    def is_configured(self, project, **kwargs):
        return all((self.get_option(k, project) for k in ('host_url', 'secret_token')))

    def get_new_issue_title(self, **kwargs):
        return 'Create Fogbugz case'

    def create_issue(self, group, form_data, **kwargs):
        """Create a Fogbugz case"""
        pass

    def get_issue_url(self, group, issue_id, **kwargs):
        host = self.get_option('host_url', group.project)
        return urlparse.urljoin(host, 'f/cases/%s' % issue_id)
