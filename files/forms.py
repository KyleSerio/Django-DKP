from django import forms

class UploadFileForm(forms.Form):
    logTypes =(
        ("1", "Guild Dump"),
        ("2", "Raid Dump"),
        ("3", "Wins Dump"),
    )
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    type = forms.MultipleChoiceField(choices = logTypes)
    #Automagically adds class="form-control" to each field, making it prettier
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class editWins(forms.Form):
    winner = forms.CharField(label="Winner", max_length=50)
    item = forms.CharField(label="Item Name", max_length=50)
    amount = forms.IntegerField()
    date = forms.DateField()