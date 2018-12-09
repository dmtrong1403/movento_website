from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Họ tên',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Họ tên'",
                'class': "common-input mb-20 form-control",
            }
        )
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Email'",
                'class': "common-input mb-20 form-control",
                'pattern': "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$",
            }
        )
    )
    phone = forms.CharField(
        max_length=12,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Số điện thoại',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Số điện thoại'",
                'class': "common-input mb-20 form-control",
                'pattern': "[0-9]{10}",
            }
        )
    )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Mô tả yêu cầu',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Mô tả yêu cầu'",
                'class': "common-input mb-20 form-control",
            }
        )
    )
