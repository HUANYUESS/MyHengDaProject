from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):  #建立模型表单类
    class Meta:   #通过元信息类进行模型的定制化
        model = Resume  #需要定制化的模型
        fields = ('name', 'sex', 'personID', 'email', 'birth', 'edu', 'school',
                  'major', 'experience', 'position', 'photo')  #需要定制化的字段
        sex_list = (
            ('男', '男'),
            ('女', '女'),
        )
        edu_list = (
            ('大专', '大专'),
            ('本科', '本科'),
            ('硕士', '硕士'),
            ('博士', '博士'),
            ('其它', '其它'),
        )
        widgets = {
            'sex': forms.Select(choices=sex_list),
            'edu': forms.Select(choices=edu_list),
            'photo': forms.FileInput(),
        }

