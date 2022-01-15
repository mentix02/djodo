from django import template

from task.models import Task

register = template.Library()


@register.filter(name='severity_color_class')
def severity_color_class(task):
    """
    Return the color CSS class associated with task severity.
    """

    if not isinstance(task, Task):
        return ''

    if task.severity == Task.SEVERITY_HIGH:
        return 'danger'
    elif task.severity == Task.SEVERITY_MEDIUM:
        return 'warning'
    else:
        return 'light'
