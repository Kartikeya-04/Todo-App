

from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Fieldset, Submit

from .models import Employee


class FeedbackForm(forms.Form):
    Email = forms.EmailField(label='Enter Your Email', max_length=100)
    UserName = forms.CharField(label='Enter Your Name', max_length=100)
    Feedback = forms.CharField(label='Please Give Your Feedback Here!', widget=forms.Textarea)

    # Adding form-control to the fields for Bootstrap styling
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Feedback Form',
                'Email',
                'UserName',
                'Feedback'
            ),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )


#form using model
class EmpForm():
    class Meta:
        model=Employee
        fields=['name','emp_id','phone',]