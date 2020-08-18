#!/usr/bin/env python
"""This file is part of the django ERP project.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__author__ = 'Emanuele Bertoldi <emanuele.bertoldi@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015, django ERP Team'
__version__ = '0.0.5'


from django.db import models
from ..models import User, Group
        

class TestModelInstance(models.Model):
    id = models.PositiveIntegerField(default=5, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(default="fake_object")
    url = models.URLField(default="http://localhost:8000/test")
    email = models.EmailField(default="u@u.it")
    choice = models.TextField(default="test", choices=[("test", "A test")])
    flag = models.BooleanField(default=True)

    class Meta:
        abstract = True
