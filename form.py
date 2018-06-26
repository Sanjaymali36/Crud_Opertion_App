from django import forms

#Form Validation code
class LenghtException():
    pass
class EmployeeForm(forms.Form):
    name=forms.CharField(required =True,max_length=30)
    email=forms.EmailField(required =True)
    mobile=forms.CharField(max_length=10)
    
    def clean_name(self):
    	data =self.cleaned_data['name']
        if len(data)<=3:
            raise forms.ValidationError('name must contains 4 charcters')
        return data

    def clean_email(self):
    	data =self.cleaned_data['email']
        if not data.endswith('.com'):
            raise forms.ValidationError('name must contains .com')
        return data
    def clean_mobile(self):
    	data =self.cleaned_data['mobile']
        try:
            if len(data)!=10:
	        raise LengthException()
            else:
                data = int(data)
	except LengthException:
            raise forms.ValidationError('name must contains 10 charcters')
        except LengthException:
            raise forms.ValidationError('name must contains integer')
        return data
	
   
